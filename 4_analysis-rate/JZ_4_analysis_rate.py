#call nw gen function to create .nw files
import os
#os.system('sh step1_zsh.nw_gen')

#generate pbs files
#os.system('sh step2_zsh.nwslm_gen')

#submit nw files with pbs
#os.system('sh step3_zsh.nwslm_submit')
###############################################################
#call step3 dmat gen file to create coefficient matrix
import step4_modifyCmo
import step5_dmat_gen_os_CPC

#call step4 step4_zsh.re_gen
os.system('sh step6_zsh.re_gen')

#generate restart slm
#os.system('sh step7_zsh.reslm_gen')

#submit restart files
#os.sytstem('sh step8_zsh.reslm_submit')