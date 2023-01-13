import sys
import math
import numpy as np
from numpy import linalg as LA
import glob

np.printoptions(precision=10)
np.set_printoptions(threshold=sys.maxsize)


##### 0. parameters #####
Cmo_file=glob.glob("*.Cmo")
ops_or_cls="ops"      # openshell or closeshell
mo_numbers=54         # ??? might need to think about linear dependencies. 
occ_orbitals=14       # The number of occupoied orbitals
vac_idx=7             # The MO index of the hole 

##### 1. create a density matrix in MO basis (Pmo) #####
if ops_or_cls=="ops":
  occ=1
  occ_alpha=np.zeros(mo_numbers)
  i=0
  while i < occ_orbitals:
    occ_alpha[i]=occ_alpha[i]+occ
    i=i+1
#  occ_cls[vac_idx-1]=0          ##### default - hole on beta, uncomment this one in case we need
  Pmo_alpha=np.diag(occ_alpha)
  print(Pmo_alpha)

  occ_beta=np.zeros(mo_numbers)
  i=0
  while i < occ_orbitals:
    occ_beta[i]=occ_beta[i]+occ
    i=i+1
  occ_beta[vac_idx-1]=0          ##### default - hole on beta
  Pmo_beta=np.diag(occ_beta)
  print(Pmo_beta)

##### 2. transform Pmo to Pao #####
## 2.1 Pao= C.Pmo.C+, C is movecs   
C_file=open(Cmo_file[0],"r")
C_lines=C_file.readlines()
line=0
Cmo_list=[]
while line < len(C_lines):
	element=C_lines[line].strip('\n').split()
	i=0
	while i < len(element):
		Cmo_list.append(float(element[i].strip("\n")))
		i=i+1
	line=line+1
Cmo=np.array(Cmo_list).reshape(mo_numbers,mo_numbers)
#print(Cmo)
Cmo_trans= np.transpose(Cmo)
#print(Cmo_trans)
Pao_alpha=np.dot(Cmo_trans, np.dot(Pmo_alpha, Cmo))
Pao_beta=np.dot(Cmo_trans, np.dot(Pmo_beta, Cmo))
#print(Pao_alpha)
#print(Pao_beta)

## 3. calculate checksum ## 
alpha=[]
i=0
while i < mo_numbers:
  j=0
  while j < mo_numbers:
    alpha.append(Pao_alpha[i][j])      
    j=j+1
  i=i+1

beta=[]
i=0
while i < mo_numbers:
  j=0
  while j < mo_numbers:
    beta.append(Pao_beta[i][j])  
    j=j+1
  i=i+1

sum_alpha1=LA.norm(alpha,1)
sum_alpha2=LA.norm(alpha,np.inf)
checksum_alpha=1.67*sum_alpha1+0.12 * math.sqrt(abs(sum_alpha2))

sum_beta1=LA.norm(beta,1)
sum_beta2=LA.norm(beta,np.inf)
checksum_beta=1.67*sum_beta1+0.12 * math.sqrt(abs(sum_beta2))

checksum=checksum_alpha+checksum_beta
print("checksum = ",checksum)

######################
nw_files=glob.glob("*.nw")
x=0
while x < len(nw_files):
	filename=nw_files[x].strip(".nw")
	datafile = open(filename+'.rt_restart', 'w+') 
	datafile.write('RT-TDDFT restart file'+'\n')
	datafile.write('created   Sat Jun 30 07:49:38 2022'+'\n') 
	datafile.write("nmats"+"     "+str(2)+"\n")                 # cs-1, os-2
	datafile.write("nbf_ao"+"    "+str(mo_numbers)+"\n")
	datafile.write("it"+"        "+str(0)+"\n")
	datafile.write("t"+"           "+"0.000000000000E+00"+"\n")
	datafile.write("checksum"+"    "+str(format(checksum,'.12E'))+"\n")

	i=0
	while i < mo_numbers:
  		j=0
  		while j < mo_numbers:
    			datafile.write('{:>20}'.format(str(format(Pao_alpha[i][j],'.10E')))+"    "+"0.0000000000E+00")
    			j=j+1
  		i=i+1

	i=0
	while i < mo_numbers:
  		j=0
  		while j < mo_numbers:
    			datafile.write('{:>20}'.format(str(format(Pao_beta[i][j],'.10E')))+"    "+"0.0000000000E+00")
    			j=j+1
  		i=i+1
	x=x+1
datafile.close()

