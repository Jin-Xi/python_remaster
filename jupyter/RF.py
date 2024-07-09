import matplotlib.pyplot as plt
import numpy as np

# 示例数据：每个大柱子有三个小柱子的值
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values1 = [20, 35, 30, 35, 27]
values2 = [25, 32, 34, 20, 25]
values3 = [30, 29, 22, 25, 22]

# 设置每个大柱子的位置和宽度
x = np.arange(len(categories))
width = 0.25  # 每个小柱子的宽度

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, values1, width, label='Group 1')
rects2 = ax.bar(x, values2, width, label='Group 2')
rects3 = ax.bar(x + width, values3, width, label='Group 3')

# 添加标签、标题和图例
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Grouped Bars')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# 显示图形
plt.tight_layout()
plt.show()
