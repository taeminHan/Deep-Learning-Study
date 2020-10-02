# 잘못된 예시

def numerical_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h


"""
반올림 오차로 인해 값이 틀어진다.
"""


def numerical_diff2(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)
