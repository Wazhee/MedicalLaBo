_base_ = 'aircraft_base.py'
n_shots = 16
data_root = 'exp/asso_opt/aircraft/aircraft_16shot_fac'
lr = 5e-5
bs = 256

concept_type = "all_submodular"
concept_select_fn = "submodular"
submodular_weights = [1e7, 1]