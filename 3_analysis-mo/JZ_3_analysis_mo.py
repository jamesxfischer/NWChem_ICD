################################################################
JZ 1/12/2023 wrapper to call all .py files
################################################################
import os
import datetime
ct = datetime.datetime.now()
ts = str(ct)

#call nw gen function to create .nw files
print(ts + ' Start -- generate nw files')
os.system('python3 1_charge.py')
print(ts + ' Done -- generate nw files')

#generate slm files
print(ts + ' Start -- generate slm files')
os.system('python3 1_charge_plot.py')
print(ts + ' Done -- generate slm files')

#submit nw files with slm
print(ts + ' Start -- submit slm files')
os.system('python3 1_NWrtparse_NO_header.py')
print(ts + ' Start -- submit slm files')

#submit nw files with slm
print(ts + ' Start -- submit slm files')
os.system('python3 2_moocc_os.py')
print(ts + ' Start -- submit slm files')
