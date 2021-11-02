# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import logging

import onnx.backend.test

from tests.test_onnx.utils.onnx_backend import OpenVinoTestBackend

from tests import (BACKEND_NAME,
                   xfail_issue_33488,
                   xfail_issue_33512,
                   xfail_issue_33535,
                   xfail_issue_33538,
                   xfail_issue_33581,
                   xfail_issue_33589,
                   xfail_issue_33593,
                   xfail_issue_33595,
                   xfail_issue_33596,
                   xfail_issue_33606,
                   xfail_issue_33633,
                   xfail_issue_33651,
                   xfail_issue_38091,
                   xfail_issue_38699,
                   xfail_issue_38701,
                   xfail_issue_38706,
                   xfail_issue_38708,
                   xfail_issue_38713,
                   xfail_issue_38722,
                   xfail_issue_38723,
                   xfail_issue_38724,
                   xfail_issue_38732,
                   xfail_issue_38734,
                   xfail_issue_38735,
                   xfail_issue_39656,
                   xfail_issue_39658,
                   xfail_issue_39659,
                   xfail_issue_39662,
                   xfail_issue_43742,
                   xfail_issue_44848,
                   xfail_issue_44851,
                   xfail_issue_44854,
                   xfail_issue_44858,
                   xfail_issue_44956,
                   xfail_issue_44957,
                   xfail_issue_44958,
                   xfail_issue_44965,
                   xfail_issue_44968,
                   xfail_issue_44976,
                   xfail_issue_45180,
                   xfail_issue_45344,
                   xfail_issue_46762,
                   xfail_issue_47323,
                   xfail_issue_47337,
                   xfail_issue_48052,
                   xfail_issue_49207,
                   xfail_issue_49750,
                   xfail_issue_49752,
                   xfail_issue_49753,
                   xfail_issue_49754,
                   xfail_issue_52463,
                   xfail_issue_55760)


def expect_fail(test_case_path, xfail):  # type: (str) -> None
    """Mark the test as expected to fail."""
    module_name, test_name = test_case_path.split(".")
    module = globals().get(module_name)
    if hasattr(module, test_name):
        xfail(getattr(module, test_name))
    else:
        logging.getLogger().warning("Could not mark test as XFAIL, not found: %s", test_case_path)


OpenVinoTestBackend.backend_name = BACKEND_NAME

# This is a pytest magic variable to load extra plugins
# Uncomment the line below to enable the ONNX compatibility report
# pytest_plugins = "onnx.backend.test.report",

# import all test cases at global scope to make them visible to python.unittest
backend_test = onnx.backend.test.BackendTest(OpenVinoTestBackend, __name__)

skip_tests_general = [
    # Big model tests (see test_zoo_models.py):
    "test_bvlc_alexnet",
    "test_densenet121",
    "test_inception_v1",
    "test_inception_v2",
    "test_resnet50",
    "test_shufflenet",
    "test_squeezenet",
    "test_vgg19",
    "test_zfnet512",
]

for test in skip_tests_general:
    backend_test.exclude(test)

# NOTE: ALL backend_test.exclude CALLS MUST BE PERFORMED BEFORE THE CALL TO globals().update

OnnxBackendNodeModelTest = None
OnnxBackendSimpleModelTest = None
OnnxBackendPyTorchOperatorModelTest = None
OnnxBackendPyTorchConvertedModelTest = None
globals().update(backend_test.enable_report().test_cases)

