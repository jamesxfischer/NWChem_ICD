################################################################
##JZ 1/12/2023 python3 convert movecs to cmo files 
##   1/12/2023 used move2asc.py instead
##	       add in functionality to grab both alpha and beta 
################################################################

import glob
import os

asc_files = glob.glob('*.asc')
for filename in asc_files:
	cmofile = filename.strip('.asc')
	cmofile = cmofile + '.cmo'
	tmpname = 'temp'
	fp = open(tmpname, 'w')
	with open(filename, 'r') as f:
		lines = f.readlines()
#		print(int(lines[12]))
		nbf_ao = int(lines[12])
		lines = lines[14:len(lines)]
		z = 0
		for line in lines:
			testline = line[4:len(line)].strip('\n')
			#print(testline)
			testline = testline.split('   ')
			for num in testline:
				newline = num.strip().rjust(24, ' ')
			#	print(newline+'\n')
				fp.write(newline+'\n')
	fp.close()
	fp = open(tmpname, 'r')
	alpha = open(cmofile  + '_alpha', 'w')
	beta = open(cmofile + '_beta', 'w')
	lines = fp.readlines()
	alpha_lines = lines[int(nbf_ao*2):int(len(lines)//2)]
	beta_lines = lines[int(len(lines)//2+nbf_ao*2):len(lines)]
	for line in alpha_lines:
		alpha.write(line)
	for line in beta_lines:
		beta.write(line)
	fp.close()
	alpha.close()
	beta.close()
	os.remove(tmpname)
	os.remove(filename)
	
