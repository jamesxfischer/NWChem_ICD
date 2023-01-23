import pandas as pd
import glob

list_csv=glob.glob("*.csv")
  
# merging two csv files
# result = pd.concat((pd.read_csv(the_csv,usecols=['distance','kcal/mol']) for the_csv in list_csv), axis='columns', join='outer')

# , names='distance')#join_axes=[list_csv[1].index])
#    map(pd.read_csv, list_csv))# , ignore_index=True)

df_list=[pd.read_csv(the_csv,usecols=['distance','kcal/mol'], dtype={'distance':str}) for the_csv in list_csv]
##
#
i=0
result=pd.DataFrame()
#result=df_list[0]
while i < len(df_list):
#for df in list_csv[1:]: #df_list[1:]:
	print(df_list[i])
	print(list_csv[i])
	theName=str(list_csv[i].strip('.csv'))
	result = pd.concat([result, df_list[i]],axis='columns', join='outer')
	result.rename(columns = {'kcal/mol':theName}, inplace = True)
#	result = pd.merge(result, df_list[i], on='distance') #ignore_index=True, axis='columns')
	i=i+1
print(result)

result.to_excel("NeAr_PES_all.xlsx")
