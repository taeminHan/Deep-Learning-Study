import numpy as np

"""
논리회로를 파이썬으로 구현 인수 x1, x2를 인수로 받는 AND 게이트 함수
매개변수 w1, w2, theta 는 함수 안에서 초기화를 한다.
가중치를 곱한 입력의 총합이 임계값을 넘으면 1을 반환 그 외에는 0을 반환한다.
"""


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7  # theta 는 임계값을 의미
    tmp = x1 * w1 + x2 * w2  # tmp 는 가중치*의 총합
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(AND(1, 0))  # 0

"""
0이 나오는 이유는 AND 게이트에서는 두 입력이 모두 1일 경우에만 참, 그 이외에는 0을 반환한다.
"""

# ===================================================================================


"""
weight(가중치), bias(편향)이 추가 되었다. 편향은 민감도설정이다. w1, w2와 기능이 다르다는 사실에 주의하자.
w1과 w2는 각 입력 신호가 결과에 주는 영향력(중요도)을 조절하는 매개변수이며, 
편향은 뉴런이 얼마나 쉽게 활성화하느냐를 조정하는 매개변수이다.
"""


# weight and bias in AND gate
def AND2(x1, x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([0.5, 0.5])  # weight (가중치)
    b = -0.7  # bias (민감도)
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(AND2(1, 0.4))

"""
np.sum(w*x) + b
= (0.5 * x1) + (0.5 * x2) + b
= (0.5 * 1) + (0.5 * 0.4) - 0.7
= 0.5 + 0.2 - 0.7
= 0
"""


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # AND 와는 가중치(w와 b)만 다르다
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # AND 와는 가중치(w와 b)만 다르다.
    b = -0.3
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

"""
AND, NAND, OR는 모두 같은 구조의 퍼셉트론이고, 차이는 가중치 매개변수의 값이다.
"""

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(x1, x2)
    return y

print(XOR(0, 0))  # 0을 출력
print(XOR(1, 0))  # 1을 출력
print(XOR(0, 1))  # 1을 출력
print(XOR(1, 1))  # 0을 출력
