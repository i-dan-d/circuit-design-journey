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
xRV = np.array(ArrRV[0]); y2RV = np.array(ArrRV[2])
xFW = np.array(ArrFW[0]); y2FW = np.array(ArrFW[2])

# Gộp 2 nhánh (âm + dương) thành 1 đường I-V liên tục
V = np.concatenate([xRV, xFW])
I = np.concatenate([y2RV, y2FW])

# Sắp xếp theo V tăng dần -> tránh đường bị "nhảy loạn" khi vẽ
idx = np.argsort(V)
V, I = V[idx], I[idx]

fig, ax = plt.subplots(figsize=(7,5))
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.plot(V, I, color='red', label="I(D2)")

ax.set_xlabel("V (Volt)")
ax.set_ylabel("I (A)")
ax.set_title("PN-Junction")

# Dòng thuận và dòng ngược lệch nhau rất nhiều bậc độ lớn
# -> dùng symlog để nhìn được cả 2 vùng trên cùng 1 trục tuyến tính-ish
ax.set_yscale('symlog', linthresh=1e-9)

ax.legend()
plt.grid(alpha=0.3)
plt.show()
