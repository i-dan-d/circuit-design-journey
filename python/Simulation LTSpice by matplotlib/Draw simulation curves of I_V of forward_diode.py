import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

raw_data = "F:/Circuit_Design/circuit-design-journey/LTSpice/Diode_&_I_V.csv"
# ----------------------cách đọc file bằng open ---------------------
with open(raw_data, "r", encoding="utf-8") as simulation:
	title = simulation.readline().split()
	Arr = [[] for x in range(len(title))] # tạo list riêng biệt còn thằng ở dưới thì tạo các list cùng trỏ về một bộ nhớ, nên khi trỏ [1] thì toàn bộ 0,2,3.... cũng sẽ đc trỏ tới.
	# Arr = [[]] * len(title)
	for x in range(len(title)):
		title[x] = [title[x]]
	for value in simulation:
		arr_raw = simulation.readline().split()
		try:
			for col in range(len(Arr)):
				Arr[col].append(float(arr_raw[col]))
		except:
			continue
	x = np.array(Arr[0])   # trục X (Voltage)
	y1 = np.array(Arr[1])  # V(n001)
	y2 = np.array(Arr[2])  # V(n002)
	y3 = np.array(Arr[3])  # I(R1)
# -------------------- Cách đọc file bằng pandas--------------------------
# df = pd.read_csv(raw_data)
# x = df["V1"]
# y1 = df["V(n001)"]
# y2 = df["V(n002)"]
# y3 = df["I(R1)"]*1000 # đổi từ A sang mA


fig, ax1 = plt.subplots()

ax1.plot(x, y1, label="V(n001)", color="green")
ax1.plot(x, y2, label="V(n002)", color="blue")
ax1.set_xlabel("Voltage (V)")
ax1.set_ylabel("Voltage (V)")
ax1.legend(loc="upper left")

# Tạo trục y bên phải cho dòng điện
ax2 = ax1.twinx()
ax2.plot(x, y3, label="I(R1)", color="red")
ax2.set_ylabel("Current (mA)")
ax2.legend(loc="upper right")

# Làm đẹp: đổi màu trục y bên phải cho khớp với đường màu đỏ
ax2.tick_params(axis='y', colors='red')
ax2.spines['right'].set_color('red')

plt.title("PN Junction Simulation")
plt.show()
