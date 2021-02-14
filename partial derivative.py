# 예제 직접 해보기!
# 편미분


def function_2(x):
    # 인수 x는 넘파이 배열이라고 가정하자
    return x[0] ** 2 + x[1] ** 2
    # 또는 np.sum(x**2)


def numerical_diff2(f, x):
    h = 1e-4
    return print((f(x + h) - f(x - h)) / (2 * h))


# 문제 1: x0 = 3, x1 = 4일 때, x0에 대한 편미분

def function_tmp1(x0):
    return x0 * x0 + 4.0 ** 2.0


numerical_diff2(function_tmp1, 3.0)  # 6.00000000000378


# 문제 2: x0 = 3, x1 = 4일 때, x1에 대한 편미분

def function_tmp2(x1):
    return 3.0 ** 2.0 + x1 * x1


numerical_diff2(function_tmp2, 4.0)  # 7.999999999999119
