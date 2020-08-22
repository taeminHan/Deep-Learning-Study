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