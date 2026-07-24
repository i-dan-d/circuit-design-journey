import numpy as np 
import matplotlib.pyplot as plt

#================= Day 1 to 2: Foundation of Numpy and Matplotlib structure
# Linear data
y1 = np.arange(0, 50, 0.1)
x1 = np.linspace(0, 100, len(y1))

# plt.plot(x1, y1, color="green")
# # sin/cos data
# y2 = np.sin(x1)
# y3 = np.cos(x1)
# plt.plot(x1, y2, color="red")
# plt.plot(x1, y3, color="orange")
# #  Element-wise power
# y4 = (y2**2)+2
# plt.plot(x1, y4, color="pink")
# # Random data
# # np.random.seed(1)
# # x2 = np.random.rand(10)
# # y5 = np.random.randn(10)
# # plt.plot(x2, y5, color="yellow")

# plt.title("Duy handsome")
# plt.show()

# ============ Day 3-4: Figure, Axes and 2 style of code to draw curves
y2 = np.sin(x1)
y3 = np.cos(x1)
# This is style 1: Pylot style
# plt.plot(x1, y2, color="green")
# plt.plot(x1, y3, color="blue")
# plt.show()
# === THIS IS STYLE 2: OBJECT-ORIENTED (OO-style) "Hướng đối tượng"
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8, 4))

ax1.plot(x1, y2, color="green") 
# ax1.scatter(x1, y2, color="red") đánh dáu các điểm lên biểu đồ với tọa độ tương ứng
ax2.plot(x1, y3, color="blue")

plt.show()
