import numpy as np
import matplotlib.pylab as plt

"""
계단함수의 그래프 표현 
"""


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)  # -0.5 ~ 0.5전까지 0.1 간격의 넘파이 배열을 생성
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y축의 범위지정
plt.show()

"""
시그모이드 함수 구현
"""


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
