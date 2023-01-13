import numpy as np 
import glob 

basename="gamma1.0-zeta1.0-E0.07-time."
# MOmats=glob.glob("*.Pmo")
alpha_mats=glob.glob("*.Pmo_alpha")
beta_mats=glob.glob("*.Pmo_beta")

virt_list=[7]
hole_list=[9,10,11]
#virt_list=[15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

i=0
while i < len(hole_list):
	ra_file=open("rate_alpha."+str(hole_list[i])+"-"+str(virt_list[-1]), "w+")
	rb_file=open("rate_beta."+str(hole_list[i])+"-"+str(virt_list[-1]), "w+")
	rab_file=open("rate_ab."+str(hole_list[i])+"-"+str(virt_list[-1]), "w+")
	t=0
	while t < len(alpha_mats):
		j=0
		while j < len(virt_list):
			alpha_file=str(basename+str(t)+".Pmo_alpha")
			beta_file=str(basename+str(t)+".Pmo_beta")
			Pa_file= np.loadtxt(alpha_file)
			Pb_file= np.loadtxt(beta_file)
			Pab = Pa_file + Pb_file
			ra_file.write(str(Pa_file[hole_list[i]][virt_list[j]]) + "    ")
			rb_file.write(str(Pb_file[hole_list[i]][virt_list[j]]) + "    ")
			rab_file.write(str(Pab[hole_list[i]][virt_list[j]]) + "    ")
			j=j+1
		ra_file.write("\n")
		rb_file.write("\n")
		rab_file.write("\n")
		t=t+1
	i=i+1

