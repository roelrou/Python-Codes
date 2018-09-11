import pandas as pd
import openpyxl
import csv
import collections  
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

Eo = 5.0    #Alpha energy
dx = 0.0001  

Eo_ar = Eo
R_ar=0
dE_ar=0 

columns  = ['Energy', 'dE/dX_argon']
dataar = pd.read_excel('data_He_Ar.xlsx', header=None , names=columns)
dataar.head()
print dataar


E_i_ar = dataar['Energy']
dEdx_i_ar = dataar['dE/dX_argon']

E_iList_ar = list(E_i_ar)
dEdx_iList_ar = list(dEdx_i_ar)

# For Helium.

R_arL = []
Eo_arL = []
dE_arL = []

while Eo_ar > 0: 
  interpolated_dEdx = float(interp1d(E_iList_ar,dEdx_iList_ar,fill_value="extrapolate")(Eo_ar))
  dE_ar = interpolated_dEdx*dx
  E_ar = Eo_ar - dE_ar
  R_ar += dx
  Eo_ar = E_ar
  R_arL.append(R_ar)
  Eo_arL.append(Eo_ar)
  dE_arL.append(dE_ar)

 # Create a dataframe.

particleState_ar = pd.DataFrame({'R_ar': R_arL, 'Eo_ar': Eo_arL, 'dE_ar': dE_arL})
#print particleState

particleState_ar.plot(x='R_ar',y='dE_ar')

plt.show()
