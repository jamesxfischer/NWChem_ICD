import numpy as np 
import glob 

S=np.loadtxt("gamma1.0-zeta1.0-E0.07-time.0.Smat")
C_file=open("gamma1.0-zeta2.5-E0.10-dis3.3.Cmo","r")
mo_numbers=54
#S_diag, S_vec = np.linalg.eigh(S)
AOmats=glob.glob("*.rt_restart")
#lamda=np.dot(S_vec, np.dot(S, S_vec.T))
#S_daig_matrix = S_diag * np.eye(len(S_diag))        ##  This is small s
#S_sqrt_inv = np.sqrt(np.linalg.inv(S_daig_matrix))  ##  s的-1/2次方

AO_elements=(mo_numbers*mo_numbers)*4                ##   4 for os, 2 for cs
print("Numbers of AO elements : ",AO_elements)

re_list=[]
j=0
while j < AO_elements:
        re_list.append(j)
        j=j+2

im_list=[]
j=1
while j < AO_elements:
	im_list.append(j)
	j=j+2
half_elements=len(re_list)//2

#####  transform Pmo to Pao #####
##  Pmo= C+.S.Pao.S.C
## YS: How to ignore the useless lines in movec files?

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


i=0
while i < len(AOmats):
	Pao= np.loadtxt(AOmats[i])
	Pre=np.delete(Pao,im_list)
	re_alpha_list, re_beta_list=Pre[:half_elements], Pre[half_elements:]
	P_alpha=re_alpha_list.reshape(mo_numbers,mo_numbers)
	P_beta=re_beta_list.reshape(mo_numbers,mo_numbers)
#	np.savetxt("test.P",P,fmt='%10.10f',delimiter=' ')
#	P=np.delete(P2,im_list)
#	np.savetxt("test.P",P,fmt='%10.10f',delimiter=' ')
#	print(P.shape)
	filename=AOmats[i]
	labelname=filename.strip(".rt_restart") 
#	np.savetxt("test.P2",P2,fmt='%10.10f',delimiter=' ')

	SPaS=np.dot(S, np.dot(P_alpha,S))
	SPbS=np.dot(S, np.dot(P_beta,S))
#	Pmo=np.dot(np.transpose(Cmo), np.dot(SPS, Cmo))
	Pa_mo=np.dot(Cmo, np.dot(SPaS, np.transpose(Cmo)))
	Pb_mo=np.dot(Cmo, np.dot(SPbS, np.transpose(Cmo)))
	# print("P': \n", Pmo)
	np.savetxt(labelname+".Pmo_alpha",Pa_mo,fmt='%10.10f',delimiter=' ')
	np.savetxt(labelname+".Pmo_beta",Pb_mo,fmt='%10.10f',delimiter=' ')
	i=i+1