tests_expected_to_fail = [
    (xfail_issue_49207,
     "OnnxBackendNodeModelTest.test_rnn_seq_length_cpu",
     "OnnxBackendNodeModelTest.test_simple_rnn_defaults_cpu",
     "OnnxBackendNodeModelTest.test_simple_rnn_with_initial_bias_cpu",
     "OnnxBackendNodeModelTest.test_gru_defaults_cpu",
     "OnnxBackendNodeModelTest.test_gru_seq_length_cpu",
     "OnnxBackendNodeModelTest.test_gru_with_initial_bias_cpu",
     "OnnxBackendNodeModelTest.test_lstm_defaults_cpu",
     "OnnxBackendNodeModelTest.test_lstm_with_initial_bias_cpu",
     "OnnxBackendNodeModelTest.test_lstm_with_peepholes_cpu"),
    (xfail_issue_49752,
     "OnnxBackendNodeModelTest.test_constant_pad_cpu",
     "OnnxBackendNodeModelTest.test_edge_pad_cpu",
     "OnnxBackendNodeModelTest.test_reflect_pad_cpu"),
    (xfail_issue_39656,
     "OnnxBackendNodeModelTest.test_reshape_extended_dims_cpu",
     "OnnxBackendNodeModelTest.test_reshape_negative_dim_cpu",
     "OnnxBackendNodeModelTest.test_reshape_one_dim_cpu",
     "OnnxBackendNodeModelTest.test_reshape_reduced_dims_cpu",
     "OnnxBackendNodeModelTest.test_reshape_negative_extended_dims_cpu",
     "OnnxBackendNodeModelTest.test_reshape_reordered_all_dims_cpu",
     "OnnxBackendNodeModelTest.test_reshape_reordered_last_dims_cpu",
     "OnnxBackendNodeModelTest.test_reshape_zero_and_negative_dim_cpu",
     "OnnxBackendNodeModelTest.test_reshape_zero_dim_cpu"),
    (xfail_issue_39658,
     "OnnxBackendNodeModelTest.test_tile_cpu",
     "OnnxBackendNodeModelTest.test_tile_precomputed_cpu"),
    (xfail_issue_39659,
     "OnnxBackendNodeModelTest.test_constantofshape_float_ones_cpu",
     "OnnxBackendNodeModelTest.test_constantofshape_int_zeros_cpu",
     "OnnxBackendNodeModelTest.test_constantofshape_int_shape_zero_cpu"),
    (xfail_issue_45344,
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_center_point_box_format_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_flipped_coordinates_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_identical_boxes_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_limit_output_size_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_single_box_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_suppress_by_IOU_and_scores_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_suppress_by_IOU_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_two_batches_cpu",
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_two_classes_cpu"),
    (xfail_issue_39662,
     "OnnxBackendNodeModelTest.test_nonmaxsuppression_two_classes_cpu",
     "OnnxBackendNodeModelTest.test_scatter_elements_with_negative_indices_cpu",
     "OnnxBackendNodeModelTest.test_gather_negative_indices_cpu"),
    (xfail_issue_49753,
     "OnnxBackendNodeModelTest.test_slice_default_axes_cpu"),
    (xfail_issue_49754,
     "OnnxBackendNodeModelTest.test_top_k_cpu",
     "OnnxBackendNodeModelTest.test_top_k_negative_axis_cpu",
     "OnnxBackendNodeModelTest.test_top_k_smallest_cpu"),
    (xfail_issue_33633,
     "OnnxBackendNodeModelTest.test_maxpool_2d_dilations_cpu"),
    (xfail_issue_46762,
     "OnnxBackendNodeModelTest.test_min_uint8_cpu",
     "OnnxBackendNodeModelTest.test_min_uint16_cpu",
     "OnnxBackendNodeModelTest.test_min_uint32_cpu",
     "OnnxBackendNodeModelTest.test_min_uint64_cpu"),
    (xfail_issue_55760,
     "OnnxBackendNodeModelTest.test_argmax_negative_axis_keepdims_example_select_last_index_cpu",
     "OnnxBackendNodeModelTest.test_argmin_negative_axis_keepdims_example_select_last_index_cpu",
     "OnnxBackendNodeModelTest.test_argmax_negative_axis_keepdims_random_select_last_index_cpu",
     "OnnxBackendNodeModelTest.test_argmin_negative_axis_keepdims_random_select_last_index_cpu"),
    (xfail_issue_38091,
     "OnnxBackendNodeModelTest.test_gather_negative_indices_cpu"),
    (xfail_issue_52463,
     "OnnxBackendPyTorchOperatorModelTest.test_operator_add_size1_singleton_broadcast_cpu"),
    (xfail_issue_47323,
     "OnnxBackendPyTorchOperatorModelTest.test_operator_add_broadcast_cpu",
     "OnnxBackendPyTorchOperatorModelTest.test_operator_addconstant_cpu",
     "OnnxBackendPyTorchOperatorModelTest.test_operator_add_size1_right_broadcast_cpu"),
    (xfail_issue_38699,
     "OnnxBackendSimpleModelTest.test_gradient_of_add_and_mul_cpu",
     "OnnxBackendSimpleModelTest.test_gradient_of_add_cpu"),
    (xfail_issue_33596,
     "OnnxBackendSimpleModelTest.test_sequence_model5_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model7_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model1_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model3_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model6_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model8_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model4_cpu",
     "OnnxBackendSimpleModelTest.test_sequence_model2_cpu"),
    (xfail_issue_38701,
     "OnnxBackendSimpleModelTest.test_strnorm_model_monday_casesensintive_nochangecase_cpu",
     "OnnxBackendSimpleModelTest.test_strnorm_model_nostopwords_nochangecase_cpu",
     "OnnxBackendSimpleModelTest.test_strnorm_model_monday_empty_output_cpu",
     "OnnxBackendSimpleModelTest.test_strnorm_model_monday_insensintive_upper_twodim_cpu",
     "OnnxBackendSimpleModelTest.test_strnorm_model_monday_casesensintive_lower_cpu",
     "OnnxBackendSimpleModelTest.test_strnorm_model_monday_casesensintive_upper_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_nostopwords_nochangecase_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_export_monday_casesensintive_nochangecase_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_export_monday_insensintive_upper_twodim_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_export_monday_casesensintive_lower_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_export_monday_empty_output_cpu",
     "OnnxBackendNodeModelTest.test_strnormalizer_export_monday_casesensintive_upper_cpu",
     "OnnxBackendNodeModelTest.test_cast_STRING_to_FLOAT_cpu",
     "OnnxBackendNodeModelTest.test_cast_FLOAT_to_STRING_cpu"),
    (xfail_issue_33595,
     "OnnxBackendNodeModelTest.test_unique_not_sorted_without_axis_cpu",
     "OnnxBackendNodeModelTest.test_unique_sorted_with_negative_axis_cpu",
     "OnnxBackendNodeModelTest.test_unique_sorted_with_axis_cpu",
     "OnnxBackendNodeModelTest.test_unique_sorted_with_axis_3d_cpu",
     "OnnxBackendNodeModelTest.test_unique_sorted_without_axis_cpu"),
    (xfail_issue_33651,
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_batch_onlybigrams_skip5_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_onlybigrams_levelempty_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_batch_onlybigrams_skip0_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_uniandbigrams_skip5_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_only_bigrams_skip0_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_batch_uniandbigrams_skip5_cpu",
     "OnnxBackendNodeModelTest.test_tfidfvectorizer_tf_onlybigrams_skip5_cpu"),
    (xfail_issue_38706,
     "OnnxBackendNodeModelTest.test_split_zero_size_splits_cpu"),
    (xfail_issue_38708,
     "OnnxBackendNodeModelTest.test_slice_default_steps_cpu",
     "OnnxBackendNodeModelTest.test_slice_negative_axes_cpu",
     "OnnxBackendNodeModelTest.test_slice_neg_steps_cpu",
     "OnnxBackendNodeModelTest.test_slice_neg_cpu",
     "OnnxBackendNodeModelTest.test_slice_cpu",
     "OnnxBackendNodeModelTest.test_slice_end_out_of_bounds_cpu",
     "OnnxBackendNodeModelTest.test_slice_start_out_of_bounds_cpu"),
    (xfail_issue_33538,
     "OnnxBackendNodeModelTest.test_scan_sum_cpu",
     "OnnxBackendNodeModelTest.test_scan9_sum_cpu"),
    (xfail_issue_49750,
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_linear_align_corners_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_cubic_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_cubic_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_cubic_align_corners_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_nearest_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_cubic_asymmetric_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_cubic_A_n0p5_exclude_outside_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_linear_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_cubic_align_corners_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_linear_align_corners_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_scales_cubic_A_n0p5_exclude_outside_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_nearest_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_scales_linear_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_sizes_cubic_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_sizes_nearest_round_prefer_ceil_asymmetric_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_sizes_nearest_floor_align_corners_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_sizes_nearest_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_sizes_nearest_ceil_half_pixel_cpu",
     "OnnxBackendNodeModelTest.test_resize_upsample_sizes_cubic_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_sizes_linear_pytorch_half_pixel_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_sizes_nearest_cpu",
     "OnnxBackendNodeModelTest.test_resize_downsample_sizes_nearest_tf_half_pixel_for_nn_cpu"),
    (xfail_issue_33581,
     "OnnxBackendNodeModelTest.test_gather_elements_negative_indices_cpu"),
    (xfail_issue_38713,
     "OnnxBackendNodeModelTest.test_momentum_cpu",
     "OnnxBackendNodeModelTest.test_nesterov_momentum_cpu",
     "OnnxBackendNodeModelTest.test_momentum_multiple_cpu"),
    (xfail_issue_47337,
     "OnnxBackendNodeModelTest.test_onehot_without_axis_cpu",
     "OnnxBackendNodeModelTest.test_onehot_with_negative_axis_cpu",
     "OnnxBackendNodeModelTest.test_onehot_with_axis_cpu",
     "OnnxBackendNodeModelTest.test_onehot_negative_indices_cpu"),
    (xfail_issue_33488,
     "OnnxBackendNodeModelTest.test_maxunpool_export_with_output_shape_cpu",
     "OnnxBackendNodeModelTest.test_maxunpool_export_without_output_shape_cpu"),
    (xfail_issue_33589,
     "OnnxBackendNodeModelTest.test_isnan_cpu",
     "OnnxBackendNodeModelTest.test_isinf_positive_cpu",
     "OnnxBackendNodeModelTest.test_isinf_negative_cpu",
     "OnnxBackendNodeModelTest.test_isinf_cpu"),
    (xfail_issue_33535,
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_min_adjusted_cpu",
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_cpu",
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_max_adjusted_cpu"),
    (xfail_issue_38722,
     "OnnxBackendNodeModelTest.test_matmulinteger_cpu",
     "OnnxBackendNodeModelTest.test_qlinearmatmul_2D_cpu",
     "OnnxBackendNodeModelTest.test_qlinearmatmul_3D_cpu"),
    (xfail_issue_38723,
     "OnnxBackendNodeModelTest.test_qlinearconv_cpu"),
    (xfail_issue_38724,
     "OnnxBackendNodeModelTest.test_resize_tf_crop_and_resize_cpu"),
    (xfail_issue_33512,
     "OnnxBackendNodeModelTest.test_einsum_transpose_cpu",
     "OnnxBackendNodeModelTest.test_einsum_batch_diagonal_cpu",
     "OnnxBackendNodeModelTest.test_einsum_batch_matmul_cpu",
     "OnnxBackendNodeModelTest.test_einsum_sum_cpu",
     "OnnxBackendNodeModelTest.test_einsum_inner_prod_cpu"),
    (xfail_issue_33606,
     "OnnxBackendNodeModelTest.test_det_2d_cpu",
     "OnnxBackendNodeModelTest.test_det_nd_cpu"),
    (xfail_issue_38732,
     "OnnxBackendNodeModelTest.test_convinteger_with_padding_cpu",
     "OnnxBackendNodeModelTest.test_basic_convinteger_cpu"),
    (xfail_issue_38734,
     "OnnxBackendNodeModelTest.test_adam_multiple_cpu",
     "OnnxBackendNodeModelTest.test_adam_cpu"),
    (xfail_issue_38735,
     "OnnxBackendNodeModelTest.test_adagrad_multiple_cpu",
     "OnnxBackendNodeModelTest.test_adagrad_cpu"),
    (xfail_issue_48052,
     "OnnxBackendNodeModelTest.test_training_dropout_cpu",
     "OnnxBackendNodeModelTest.test_training_dropout_mask_cpu",
     "OnnxBackendNodeModelTest.test_training_dropout_default_cpu",
     "OnnxBackendNodeModelTest.test_training_dropout_zero_ratio_cpu",
     "OnnxBackendNodeModelTest.test_training_dropout_default_mask_cpu",
     "OnnxBackendNodeModelTest.test_training_dropout_zero_ratio_mask_cpu"),
    (xfail_issue_45180,
     "OnnxBackendNodeModelTest.test_reduce_sum_do_not_keepdims_example_cpu",
     "OnnxBackendNodeModelTest.test_reduce_sum_do_not_keepdims_random_cpu",
     "OnnxBackendNodeModelTest.test_reduce_sum_keepdims_example_cpu",
     "OnnxBackendNodeModelTest.test_reduce_sum_keepdims_random_cpu",
     "OnnxBackendNodeModelTest.test_reduce_sum_negative_axes_keepdims_example_cpu"),
    (xfail_issue_43742,
     "OnnxBackendNodeModelTest.test_if_cpu",
     "OnnxBackendNodeModelTest.test_if_seq_cpu"),
    (xfail_issue_44848,
     "OnnxBackendNodeModelTest.test_range_float_type_positive_delta_cpu",
     "OnnxBackendNodeModelTest.test_range_int32_type_negative_delta_cpu",),
    (xfail_issue_44851,
     "OnnxBackendNodeModelTest.test_expand_dim_changed_cpu",
     "OnnxBackendNodeModelTest.test_expand_dim_unchanged_cpu",
     "OnnxBackendSimpleModelTest.test_expand_shape_model1_cpu",
     "OnnxBackendSimpleModelTest.test_expand_shape_model2_cpu",
     "OnnxBackendSimpleModelTest.test_expand_shape_model3_cpu",
     "OnnxBackendSimpleModelTest.test_expand_shape_model4_cpu",),
    (xfail_issue_44854,
     "OnnxBackendNodeModelTest.test_split_variable_parts_1d_cpu",
     "OnnxBackendNodeModelTest.test_split_variable_parts_2d_cpu",
     "OnnxBackendNodeModelTest.test_split_variable_parts_default_axis_cpu",),
    (xfail_issue_44858,
     "OnnxBackendNodeModelTest.test_unsqueeze_axis_0_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_axis_1_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_axis_2_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_negative_axes_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_three_axes_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_two_axes_cpu",
     "OnnxBackendNodeModelTest.test_unsqueeze_unsorted_axes_cpu",),
    (xfail_issue_44956,
     "OnnxBackendNodeModelTest.test_loop11_cpu",
     "OnnxBackendNodeModelTest.test_range_int32_type_negative_delta_expanded_cpu",
     "OnnxBackendNodeModelTest.test_range_float_type_positive_delta_expanded_cpu"),
    (xfail_issue_44957,
     "OnnxBackendNodeModelTest.test_compress_0_cpu",
     "OnnxBackendNodeModelTest.test_compress_1_cpu",
     "OnnxBackendNodeModelTest.test_compress_default_axis_cpu",
     "OnnxBackendNodeModelTest.test_compress_negative_axis_cpu",
     "OnnxBackendNodeModelTest.test_nonzero_example_cpu"),
    (xfail_issue_44958,
     "OnnxBackendNodeModelTest.test_upsample_nearest_cpu"),
    (xfail_issue_44965,
     "OnnxBackendNodeModelTest.test_loop13_seq_cpu",
     "OnnxBackendNodeModelTest.test_sequence_insert_at_back_cpu",
     "OnnxBackendNodeModelTest.test_sequence_insert_at_front_cpu",),
    (xfail_issue_44968,
     "OnnxBackendNodeModelTest.test_squeeze_cpu",
     "OnnxBackendNodeModelTest.test_squeeze_negative_axes_cpu",),
    (xfail_issue_44976,
     "OnnxBackendNodeModelTest.test_quantizelinear_axis_cpu",
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_min_adjusted_expanded_cpu",
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_expanded_cpu",
     "OnnxBackendNodeModelTest.test_dynamicquantizelinear_max_adjusted_expanded_cpu",
     "OnnxBackendNodeModelTest.test_quantizelinear_cpu"),
    (xfail_issue_33593,
     "OnnxBackendNodeModelTest.test_maxpool_with_argmax_2d_precomputed_strides_cpu",
     "OnnxBackendNodeModelTest.test_maxpool_with_argmax_2d_precomputed_pads_cpu",)
]

for test_group in tests_expected_to_fail:
    for test_case in test_group[1:]:
        expect_fail("{}".format(test_case), test_group[0])