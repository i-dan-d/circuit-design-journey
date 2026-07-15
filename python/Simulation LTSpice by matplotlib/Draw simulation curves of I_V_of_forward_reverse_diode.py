import matplotlib.pyplot as plt 
import numpy as np 

raw_data_forward = "F:/Circuit_Design/circuit-design-journey/LTSpice/Forward_diode.csv"
raw_data_reverse = "F:/Circuit_Design/circuit-design-journey/LTSpice/Reverse_Diode.csv"
with open(raw_data_forward, 'r', encoding="utf-8") as data_FW:
	tittle = data_FW.readline().split()
	ArrFW = [[] for x in range(len(tittle))]
	for rawFW in data_FW:
		arrRaw = rawFW.split()
		for col in range(len(tittle)):
			ArrFW[col].append(float(arrRaw[col]))
with open(raw_data_reverse, 'r', encoding="utf-8") as data_RV:
	tittle = data_RV.readline().split()
	ArrRV = [[] for x in range(len(tittle))]
	for rawRV in data_RV:
		arrRaw = rawRV.split()
		for col in range(len(tittle)):
			ArrRV[col].append(float(arrRaw[col]))
xRV = np.array(ArrRV[0])
y1RV = np.array(ArrRV[1])
y2RV = np.array(ArrRV[2])

xFW = np.array(ArrFW[0])
y1FW = np.array(ArrFW[1])
y2FW = np.array(ArrFW[2])
fig, ax = plt.subplots()
# Vẽ trục x và y
ax.axhline(0, color='black', linewidth=1)  # trục x
ax.axvline(0, color='black', linewidth=1)  # trục y
# ax.plot(xFW,y1FW, color="green")
# ax.plot(xRV,y1RV, color="green")
ax.plot(xFW, y2FW, label="I(D-FW)", color="red")
ax.plot(xRV, y2RV, label="I(D-RW)", color="blue")
ax.set_xlabel("V - Voltage")
ax.set_ylabel("mA - Current")


plt.title("PN-Junction")
plt.show()
