# 잘못된 예시

def numerical_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h


"""
반올림 오차로 인해 값이 틀어진다.
"""


def numerical_diff2(f, x):
    h = 1e-4
    # return (f(x + h) - f(x - h)) / (2 * h)
    print((f(x + h) - f(x - h)) / (2 * h))


def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


"""
    y = 0.01x^2 + 0.1x의 그래프
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 20.0, 0.1)  # 0에서 20까지 0.1 간격의 배열 x를 만든다. (20은 미포함)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()

# x = 5일때와 10일 때 이 함수의 미분을 계산하면?

numerical_diff2(function_1, 5)  # 0.1999999999990898
numerical_diff2(function_1, 10)  # 0.2999999999986347