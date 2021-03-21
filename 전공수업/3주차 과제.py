import warnings
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)

reg = linear_model.LinearRegression()

num_points = 100
vector_set = []

for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vector_set.append([x1, y1])

x_data = [[v[0]] for v in vector_set]
"""
x_data 에서 독립변수를 2차원 배열로 만듦 
"""
y_data = [v[1] for v in vector_set]

reg.fit(x_data, y_data)

print("기울기:", reg.coef_)
print("y절편:", reg.intercept_)
print("유사도:", reg.score(x_data, y_data))

y_pred = reg.predict(x_data)

plt.scatter(x_data, y_data, color='red')
plt.plot(x_data, y_pred, color='blue', linewidth=3)
plt.show()
