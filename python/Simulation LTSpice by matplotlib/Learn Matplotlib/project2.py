import numpy as np 
import matplotlib.pyplot as plt 
students = [650, 700, 650]
np.random.seed(2)
class1 = np.random.randint(1, 10, size=students[0])
class2 = np.random.randint(1, 10, size=students[1])
class3 = np.random.randint(1, 10, size=students[2])
class_merged = np.concatenate((class1, class2, class3))
fig, axes = plt.subplots(3, 4, figsize=(9,7))

axes[0,0].hist(class1,bins=15, color="blue", edgecolor="black", alpha=0.6, label='A')
axes[0,1].hist(class2,bins=15, color="green", edgecolor="black", alpha=0.6, label='B')
axes[0,2].hist(class3,bins=15, color="purple", edgecolor="black", alpha=0.6, label='C')
axes[0,3].hist(class_merged,bins=15, color="red", edgecolor="black", alpha=0.6, label='ABC')

axes[1,0].violinplot(class1)
axes[1,1].violinplot(class2)
axes[1,2].violinplot(class3)
axes[1,3].violinplot(class1)
axes[1,3].violinplot(class2)
axes[1,3].violinplot(class3)

axes[2,0].bar((sum(class1)/len(class1)), (sum(class1)/len(class1)), width=0.01)
axes[2,0].bar((sum(class2)/len(class2)), (sum(class2)/len(class1)), width=0.01)
axes[2,0].bar((sum(class3)/len(class3)), (sum(class3)/len(class1)), width=0.01)


fig.suptitle("Điểm thi của 200 học sinh 3 lớp A, B, C")
fig.tight_layout()
fig.legend()
plt.show()
print(class_merged)