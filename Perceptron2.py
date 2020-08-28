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


"""
계단함수와 시그모이드 함수는 입력이 중요하면 큰 값을 출력하고 입력이 중요하지 않으면 작은 값을 출력한다는 공통점이 있다.
"""

# 비선형 함수

"""
ReLU 함수
"""


def relu(x):
    return np.maximum(0, x)


"""
ReLU는 0 이하는 0으로 그 이상은 그대로 출력하기 때문에 0이 기준이다.
maximum 함수는 두 입력중 큰 값을 선택해 반환하는 함수이다.
"""
