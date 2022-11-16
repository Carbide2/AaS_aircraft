from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

CL = 1  # lift coefficient
CD = CL/20  # drag coefficient
p = 1.28  # air density; kg/m3
V2 = input('How fast would you like your plane to fly (in kph)? ')  # km/h
V1 = float(V2)  # km/h
V = float(V1/3.6)
BATwhkg1 = input('What would you like to set the battery density of the plane to (in Whr/kg)? ')  # Whr/kg
BATwhkg = float(BATwhkg1)  # Whr/kg
m01 = input("What would you like your plane's empty weight to be (in kg)? ")  # kg
m0 = float(m01)  # kg
mBAT1 = input('How heavy would you like your battery to be (in kg)? ')
mBAT = float(mBAT1)
ws1 = input('How wide would you like your wing to be (in metres, from tip to tip)? ')  # metres
ws = float(ws1)  # metres
wc1 = input('How deep would you like your wing to be (in metres, from front to back)? ')  # metres
wc = float(wc1)  # meters
S = ws*wc  # metres2
mg = ((p/2)*(V**2))*S*CL
g = mg/(m0+mBAT)
plev = (CD/CL**(3/2))*(np.sqrt((2*((m0+mBAT)*g)**3)/(p*S)))

tflightmax4 = ((BATwhkg*mBAT) / plev)
print(tflightmax4)
