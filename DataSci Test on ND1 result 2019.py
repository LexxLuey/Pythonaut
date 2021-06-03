import pandas as pd

result_df = pd.read_csv('C:/Users/USER/Documents/pyttangz/dataman.csv')

print(result_df['COM_121'].describe())
print(result_df['COM_122'].describe())
print(result_df['COM_123'].describe())
print(result_df['COM_124'].describe())
print(result_df['COM_125'].describe())
print(result_df['COM_126'].describe())
print(result_df['EED_126'].describe())
print(result_df['GNS_121'].describe())
print(result_df['GNS_101'].describe())

result_df[['Surname'],['COM_121'],['COM_122'],['COM_123'],['COM_124'],['COM_125'],['COM_126'],['EED_126'],['GNS_121'],['GNS_101'],['Grade']] 

gradeStudents = result_df.groupby('Grade')

print(gradeStudents)

#for Grade. Grade_df in gradeStudents:
#	print(Grade)
#	print(Grade_df)



#print(result_df[result_df.COM_121 == result_df.COM_121.max()])

#print(result_df.shape)

#print(result_df)

print(gradeStudents.max())
