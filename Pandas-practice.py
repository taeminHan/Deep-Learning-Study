import pandas as pd

# 파일들로부터 데이터 읽어오기

file = './TIL/lemonade.csv'
lemonade = pd.read_csv(file)

file = './TIL/boston.csv'
boston = pd.read_csv(file)

file = './TIL/iris.csv'
iris = pd.read_csv(file)

# 데이터 모양으로 동작실행 확인하기

print(lemonade.shape)  # (6, 2)
print(boston.shape)  # (506, 14)
print(iris.shape)  # (150, 5)

# 칼럼이름 출력
print(lemonade.columns)  # Index(['온도', '판매량'], dtype='object')
print(boston.columns)  # Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat', 'medv'],
print(iris.columns)  # Index(['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭', '품종'], dtype='object')

independent = lemonade[['온도']]
dependent = lemonade[['판매량']]
print(independent.shape, dependent.shape)  # (6, 1) (6, 1)

independent = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
dependent = boston[['medv']]
print(independent.shape, dependent.shape)  # (506, 13) (506, 1)

independent = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
dependent = iris[['품종']]
print(independent.shape, dependent.shape)  # (150, 4) (150, 1)

print(lemonade.head())  # 상위 5개의 데이터를 추출
"""온도  판매량
0  20   40
1  21   42
2  22   44
3  23   46
4  24   48"""

print(boston.head())

"""
      crim    zn  indus  chas    nox  ...  tax  ptratio       b  lstat  medv
0  0.00632  18.0   2.31     0  0.538  ...  296     15.3  396.90   4.98  24.0
1  0.02731   0.0   7.07     0  0.469  ...  242     17.8  396.90   9.14  21.6
2  0.02729   0.0   7.07     0  0.469  ...  242     17.8  392.83   4.03  34.7
3  0.03237   0.0   2.18     0  0.458  ...  222     18.7  394.63   2.94  33.4
4  0.06905   0.0   2.18     0  0.458  ...  222     18.7  396.90   5.33  36.2
"""

print(iris.head())

"""
   꽃잎길이  꽃잎폭  꽃받침길이  꽃받침폭      품종
0   5.1     3.5     1.4       0.2       setosa
1   4.9     3.0     1.4       0.2       setosa
2   4.7     3.2     1.3       0.2       setosa
3   4.6     3.1     1.5       0.2       setosa
4   5.0     3.6     1.4       0.2       setosa

"""
