# $1: number of shots
# $2: dataset (flower/food101)

python main.py --cfg cfg/asso_opt/$2/$2_$1shot_fac.py --work-dir exp/asso_opt/$2/$2_$1shot_fac --func asso_opt_main

#python main.py --cfg jiezy/LaBo/asso_opt/CIFAR10/CIFAR10_1shot_fac.py --work-dir jiezy/LaBo/asso_opt/CIFAR10/CIFAR10_1shot_fac --func asso_opt_main