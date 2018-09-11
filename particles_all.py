import pandas as pd
import openpyxl
import csv
import collections  
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

Eo = 5.0    #Energia del ion de helio en MeV
dx = 0.0001  

#Inicializando variables
Eo_ar = Eo
R_ar=0
dE_ar=0 

Eo_c = Eo
R_c=0
dE_c=0 

Eo_fe = Eo
R_fe=0
dE_fe=0 

#Accesando a la energia y a los stopping power del archivo xlsx

columns  = ['Energy', 'dE/dX_argon', 'dE/dX_carbono', 'dE/dX_hierro' ]
data = pd.read_excel('data_He_Ar_C_Fe.xlsx', header=None , names=columns)
data.head()
print data  # Imprime la informacion del xlsx 

#Asignando la energia y los stopping power
E_i = data['Energy']
dEdx_i_ar = data['dE/dX_argon']
dEdx_i_c = data['dE/dX_carbono']
dEdx_i_fe = data['dE/dX_hierro']

#Asignando las variables a una lista
E_iList = list(E_i)
dEdx_iList_ar = list(dEdx_i_ar)
dEdx_iList_c = list(dEdx_i_c)
dEdx_iList_fe = list(dEdx_i_fe)

#Almacenando la informacion en los tres materiales
R_arL = []
Eo_arL = []
dE_arL = []

R_cL = []
Eo_cL = []
dE_cL = []

R_feL = []
Eo_feL = []
dE_feL = []

#Condiciones de la particula incidente al ingresar en los distintos materiales

while Eo_ar > 0: 
  interpolated_dEdx = float(interp1d(E_iList,dEdx_iList_ar,fill_value="extrapolate")(Eo_ar))
  dE_ar = interpolated_dEdx*dx
  E_ar = Eo_ar - dE_ar
  R_ar += dx
  Eo_ar = E_ar
  R_arL.append(R_ar)
  Eo_arL.append(Eo_ar)
  dE_arL.append(dE_ar)

while Eo_c > 0: 
  interpolated_dEdx = float(interp1d(E_iList,dEdx_iList_c,fill_value="extrapolate")(Eo_c))
  dE_c = interpolated_dEdx*dx
  E_c = Eo_c - dE_c
  R_c += dx
  Eo_c = E_c
  R_cL.append(R_c)
  Eo_cL.append(Eo_c)
  dE_cL.append(dE_c)

while Eo_fe > 0: 
  interpolated_dEdx = float(interp1d(E_iList,dEdx_iList_fe,fill_value="extrapolate")(Eo_fe))
  dE_fe = interpolated_dEdx*dx
  E_fe = Eo_fe - dE_fe
  R_fe += dx
  Eo_fe = E_fe
  R_feL.append(R_fe)
  Eo_feL.append(Eo_fe)
  dE_feL.append(dE_fe)
 
  
# Crea un dataframe.

particleState_ar = pd.DataFrame({'R_ar': R_arL, 'Eo_ar': Eo_arL, 'dE_ar': dE_arL})
particleState_c = pd.DataFrame({'R_c': R_cL, 'Eo_c': Eo_cL, 'dE_c': dE_cL})
particleState_fe = pd.DataFrame({'R_fe': R_feL, 'Eo_fe': Eo_feL, 'dE_fe': dE_feL})

#print particleState

particleState_ar.plot(x='R_ar',y='dE_ar')
plt.ylabel('Stopping power', fontsize=16)
plt.xlabel('R', fontsize=16)
plt.suptitle('Argon')
particleState_c.plot(x='R_c',y='dE_c')
plt.ylabel('Stopping power', fontsize=16)
plt.xlabel('R', fontsize=16)
plt.suptitle('Carbono')
particleState_fe.plot(x='R_fe',y='dE_fe')
plt.ylabel('Stopping power', fontsize=16)
plt.xlabel('R', fontsize=16)
plt.suptitle('Hierro')
plt.show()
