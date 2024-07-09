import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 示例数据
np.random.seed(42)
n_samples = 100
data = pd.read_csv("/Users/jinx/code/Rs/p_data.csv")

# 逻辑回归模型
X = data[['ALB', 'age', 'PLT']]
y = data['S']
X = sm.add_constant(X)  # 添加截距项
model = sm.Logit(y, X).fit()

# 打印模型摘要
print(model.summary())

# 绘制列线图
def plot_nomogram(model, feature_names, figsize=(10, 7)):
    # 获取系数
    coef = model.params
    # 获取每个特征的范围
    ranges = {name: (data[name].min(), data[name].max()) for name in feature_names}
    ranges['const'] = (1, 1)  # 截距项

    fig, axes = plt.subplots(len(coef), 1, figsize=figsize)
    if len(coef) == 1:
        axes = [axes]  # 处理单个特征的情况

    for ax, (name, c) in zip(axes, coef.items()):
        r = ranges[name]
        x = np.linspace(r[0], r[1], 100)
        y = c * x
        ax.plot(x, y, label=f'{name} (coef={c:.2f})')
        ax.set_xlabel(name)
        ax.set_ylabel('Points')
        ax.legend()

    plt.tight_layout()
    plt.show()

# 调用绘图函数
feature_names = ['ALB', 'age', 'PLT']
plot_nomogram(model, feature_names)
