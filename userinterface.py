from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

CL = 1.0  # lift coefficient
CD = CL/20  # drag coefficient
p = 1.28  # air density; kg/m3
g = 9.81  # m/s^2
BATwhkg1 = input('What would you like to set the battery density of the plane to (in Wh/kg)? ')  # Wh/kg
BATwhkg = float(BATwhkg1)  # Whr/kg
m01 = input("What would you like your plane's empty weight to be (in kg)? ")  # kg
m0 = float(m01)  # kg
V2 = input('How fast would you like your plane to fly (in kph)? ')  # km/h
V1 = float(V2)  # km/h
V = float(V1/3.6)  # m/s
ws1 = input('What would you like your wingspan to be (in metres, from tip to tip)? ')  # metres
ws = float(ws1)  # metres
wc1 = input('What would you like your wing chord to be (in metres, from front to back)? ')  # metres
wc = float(wc1)  # meters
S = ws*wc  # metres2

values = np.arange(0.001, (5*m0), 0.001)
tflightmax4 = []
tflightmax5 = []
batteryratio = []
for num in values:
    mg = ((p/2)*(V**2))*S*CL  # broken, need fix (plotting straight line)
    T = (p/2)*(V**2)*S*CL
    plev1 = T*V
    plev2 = (CD/CL**(3/2))*(np.sqrt((2*((m0+num)*g)**3)/(p*S)))
    tflightmax4.append((BATwhkg*num) / (CD/(CL**(3/2))*(np.sqrt((2*((m0+num)*g)**3) / (p*S)))))
    tflightmax5.append((BATwhkg*num)/plev2)
    batteryratio.append(num / m0)
print(max(tflightmax5))

plt.plot(batteryratio, tflightmax5, '#FF33FF')
plt.title('Flight time (m) by battery ratio')
plt.xlabel('Battery ratio (mBAT/m0)')
plt.ylabel('Flight time (m)')
plt.tight_layout()
plt.show()
# try calculating with m/s instead of kph... maybe works better????
