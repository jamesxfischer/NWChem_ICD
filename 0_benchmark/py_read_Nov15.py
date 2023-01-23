#python script to scrape out final energy from folder .nwo files

import os
import glob
import pandas as pd

#grab all nwo files
file_location = os.path.join('*.nwo')
filenames = glob.glob(file_location)
print(filenames[0])
csv_name=os.getcwd().split("/")[-1]  #os.path.split(path)[-1]
print(csv_name)
file_name = filenames[0]
split_filename = file_name.split('_')
func = split_filename[1]
# basis = split_filename[2]
basis = split_filename[2]+'-'+split_filename[3]


datafile = open(csv_name+'.csv', 'w+') # func + '_' + basis + '.csv', 'w+') 
datafile.write('distance,energy\n')
#loop through the file, look for 'Corrected energy ='
for f in filenames:
	#get the distance,basis set,funtional
	file_name = os.path.basename(f)
	#split file using "_" as deliminator
	split_filename = file_name.split('_')
	#distance is the 4th-7th character in the string
	distance = split_filename[6][4:8]
	#funtional and basis
	
	#output look for corrected enrgy keyword
	outfile = open(f, 'r')
	data = outfile.readlines()
	outfile.close()
	for line in data:
		if 'Corrected energy =' in line:
			energy_line = line
			words = energy_line.split()
			energy = words[3]
			#print(distance, energy)
			datafile.write(distance+','+energy+'\n')
datafile.close()

df=pd.read_csv(csv_name+'.csv')
df=df.sort_values('distance', ascending=True)
df['kcal/mol']=(df['energy']-df['energy'].iat[-1])*627.51
df.to_csv('../'+csv_name+'.csv', index=False)



