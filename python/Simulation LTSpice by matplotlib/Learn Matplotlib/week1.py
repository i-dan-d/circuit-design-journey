import numpy as np 
import matplotlib.pyplot as plt

# Linear data
y1 = np.arange(0, 10, 0.5)
x1 = np.linspace(0, 10, len(y1))
plt.plot(x1, y1, color="green")
# sin/cos data
y2 = np.sin(x1)
y3 = np.cos(x1)
plt.plot(x1, y2, color="red")
plt.plot(x1, y3, color="orange")
#  Element-wise power
y4 = (y2**2)+2
plt.plot(x1, y4, color="pink")
# Random data
# np.random.seed(1)
# x2 = np.random.rand(10)
# y5 = np.random.randn(10)
# plt.plot(x2, y5, color="yellow")

plt.title("Duy handsome")
plt.show()