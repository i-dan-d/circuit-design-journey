import matplotlib.pyplot as plt 
import numpy as np 
#**Thực hành — Dự án:** Vẽ 1 figure có 4 đường (sin, cos, tuyến tính, parabol) trên cùng 1 axes, 
#mỗi đường có màu, label, linestyle khác nhau, có legend, title, grid.
data = [0, 10]
amount = 100
x1 = np.linspace(data[0], data[1], amount)
y1 = np.arange(data[0], data[1], data[1]/amount)

fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.plot(x1, np.sin(x1), color="green", label="Sin")
ax.plot(x1, np.cos(x1), color="blue", label="cos")
ax.plot(x1, y1, color="red", label="Linear")
ax.plot(x1, (x1**2), color="pink", label="Parabol")
# ax.hist(np.sin(x1))
# ax.boxplot(x1)
# -------- Axis and Tick with Axes
ax.set_title("This is title from Axes")
ax.set_xlim(0, 10)
ax.set_ylim(-1, 10)
# -------- Decoration
ax.legend()
ax.grid(True)
ax.annotate("Sin x Cos", xy=(0.785, 0.707), xytext=((0.785), 0.707))
ax.axhline(y=0.707) # X
ax.axvline(x=0.785) # Y
fig.suptitle("Practice project")
# fig.figimage(1, 10)
fig.savefig("project.png", dpi=300, bbox_inches='tight')

plt.show()