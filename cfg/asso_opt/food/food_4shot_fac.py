_base_ = 'food_base.py'
n_shots = 4
data_root = 'exp/asso_opt/food/food_4shot_fac'
lr = 1e-4
bs = 64

concept_type = "all_submodular"
concept_select_fn = "submodular"
submodular_weights = [1e7, 1]