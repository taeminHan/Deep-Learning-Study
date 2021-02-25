# 양쪽의 편미분을 묶어서 계산한다고 할때는 어떻게 해야 할까?
import numpy as np


def numerical_gradient(f, x):
    h = 1e-4  # 0.001
    grad = np.zeros_like(x)  # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x + h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 값 복원

    print(grad)
    """
        numerical_gradient: 함수의 구현은 복잡하지만 동작 방식은 변수가 하나일때의 수치 미분과 거의 같다.
    """


def function_2(x):
    # 인수 x는 넘파이 배열이라고 가정하자
    return x[0] ** 2 + x[1] ** 2
    # 또는 np.sum(x**2)


numerical_gradient(function_2, np.array([3.0, 4.0]))  # [6. 8.]
# [실제로는 6.00000~, 7.999999~]라는 값을 얻지만 넘파이 배열을 출력할 때 수치를 보기 쉽도록 하공하기 때문에 위와같이 출력하게 된다.
numerical_gradient(function_2, np.array([0.0, 2.0]))  # [0. 4.]
numerical_gradient(function_2, np.array([3.0, 0.0]))  # [6. 0.]

# 기울기가 가리키는 쪽은 각 장소에서 함수의 출력 값을 가장 크게 줄이는 방향이다.
