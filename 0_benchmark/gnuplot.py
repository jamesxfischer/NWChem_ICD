import numpy as np
import pandas as pd
import glob
import os
from subprocess import Popen

#cmd = ['gnuplot','-e', "input_fname='x_omega0.5_Gau0.0_gamma2_zeta1_E0.0_c10w1.charge' ;output_fname='data4.png'", "plot.plt"]
#Popen(cmd)

############ Read files ##############
outfile = glob.glob("*_Ar")

i=0
while i < len(outfile):
  fname=str(outfile[i].strip("_Ar"))
  print(fname)
  cmd = ['gnuplot','-e', "input_fname="+"'"+fname+ "_Ar"+"'"+" ;output_fname='"+fname+".png'", "gnuplot.tpl"]
  Popen(cmd)
  i=i+1

