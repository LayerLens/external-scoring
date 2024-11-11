import numpy as np
[]

def is_floats(x) -> bool:
    """Helper function to check float values for comparison"""
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    """Custom assertion function that handles float comparisons"""
    # Special handling for booleans
    if isinstance(out, bool) or isinstance(exp, bool):
        assert out == exp, f"out: {out}, exp: {exp}"
        return
        
    # Float comparison setup
    if atol == 0 and is_floats(exp):
        atol = 1e-6
    
    # Handle set conversion for sequences
    if isinstance(out, (list, tuple)) and isinstance(exp, (list, tuple)):
        out = set(out)
        exp = set(exp)
    
    # Do the actual comparison
    if out != exp and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert out == exp, f"out: {out}, exp: {exp}"

# Test data
inputs = [['aab_cbbbc'], ['aab_Abbbc'], ['Aaab_abbbc'], ['a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z'], ['abc_def_ghi_jkl_mno_pqr_stu_vwx_yz'], ['_'], ['_abc'], ['abc_'], ['abc_def_ghi_'], ['A__B_ccC_dDd_eE_fFF_g_hhH_iJj'], ['a'], ['abc_DEF_ghi'], ['abc'], ['abc_def_'], ['_abc_def'], ['_abc_def_'], ['a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_'], ['_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yz'], ['ab_abc_def_c_'], ['_abc_deaf'], ['abc_def_ghi_jkl_mno_pqr_stu_vwxyz'], ['abdc_def_ghi_jkl_mno_pqr_stuu_vwx_yz'], ['A__B_cc_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yzC_dDd_eE_fFF_g_hhH_iJj'], ['abdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['_abcabc_d_ghi_jkl_mno_pqr_stu_vwx_yz'], ['abdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno__pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno__pqr_stu_vwx_yz_mno_pqrabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz_stuu_vwx_yzstuu_vwx_yz'], ['_abcabc_def_ghi_jkl_mno_pqr_stu_vwxq_yz'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pqr_stuu_vwx_yz'], ['wJz'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yztuu_vwx_yz'], ['abc_def_ghiabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abc_def_ghie_'], ['abc_def_ghi_jkl_mno_pqr_stu_vabc_def_ghie_wxyz'], ['aba_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_abc_def_ghi_jkl_mno_pqr_stu_vwxyzc_def_'], ['_abcabc_def_ghi_jkl_mno_pqr_stu_vwxq_yabdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yztuu_vwx_yzz'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_afbc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yzabc_def_z'], ['PfGhQdq'], ['c'], ['ab_abc_A__B_ccC_dDd_eE_fFF_g_hhH_iJjdef_c_'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc_defi_jkl_abcabmno_pqr_stuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abdc_def_ghi_jkl_abcabc_def_ghi__jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc__def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pq_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno__pqr_stu_vwx_yz_mno_pqrabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz_stuu_vwx_yzstuu_vwx_yz_yyz_mno_pqr_stuu_vwx_yz'], ['A__B_cc_abcabc_def_ghi_jk_l_mno_pqr_stu_vwx_yzC_dDd_eE_fFF_g_hhH_iJj'], ['ac_'], ['abc_DEF_ghia'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno__pqr_stu_vwx_yz_mno_pqrabdc_def_xghi_jkl_abcabc_def_ghabc_def_ghi_jkl_mno_pqr_stu_vwxyztuu_vwx_yz_stuu_vwx_yzstuu_vwx_yz_yyz_mno_pqr_stuu_vwx_yz'], ['cc'], ['_abcabc_d_ghi_jkl_mno_pqr_stu_vmwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEaba_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_abc_def_ghi_jkl_mno_pqr_stu_vwxyzc_def_F_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abc_d_abcabc_def_ghi_jkl_mno_pqr_stu_vwxq_yabdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yztuu_vwx_yzzef_ghi_'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_abc_defi_jkl_abcbabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yztuu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc_defi_jkl_abcaxbmno_pqr_stuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['_abcabc_def_ghi_jkl_mnao_pqr_stu_vwx_yz'], ['no_pqr_stuu_vwx_yzz'], ['abc_def_ghi_jkl_mnoc_pqr_stu_vabc_def_ghie_wxyz'], ['_ab_abc_defc_def_'], ['a_b_c_d_e_f_g_hf_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z'], ['abc_DEF_ghDia'], ['L'], ['abdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_afbc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yzabc_def_qz'], ['abc_def_ghi_jkl_mno_pqr_stmu_vwxyz'], ['_abcabc_def_ghi_jkl_mno_pqr_stmu_vwxyz_deaf'], ['A__B_cc_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yzC_dDd_eE_fFF_g_hhH_iJLj'], ['_abcabc_def_ghi_jkl_mno_pqr_stu_vwxq_yabdc_def_gh_abc_defi_jkl_abcabmino_pqr_sabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yztuu_vwx_yzz'], ['no__abc_deafpqr_stuu_vwx_LPfGhQdqyzz'], ['_aabc'], ['abc_defabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc_defi_jkl_abcabmno_pqr_stuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['A__B_cc_abcabc_def_ghi__jkl_mno_pqr_stu_vwx_yzC_dDd_eE_fFF_g_hhH_iJj'], ['PfGhQQdq'], ['abc_DEF_PfGhQdqghDia'], ['abc_def_ghiabdc_def_gh_abc_defi_ijkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abc_def__ghi_jkl_mnoc_pqr_stu_vabc_def_ghie_wxyz'], ['aabc'], ['ano_pqr_stuu_vwx_yzzbc_def_ghie_'], ['PfGhQQdq_abcabc_d_ghi_jkl_mno_pqr_stu_vmwx_yz'], ['abc_DEF_PfGhQdqghQDia'], ['abc_def_ghai_'], ['abdc_def_ghi_pqr_stuu_vwx_yz'], ['abc_defabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc_defi_jkl_abcabmno_pqr_stabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yzuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['abc_def_ghiabdc_def_gh_abc_defi_ijkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_spqr_stuu_vwx_yz'], ['abdc_def_ghi_jkl_abcabc_def_ghi__jkl_mno_pqr_ustu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['_abPfGhQQdqcabc_def_ghi_jkl_mno_pqr_stmu_vwxyz_deaf'], ['_ab_abc_defc_defabdc_def_ghi_jkl_abcabc_def_ghi_jkl_mno__pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abdbc_def_ghi_jkl_abcabc_def_ghi__jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['abc_def_ghi_jk_l_mno_spqr_stu_vwx_yz'], ['abc_defabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc__defi_jkl_abcabmno_pqr_stuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['A__B_cc_aghi_jk_l_mno_pqr_stu_vwx_yzC_da_b_tc_d_e_f_g_hf_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_zDd_eE_fFF_g_hhH_iJj'], ['vabc_def_ghi_jkl_mno_pqr_stu_vwx_yz'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mx_yz'], ['abc_def_abdc_def_gh_abc_defi_jkl_abcabmno_pqr_sabdc_def_gh_afbc_defi_jkl_abcabc_def_ghi_jkl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yzabc_def_qzghiabdc_def_gh_abc_defi_ijkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_spqr_stuu_vwx_yz'], ['abdc_def_ghi_jkl_mno_p_abc_def_qr_stuuPfGhQQdq_abcabc_d_ghi_jkl_mno_pqr_stu_vmwx_yz_vwx_yz'], ['_abcabc_d_ghi_jkl_mno_abc_def_ghai_pqr_stu_vwx_yz'], ['yz'], ['abdc_def_ghi_jkl_mno_p_abc_abc_defabdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEabcF_ghiqr_stabdc_def_gh_abc__defi_jkl_abcabmno_pqr_stuu_vwx_yzu_vwx_yyz_mno_pqr_stuu_vwx_yzdef_qr_stuuPfGhQQdq_abcabc_d_ghi_jkl_mno_pqr_stu_vmwx_yz_vwx_yz'], ['abdc_Edef_gh_abc_defi_jkl_abcabc__def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yyz_mno_pqr_stuu_vwx_yz'], ['bc_def_'], ['abc_def_dghi_'], ['abdcc_def_ghi_jkl_abcabc_def_ghi__jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz'], ['_acbc_def_'], ['abdc_Edef_gh_abc_defi_jkl_abcabc__def_ghi_jkl_yz'], ['habcghia'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_jkl_mno_pabc_DEF_ghiqr_stu_vwx_yeyz_mx_yz'], ['_abcabc_d_ghi_jkl_mno_pqr_stu_x_yz'], ['a_b_c_d_e_f_g_h_i_j_aba_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_abc_def_ghi_jkl_mno_pqr_stu_vwxyzc_def_m_n_o_p_q_r_s_t_u_v_w_x_y_z'], ['abdc_def_gh_abc_bdefi_jkl_abcabmno_pq_yz'], ['an_pqr_stuu_vwx_yzzbc_def_ghie_'], ['PfGhQdqL'], ['_abcabc_d_ghi_jkl_mno_pqr_stu_z'], ['abc_DEF_PhQdqghQDia'], ['abdc_def_gh_abc_defi_jkl_abcabc_def_ghi_abdbc_def_ghi_jkl_abcabc_def_ghi__jkl_mno_pqr_stu_vwx_yz_mno_pqr_stuu_vwx_yzl_mno_pa_abcbc_DEF_ghiqr_stu_vwx_yz_mno_pqr_stuu_vwx_yz']]
results = [True, False, False, True, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False]

def ll_run_tests(response_data):
    """
    Main test function for code evaluation.
    Args:
        response_data: Dict containing response code
    Returns:
        bool: True if all test cases pass
    """
    try:
        # Initialize test environment
        global_namespace = {
            'np': np,
            'assertion': assertion,
            'is_floats': is_floats,
            'inputs': inputs,
            'results': results
        }
        
        # Execute solution code
        response_code = response_data.get('parsed_result', response_data.get('result', ''))
        exec(response_code, global_namespace)
        
        # Verify function exists
        func_name = "text_lowercase_underscore"
        if func_name not in global_namespace:
            print(f"Function '{func_name}' not found in response")
            return False
        
        # Execute tests
        solution_func = global_namespace[func_name]
        
        # Run input/output tests
        for i, (test_input, expected) in enumerate(zip(inputs, results)):
            try:
                result = solution_func(*test_input)
                assertion(result, expected, 0)
            except AssertionError as e:
                print(f"Test case {i} failed: {str(e)}")
                print(f"Input: {test_input}")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                return False
        
        # Run assertion-based tests if any
        for test_case in ['assert text_lowercase_underscore("aab_cbbbc")==(True)', 'assert text_lowercase_underscore("aab_Abbbc")==(False)', 'assert text_lowercase_underscore("Aaab_abbbc")==(False)']:
            try:
                exec(test_case, global_namespace)
            except AssertionError as e:
                print(f"Assertion test failed: {str(e)}")
                print(f"Test case: {test_case}")
                return False
            
        return True
            
    except Exception as e:
        print(f"Error during test execution: {str(e)}")
        return False
