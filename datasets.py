import numpy as np
import math


wines = np.genfromtxt('/Users/ROrodri/Documents/pythoncsv/winequality-red.csv',delimiter=';',skip_header=1)
print(wines)

print("fiex acidity column",wines[:,0])

print("with the column shape \n",wines[:,0:1])

print(wines[:,0:3])

print(wines[:,[0,2,4]])


print(wines[:,-1].mean())



graduate_admissions = np.genfromtxt('/Users/ROrodri/Documents/pythoncsv/Admission_Predict.csv',dtype=None,delimiter=',',skip_header=1,names=('Serial No','GRE score','TOEFL score','University Rating','SOP','LOR','CGPA','Research','Chance of Admit'))
print(graduate_admissions)
print(graduate_admissions.shape)
print(graduate_admissions['CGPA'][0:5])
print(graduate_admissions['Chance_of_Admit'][0:5])

graduate_admissions['CGPA'] = graduate_admissions['CGPA'] /10 * 4
print(graduate_admissions['CGPA'][:20])
print(len(graduate_admissions[graduate_admissions['Research'] == 1]))

#Verificar si los estudiantes con altas posibilidades de aceptación >0.8 tienen en promedio un puntaje de GRE más alto 

print(graduate_admissions[graduate_admissions['Chance_of_Admit'] > 0.8 ]['GRE_score'].mean())
print(graduate_admissions[graduate_admissions['Chance_of_Admit'] < 0.4 ]['GRE_score'].mean())

#Realizaremos lo mismo con el punta de CGPA
print(graduate_admissions[graduate_admissions['Chance_of_Admit'] > 0.8 ]['CGPA'].mean())
print(graduate_admissions[graduate_admissions['Chance_of_Admit'] < 0.4 ]['CGPA'].mean())