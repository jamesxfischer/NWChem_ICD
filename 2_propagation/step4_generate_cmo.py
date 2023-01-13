################################################################
##JZ 1/12/2023 python3 convert movecs to cmo files 
################################################################

import glob
import os


movecs_files = glob.glob('*.movecs')
x = 0
while x < len(movecs_files):
	filename = movecs_files[x].strip('.movecs')
	movecfile = movecs_files[x]
	datafile = filename+'.cmo'
	command_line = 'python3 mov2asc_py3.py ' + movecfile + ' > ' + datafile
	os.system(command_line)
	x = x+1


