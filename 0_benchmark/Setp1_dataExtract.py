import glob
import os
import numpy as np
#from nw_rtsparse import read_input
#from Load_Files import atom_list

Dimer1="Ar"
#Dimer2="Ar2"
target=" "
extract="charge"
spin="total"
outputs=glob.glob("*.nwo")

i=0
while i < len(outputs):
  print(outputs[i])
  filename=outputs[i].strip(".nwo") #.split(".")
  print(filename)
  output_Dimer1=filename+"_"+Dimer1
#  output_Dimer2=filename+"_"+Dimer2
#  output_filename = "ETH." + str(pair)+ ".time." + str(time_step)
  os.system("python3 nw_rtparse.py  "+target + " -x "+extract + " -g "+Dimer1+" " " -s "+spin +" " +  outputs[i] + ">" + output_Dimer1)
#  os.system("python3 nw_rtparse.py  "+target + " -x "+extract + " -g "+Dimer2+" "+ " -s "+spin+" "+ outputs[i] + ">" + output_Dimer2)
#  os.system("paste"+" "+ output_Dimer1 +" "+ output_Dimer2 +" > "+ filename+".charge") 
  i=i+1



