################################################################
##JZ 1/10/2023 python3 script to call other python and slm files 
##	     update .movecs
##            generate .Cmo files
##             restart
################################################################
import os
import datetime
ct = datetime.datetime.now()
ts = str(ct)

#convert all movecs files to cmo files call step4.....py
print(ts + ' Start -- generate cmo')
os.system('python3 step4_generate_cmo.py')
print(ts + ' Done -- generate cmo')

#call step5 compute new rt_restart file
print(ts + ' Start -- compute CPC')
os.system('python3 step5_dmat_gen_os_CPC.py')
print(ts + ' Done -- compute CPC')

#call step6 step6_zsh.re_gen
print(ts + ' Start -- generate .re files')
os.system('sh step6_zsh.re_gen')
print(ts + ' Done -- generate .re files')

#generate restart slm
print(ts + ' Start -- generate re.slm files')
os.system('sh step7_zsh.reslm_gen')
print(ts + ' Done -- generate re.slm files')

#submit restart files
print(ts + ' Start -- submite re.slm files')
os.system('sh step8_zsh.reslm_submit')
print(ts + ' Done -- submit re.slm files')