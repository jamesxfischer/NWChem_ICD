################################################################
JZ 1/10/2023 python3 script to call other python and slm files 
	     initialize to generate .db .movec files
JZ 1/12/2023 add in comment lines to show progress
################################################################
import os
import datetime
ct = datetime.datetime.now()
ts = str(ct)

#call nw gen function to create .nw files
print(ts + ' Start -- generate nw files')
os.system('sh step1_zsh.nw_gen')
print(ts + ' Done -- generate nw files')

#generate slm files
print(ts + ' Start -- generate slm files')
os.system('sh step2_zsh.nwslm_gen')
print(ts + ' Done -- generate slm files')

#submit nw files with slm
print(ts + ' Start -- submit slm files')
os.system('sh step3_zsh.nwslm_submit')
print(ts + ' Start -- submit slm files')
