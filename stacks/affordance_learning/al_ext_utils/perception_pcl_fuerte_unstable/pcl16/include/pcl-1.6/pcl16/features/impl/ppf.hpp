/*
 * Software License Agreement (BSD License)
 *
 *  Point Cloud Library (PCL) - www.pointclouds.org
 *  Copyright (c) 2011, Alexandru-Eugen Ichim
 *                      Willow Garage, Inc
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *
 * $Id: ppf.hpp 5036 2012-03-12 08:54:15Z rusu $
 */

#ifndef PCL16_FEATURES_IMPL_PPF_H_
#define PCL16_FEATURES_IMPL_PPF_H_

#include <pcl16/features/ppf.h>
#include <pcl16/features/pfh.h>

//////////////////////////////////////////////////////////////////////////////////////////////
template <typename PointInT, typename PointNT, typename PointOutT>
pcl16::PPFEstimation<PointInT, PointNT, PointOutT>::PPFEstimation ()
    : FeatureFromNormals <PointInT, PointNT, PointOutT> ()
{
  feature_name_ = "PPFEstimation";
  // Slight hack in order to pass the check for the presence of a search method in Feature::initCompute ()
  Feature<PointInT, PointOutT>::tree_.reset (new pcl16::search::KdTree <PointInT> ());
  Feature<PointInT, PointOutT>::search_radius_ = 1.0f;
}


//////////////////////////////////////////////////////////////////////////////////////////////
template <typename PointInT, typename PointNT, typename PointOutT> void
pcl16::PPFEstimation<PointInT, PointNT, PointOutT>::computeFeature (PointCloudOut &output)
{
  // Initialize output container - overwrite the sizes done by Feature::initCompute ()
  output.points.resize (indices_->size () * input_->points.size ());
  output.height = 1;
  output.width = static_cast<uint32_t> (output.points.size ());
  output.is_dense = true;

  // Compute point pair features for every pair of points in the cloud
  for (size_t index_i = 0; index_i < indices_->size (); ++index_i)
  {
    size_t i = (*indices_)[index_i];
    for (size_t j = 0 ; j < input_->points.size (); ++j)
    {
      PointOutT p;
      if (i != j)
      {
        if (//pcl16::computePPFPairFeature
            pcl16::computePairFeatures (input_->points[i].getVector4fMap (),
                                      normals_->points[i].getNormalVector4fMap (),
                                      input_->points[j].getVector4fMap (),
                                      normals_->points[j].getNormalVector4fMap (),
                                      p.f1, p.f2, p.f3, p.f4))
        {
          // Calculate alpha_m angle
          Eigen::Vector3f model_reference_point = input_->points[i].getVector3fMap (),
                          model_reference_normal = normals_->points[i].getNormalVector3fMap (),
                          model_point = input_->points[j].getVector3fMap ();
          Eigen::AngleAxisf rotation_mg (acosf (model_reference_normal.dot (Eigen::Vector3f::UnitX ())),
                                         model_reference_normal.cross (Eigen::Vector3f::UnitX ()).normalized ());
          Eigen::Affine3f transform_mg = Eigen::Translation3f ( rotation_mg * ((-1) * model_reference_point)) * rotation_mg;

          Eigen::Vector3f model_point_transformed = transform_mg * model_point;
          float angle = atan2f ( -model_point_transformed(2), model_point_transformed(1));
          if (sin (angle) * model_point_transformed(2) < 0.0f)
            angle *= (-1);
          p.alpha_m = -angle;
        }
        else
        {
          PCL16_ERROR ("[pcl16::%s::computeFeature] Computing pair feature vector between points %zu and %zu went wrong.\n", getClassName ().c_str (), i, j);
          p.f1 = p.f2 = p.f3 = p.f4 = p.alpha_m = std::numeric_limits<float>::quiet_NaN ();
          output.is_dense = false;
        }
      }
      // Do not calculate the feature for identity pairs (i, i) as they are not used
      // in the following computations
      else
      {
        p.f1 = p.f2 = p.f3 = p.f4 = p.alpha_m = std::numeric_limits<float>::quiet_NaN ();
        output.is_dense = false;
      }

      output.points[index_i*input_->points.size () + j] = p;
    }
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////
template <typename PointInT, typename PointNT> void
pcl16::PPFEstimation<PointInT, PointNT, Eigen::MatrixXf>::computeFeatureEigen (pcl16::PointCloud<Eigen::MatrixXf> &output)
{
  // Initialize output container - overwrite the sizes done by Feature::initCompute ()
  output.points.resize (indices_->size () * input_->points.size (), 5);
  output.height = 1;
  output.width = static_cast<uint32_t> (indices_->size () * input_->points.size ());

  output.is_dense = true;
  // Compute point pair features for every pair of points in the cloud
  for (size_t index_i = 0; index_i < indices_->size (); ++index_i)
  {
    size_t i = (*indices_)[index_i];
    for (size_t j = 0 ; j < input_->points.size (); ++j)
    {
      Eigen::VectorXf p (5);
      if (i != j)
      {
        if (//pcl16::computePPFPairFeature
            pcl16::computePairFeatures (input_->points[i].getVector4fMap (),
                                      normals_->points[i].getNormalVector4fMap (),
                                      input_->points[j].getVector4fMap (),
                                      normals_->points[j].getNormalVector4fMap (),
                                      p (0), p (1), p (2), p (3)))
        {
          // Calculate alpha_m angle
          Eigen::Vector3f model_reference_point = input_->points[i].getVector3fMap (),
                          model_reference_normal = normals_->points[i].getNormalVector3fMap (),
                          model_point = input_->points[j].getVector3fMap ();
          Eigen::AngleAxisf rotation_mg (acosf (model_reference_normal.dot (Eigen::Vector3f::UnitX ())),
                                         model_reference_normal.cross (Eigen::Vector3f::UnitX ()).normalized ());
          Eigen::Affine3f transform_mg = Eigen::Translation3f ( rotation_mg * ((-1) * model_reference_point)) * rotation_mg;

          Eigen::Vector3f model_point_transformed = transform_mg * model_point;
          float angle = atan2f ( -model_point_transformed(2), model_point_transformed(1));
          if (sin (angle) * model_point_transformed(2) < 0.0f)
            angle *= (-1);
          p (4) = -angle;
        }
        else
        {
          PCL16_ERROR ("[pcl16::%s::computeFeature] Computing pair feature vector between points %zu and %zu went wrong.\n", getClassName ().c_str (), i, j);
          p.setConstant (std::numeric_limits<float>::quiet_NaN ());
          output.is_dense = false;
        }
      }
      // Do not calculate the feature for identity pairs (i, i) as they are not used
      // in the following computations
      else
      {
        p.setConstant (std::numeric_limits<float>::quiet_NaN ());
        output.is_dense = false;
      }

      output.points.row (index_i*input_->points.size () + j) = p;
    }
  }
}


#define PCL16_INSTANTIATE_PPFEstimation(T,NT,OutT) template class PCL16_EXPORTS pcl16::PPFEstimation<T,NT,OutT>;


#endif // PCL16_FEATURES_IMPL_PPF_H_