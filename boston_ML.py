# 라이브러리 사용
import pandas as pd
import tensorflow as tf

# 1.과거의 데이터를 준비
file = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(file)
boston.head()
print(boston.columns)

# 독립변수, 종속변수 분리
독립 = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
             'ptratio', 'b', 'lstat']]
종속 = boston[['medv']]

print(독립.shape, 종속.shape)

# 2. 모델의 구조 만들기
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

# 3. 데이터로 모델 학습
model.fit(독립, 종속, epochs=100000)

model.predict(독립[0:5])

종속[0:5]

# 모델의 수식 확인
model.get_weights()
