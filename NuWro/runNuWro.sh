#!/bin/bash

echo "RUNNING SF, Ar, test025l00001w"
SEED=${RANDOM}
NEVTS=1000000
NTESTEVTS=10000000

cd /eos/user/a/amgruber/SWAN_projects/XSec_ROOT/NuWro

mkdir -p test025l00001w
cd test025l00001w

nuwro -i ../params_SF.txt -o ./test025l00001w_Ar_SF_numu_NuWroOut_${SEED}.root  -p  "beam_inputroot=/eos/user/a/amgruber/SWAN_projects/XSec_ROOT/gausFlux025l00001w.root" -p  "beam_inputroot_nue=" -p  "beam_inputroot_nueb=" -p  "beam_inputroot_numu=gausFlux025l00001w" -p  "beam_inputroot_numub=" -p  "beam_inputroot_nutau=" -p  "beam_inputroot_nutaub=" -p  "beam_type=6"  -p  "dyn_coh_cc=1" -p  "dyn_coh_nc=0" -p  "dyn_dis_cc=1" -p  "dyn_dis_nc=0" -p  "dyn_mec_cc=1" -p  "dyn_mec_nc=0" -p  "dyn_qel_cc=1" -p  "dyn_qel_nc=0" -p  "dyn_res_cc=1" -p  "dyn_res_nc=0"  -p "number_of_events=${NEVTS}" -p "number_of_test_events=${NTESTEVTS}" -p "random_seed=${SEED}" -p "target_type = 1" -p "target_type = 0" -p "nucleus_p = 18" -p "nucleus_n = 22"

PrepareNuwro -F /eos/user/a/amgruber/SWAN_projects/XSec_ROOT/gausFlux025l00001w.root,gausFlux025l00001w,14,1.0 test025l00001w_Ar_SF_numu_NuWroOut_${SEED}.root

nuisflat -f GenericFlux -i NUWRO:test025l00001w_Ar_SF_numu_NuWroOut_${SEED}.root -o flat_test025l00001w_Ar_SF_numu_NuWroOut_${SEED}.root
