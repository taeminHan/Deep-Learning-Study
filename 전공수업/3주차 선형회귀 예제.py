import matplotlib.pyplot as plt
from sklearn import linear_model

#선형회귀 모델 생성
reg = linear_model.LinearRegression()

X = [[0], [1], [2]]
Y = [3, 3.5, 5.5]

reg.fit(X, Y)

print("기울기: ", reg.coef_)
print("y절편: ", reg.intercept_)
print("유사도: ", reg.score(X, Y))

print(reg. predict([[5]]))

# 학습 데이터와 y값을 산포도로 그린다.
plt.scatter(X, Y, color = 'black')

# 학습 데이터를 입력으로 하여 예측값을 계산한다.
y_pred = reg.predict(X)

# 학습 데이터와 예측값으로 선그래프를 그린다.
# 계산된 기울기와 y절편을 가지는 직선이 그려진다.
plt.plot(X, y_pred, color='blue', linewidth = 3)
plt.show()
