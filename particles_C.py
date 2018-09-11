import pandas as pd
import openpyxl
import csv
import collections  
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

Eo = 5.0    #Alpha energy
dx = 0.0001  

Eo_he = Eo
R_he=0
dE_he=0 

columns  = ['Energy', 'dE/dX']
dataHe = pd.read_excel('data_He_C.xlsx', header=None , names=columns)
dataHe.head()
#print dataHe


E_i = dataHe['Energy']
dEdx_i = dataHe['dE/dX']

E_iList = list(E_i)
dEdx_iList = list(dEdx_i)

# For Helium.

R_heL = []
Eo_heL = []
dE_heL = []

while Eo_he > 0: 
  interpolated_dEdx = float(interp1d(E_iList,dEdx_iList,fill_value="extrapolate")(Eo_he))
  dE_he = interpolated_dEdx*dx
  E_he = Eo_he - dE_he
  R_he += dx
  Eo_he = E_he
  R_heL.append(R_he)
  Eo_heL.append(Eo_he)
  dE_heL.append(dE_he)

 # Create a dataframe.

particleState = pd.DataFrame({'R_he': R_heL, 'Eo_he': Eo_heL, 'dE_he': dE_heL})
#print particleState

particleState.plot(x='R_he',y='dE_he')

plt.show()
