# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:02:19 2022

@author: Michaël Teti
"""

import pandas as pda
import numpy as np
import matplotlib as mt
import csv

#fonction pour concaténé " en debut et en fin de tableau
def concaGuillemet (debutOuFin, valeurAmodifie):
    debutOuFin = int(debutOuFin)
    valeurModifie = str('')
    str1 = str('"')
    
    if debutOuFin == 1: 
        valeurModifie = str1 + valeurAmodifie
    elif debutOuFin == 2 : 
        valeurModifie = valeurAmodifie + str1
    
    return valeurModifie

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
ActualStepCfg = "{}{}{}" 
for i in range(0, nbrSteps): 
    CfgActualStep[i] = ActualStepCfg.format(tabExcel[i,0],'. ', tabExcel[i,1])
    #print (CfgActualStep[i])
    
#écriture dans le cfgNextStep
for i in range(0, nbrSteps):
    i = i*10  
    l = 2        
    for j in range(0,10):
        nextStepCfg = "{}{}{}" 
        temp1 = i+j
        temp2 = int(i/10) 
        
        #écriture config next step
        nbrStepStr = tabExcel[temp2,l]
        if nbrStepStr != "/":
            nbrStepInt = int(nbrStepStr)
            NameStep = tabExcel[nbrStepInt, 1]
            CfgNextStep[temp1] = nextStepCfg.format(nbrStepStr, '. ',NameStep)
        
        #écriture config next step desc 1, 2, 3
        Desc1 = l + 1
        Desc2 = l + 2
        Desc3 = l + 3 
        CfgNextStepDesc1[temp1]=tabExcel[temp2,Desc1]
        CfgNextStepDesc2[temp1]=tabExcel[temp2,Desc2]
        CfgNextStepDesc3[temp1]=tabExcel[temp2,Desc3]
        l=l+4
        
#écriture dans le fichier CSV.

df_csv = pda.read_csv('C:/Python_project/createObject_ww/template_gen_ph.csv',encoding=('U16'), sep=',', header=None,quoting=3, skiprows=5, na_filter=(False))

for i in range(15,25):
    j = i- 15
    df_csv.iloc[0,i] = ActualNextStep[j]

df_csv.iloc[0,15] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,15])  
df_csv.iloc[0,24] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,24])  
########################################################  
for i in range(25,125): 
    j = i - 25
    df_csv.iloc[0,i] = CfgActualStep[j]

df_csv.iloc[0,25] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,25])  
df_csv.iloc[0,124] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,124]) 
######################################################    
for i in range(125, 1125): 
    j = i - 125 
    df_csv.iloc[0,i] = CfgNextStep[j]

df_csv.iloc[0,125] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,125])  
df_csv.iloc[0,1124] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,1124]) 
###########################################################  
for i in range(1125, 1155): 
    j = i - 1125
    df_csv.iloc[0,i] = ActualNextStepDesc[j]

df_csv.iloc[0,1125] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,1125])  
df_csv.iloc[0,1154] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,1154]) 
##########################################################
for i in range(1155, 2155):
    j = i - 1155
    df_csv.iloc[0,i] = CfgNextStepDesc1[j]

df_csv.iloc[0,1155] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,1155])  
df_csv.iloc[0,2154] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,2154]) 
##############################################################
for i in range(2156, 3156):
    j = i - 2156
    df_csv.iloc[0,i] = CfgNextStepDesc2[j]

df_csv.iloc[0,2156] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,2156])  
df_csv.iloc[0,3155] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,3155]) 
##############################################################
for i in range(3156, 4156):
    j = i - 3156
    df_csv.iloc[0,i] = CfgNextStepDesc3[j]

df_csv.iloc[0,3156] = concaGuillemet(debutOuFin = 1, valeurAmodifie = df_csv.iloc[0,3156])  
df_csv.iloc[0,4155] = concaGuillemet(debutOuFin = 2, valeurAmodifie = df_csv.iloc[0,4155]) 
##############################################################
#default value of IO_Actual_Step
df_csv.iloc[0,2155] = 0

#correction fin de ligne
for i in range(4156,4171): 
    j = i +100
    df_csv.iloc[0,i] = df_csv.iloc[0,j] 

for i in range(4172,4272):
    df_csv.iloc[0,i] = ''       

#for i in range(4172,4272):   
#    df_csv.drop(df_csv.columns[i], axis = 1,inplace= True ) 

print (df_csv.iloc[0,0])
print (df_csv.size)

#ecrire à la 6ieme ligne
df_csv.to_csv('C:/Python_project/createObject_ww/template_gen_ph_buffer.csv',encoding=('U16'), sep=',', header=None,quoting=3, escapechar=(','),index= False)










