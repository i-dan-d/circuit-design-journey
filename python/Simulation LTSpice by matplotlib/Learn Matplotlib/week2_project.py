import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
# ================= Week 2: The type of charts basic==============
# +++++++++++++++++ Data
amount = [0, 30]
count = 120
x1 = np.linspace(amount[0], amount[1], count)
y1 = np.sin(x1)

np.random.seed(1)
data1 = np.random.rand(500)
data2 = np.random.randn(500)
data3 = np.random.rand(500)

# 1. Dữ liệu thô (ví dụ: khảo sát trình duyệt khách hàng sử dụng)
raw_data = ['Chrome', 'Safari', 'Chrome', 'Edge', 'Chrome', 'Safari', 'Firefox', 'Chrome', 'Edge']

# 2. Chuẩn bị dữ liệu: Đếm số lần xuất hiện bằng Pandas
counts = pd.Series(raw_data).value_counts()

# Lấy values (số lượng) và index (tên nhóm)
sizes = counts.values
labels = counts.index
# ----------------- Line, Scatter and Bar
# fig,(ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(7,5))

# ax1.set_title("Line Chart")
# ax1.plot(x1,y1, label="Line chart", color="green")

# ax2.set_title("Scatter Chart")
# ax2.scatter(x1, y1, label="Scatter chart", color="blue")

# ax3.set_title("Bar chart")
# ax3.bar(x1, y1, label="Bar chart")

# ax4.set_title("Barh chart")
# ax4.barh(x1, y1, label="Barh chart", color="pink")
# # fig.add_subplot(3, 2, 6)
# fig.suptitle("Line, Scatter and Bar chart")
# ------------------ Histogram, Pie, Box/Violin chart
fig, axes = plt.subplots(3, 2, figsize=(7,6))
axes[0,0].hist(data1, bins=30, label="bins1=30", color='blue', edgecolor='black', alpha=0.7)
axes[0,1].hist(data1, bins=20, label="bins1=20", color='green', edgecolor='black', alpha=0.7)
axes[1,0].hist(data3, bins=30, label="bins2=30", color='blue', edgecolor='black', alpha=0.7)
axes[1,1].hist(data3, bins=20, label="bins2=20", color='green', edgecolor='black', alpha=0.7)
#  Với pieplot thì cần chuẩn bị 2 dạng dữ liệu, từ dữ liệu thô ban đầu rồi xuất ra label và sizes của label đó
axes[2,0].pie(sizes, labels=labels,autopct='%1.1f%%', startangle=90 )

axes[2,1].boxplot(data1, label='boxplot', vert=True, patch_artist=True)
axes[2,1].violinplot(data1, showmeans=True)
fig.suptitle("Histogram, pie, Box and Violin chart")
fig.patch.set_facecolor(color='brown')
fig.tight_layout()
fig.legend()
plt.show()