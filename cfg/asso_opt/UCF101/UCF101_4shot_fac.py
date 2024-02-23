_base_ = 'UCF101_base.py'
n_shots = 4
data_root = 'exp/asso_opt/UCF101/UCF101_4shot_fac'
lr = 1e-5
bs = 32

concept_type = "all_submodular"
concept_select_fn = "submodular"
submodular_weights = [1e7, 100]