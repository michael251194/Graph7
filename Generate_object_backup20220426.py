# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:02:19 2022

@author: Michaël Teti
"""

import pandas as pda
import numpy as np
import matplotlib as mt
import csv

#déclaration des listes utilisées dans l'objet ww
lengh1 = 100
lengh2 = 1000
lengh3 = 10
lengh4 = 30

CfgActualStep = np.empty(lengh1, dtype=('U128'))
CfgNextStep = np.empty(lengh2, dtype=('U128'))
CfgNextStepDesc1 = np.empty(lengh2, dtype=('U128'))
CfgNextStepDesc2 = np.empty(lengh2, dtype=('U128'))
CfgNextStepDesc3 = np.empty(lengh2, dtype=('U128'))

ActualNextStep = np.empty(lengh3, dtype=('U128'))
ActualNextStepDesc = np.empty(lengh4, dtype=('U128'))
#initialise les valeurs du tableaux avec une virgule
for i in range(0,99):
    CfgActualStep[i]=","
    
for i in range(0,999):
    CfgNextStep[i]=","
    CfgNextStepDesc1[i]=","
    CfgNextStepDesc2[i]=","
    CfgNextStepDesc3[i]=","

for i in range(0,9): 
    ActualNextStep[i]=","

for i in range(0,29): 
    ActualNextStepDesc[i]=","

#take data from excel"
df = pda.read_excel('C:\Python_project\createObject_ww\grafcet.xlsx')
shapedf = df.shape
nbrSteps = shapedf[0]
nbrLine = shapedf[1] 

#tbleaux utilisés pour extraire les données du fichier excel
tabExcel = np.empty(shape=shapedf, dtype=('U128'))

#copy tableaux excel dans un tableau numpy
for i in range(0,nbrLine):
    tabExcel[:,i] = df.iloc[:,i]
    #print (tabExcel[:,i])

#écriture dans les listes de l'objet
#écriture dans le CfgActualStep
ActualStepCfg = "{}{}{}{}" 
for i in range(0, nbrSteps): 
    CfgActualStep[i] = ActualStepCfg.format(tabExcel[i,0],'. ', tabExcel[i,1],',')
    #print (CfgActualStep[i])
    
#écriture dans le cfgNextStep
for i in range(0, nbrSteps):
    i = i*10  
    l = 2        
    for j in range(0,10):
        nextStepCfg = "{}{}{}{}" 
        temp1 = i+j
        temp2 = int(i/10) 
        
        #écriture config next step
        nbrStepStr = tabExcel[temp2,l]
        if nbrStepStr != ',':
            nbrStepInt = int(nbrStepStr)
            NameStep = tabExcel[nbrStepInt, 1]
            CfgNextStep[temp1] = nextStepCfg.format(nbrStepStr, '. ',NameStep,',')
        
        #écriture config next step desc 1, 2, 3
        Desc1 = l + 1
        Desc2 = l + 2
        Desc3 = l + 3 
        descCfg1 = "{}{}" 
        descCfg2 = "{}{}" 
        descCfg3 = "{}{}" 
        CfgNextStepDesc1[temp1]=descCfg1.format(tabExcel[temp2,Desc1],',')
        CfgNextStepDesc2[temp1]=descCfg2.format(tabExcel[temp2,Desc2],',')
        CfgNextStepDesc3[temp1]=descCfg3.format(tabExcel[temp2,Desc3],',')
        l=l+4
        
#écriture dans le fichier CSV.

df_csv = pda.read_csv('C:/Python_project/createObject_ww/template_gen_ph.csv',encoding=('U16'), sep=',', header=None,quoting=3, skiprows=5, na_filter=(False))
for i in range(15,24):
    j = i- 15
    df_csv.iloc[0,i] = ActualNextStep[j]
    
for i in range(24,123): 
    j = i - 24
    df_csv.iloc[0,i] = CfgActualStep[j]
    
for i in range(124, 1123): 
    j = i - 124 
    df_csv.iloc[0,i] = CfgNextStep[j]
    
for i in range(1124, 1153): 
    j = i - 1124
    df_csv.iloc[0,i] = ActualNextStepDesc[j]

for i in range(1154, 2153):
    j = i - 1154
    df_csv.iloc[0,i] = CfgNextStepDesc1[j]
    
#for i in range()
print (df_csv.iloc[0,25])

df_csv.to_csv('C:/Python_project/createObject_ww/template_gen_ph_buffer.csv',encoding=('U16'), sep=',', header=None,quoting=3, escapechar=(','))
#if df_csv.iloc[0,0] == '': 
#    print('ok')









