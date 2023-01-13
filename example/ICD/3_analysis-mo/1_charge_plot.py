import math
import numpy as np
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
#from statistics import mean
#plt.rc('figure', max_open_warning = 0)

charge1=10
charge2=18
############ Read files ##############
outfile = glob.glob("*.charge")  #("*_v5.avg"+kind))

i=0
while i < len(outfile):
  ifile=outfile[i]
#  filename=outfile[ifile]
  sdata=np.transpose(np.loadtxt(ifile))
#  datas=pd.read_csv(ifile, kiprows=26)
#  ndata=len(data[1])//2-1
#  sdata=data[:,0:ndata]
  xdata=sdata[0]
  y1data=sdata[1]+charge1
  y2data=sdata[3]+charge2

############# Plot ################## 
  out_name=outfile[i].strip(".charge")
  plt.figure(figsize=(12,10))
#  plt.plot(xdata,ydata,linewidth=3, label=labelname)#filename)
  plt.legend(fontsize=18)
  plt.xticks(fontsize=16)
  plt.yticks(fontsize=16)
  plt.xlabel('Time (au)',fontsize=16)
  plt.ylabel('Charge loss',fontsize=16)
 #plt.xlim(0,3000)
  plt.plot(xdata, y1data, color = 'red',linewidth=0.5,label ='Ne')#, linestyle="dotted" )
  plt.plot(xdata, y2data, color = 'blue',linewidth=0.5,label ='Ar')#, linestyle="dotted" )
#  plt.legend()
  #plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
  #plt.ylim(bottom=0)
#  plt.text(2, 1.98, "List of existing figure numbers : "+ str(w), fontsize = 12)
#  plt.title('matplotlib.pyplot.get_fignums() function Example', fontweight ="bold")
  plt.savefig(out_name+'.jpg') #,bbox_inches='tight')
 #plt.show()
  i=i+1

 




 
