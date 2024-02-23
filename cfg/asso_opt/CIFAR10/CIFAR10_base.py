_base_ = '../base.py'
# dataset 
proj_name = "CIFAR10"
concept_root = 'datasets/CIFAR10/concepts/'
img_split_path = 'datasets/CIFAR10/splits'
img_path = 'datasets/CIFAR10/images'

concept_type = "all"

img_ext = ''
raw_sen_path = concept_root + 'concepts_raw.npy'
concept2cls_path = concept_root + 'concept2cls.npy'
cls_name_path = concept_root + 'cls_names.npy'
num_cls = 10

## data loader
bs = 32
on_gpu = True

# concept select
num_concept = num_cls * 50

# weight matrix fitting
lr = 5e-6
max_epochs = 15000

# weight matrix
use_rand_init = False
init_val = 1.
asso_act = 'softmax'
use_l1_loss = False
use_div_loss = False
lambda_l1 = 0.01
lambda_div = 0.005

# CLIP Backbone
clip_model = 'ViT-L/14'