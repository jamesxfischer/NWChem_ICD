################################################################
##JZ 1/12/2023 wrapper to call all .py files
################################################################
import os
import datetime
ct = datetime.datetime.now()
ts = str(ct)

#call nw gen function to create .nw files
print(ts + ' Start -- 1_charge.py')
os.system('python3 1_charge.py')
print(ts + ' Done -- 1_charge.py')

#generate slm files
print(ts + ' Start -- 1_charge_plot.py')
os.system('python3 1_charge_plot.py')
print(ts + ' Done -- 1_charge_plot.py')

#submit nw files with slm
print(ts + ' Start -- 2_moocc_os.py')
os.system('python3 2_moocc_os.py')
print(ts + ' Start -- 2_moocc_os.py')
