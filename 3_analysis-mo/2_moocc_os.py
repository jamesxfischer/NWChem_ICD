import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt

outfile = glob.glob('gamma1.0-zeta1.0-E0.07-time.4999.reo')

tag1="# MO Occupations (alpha spin)"
tag2="# MO Occupations (beta spin)"

for ifile in outfile :
	filename=ifile.strip(".nwo")
	f=open(ifile)
	lines=f.readlines()
	f.close()
	datafile = open(filename+'.moa', 'w+')
	for l in lines:
		if (tag1 in l ):
			alpha = l.strip().split()
			val1 = alpha[1:-5]
			for occ in val1 :
				datafile.write(occ +'\t')
			datafile.write('\n')
	datafile.close()
	datafile = open(filename+'.mob', 'w+')
	for l in lines:
        	if (tag2 in l ):
                	alpha = l.strip().split()
                	val1 = alpha[1:-5]
                	for occ in val1 :
                        	datafile.write(occ +'\t')
                	datafile.write('\n')
	datafile.close()
	a=np.loadtxt(filename+'.moa')
	b=np.loadtxt(filename+'.mob')
	c=a+b
	np.savetxt(filename+'.moocc', c , fmt="%f")

occfiles = glob.glob('*.moocc')
for ifile in occfiles :
	filename=ifile.strip(".moocc")
	occf=pd.read_csv(ifile ,header=None,delimiter=' ')
	f=pd.DataFrame(occf)
	f2=f.drop(columns=0)
	f_plot=f2.loc[0:200,9:10]
	f_plot.plot(figsize=(20, 9))
	plt.title(filename)
	plt.savefig(filename+'.png',bbox_inches='tight')
