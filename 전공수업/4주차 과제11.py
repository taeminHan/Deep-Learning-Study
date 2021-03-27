import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import itertools

vector_values = []
random_dot = []
df1 = []
df2 = []
asd = []


def dot(num_vectors):
    for i in range(num_vectors):
        if np.random.random() > 0.5:
            vector_values.append([np.random.normal(0.5, 0.6),
                                  np.random.normal(0.3, 0.9)])
        else:
            vector_values.append([np.random.normal(2.5, 0.4),
                                  np.random.normal(0.8, 0.5)])

    df = pd.DataFrame({"x": [v[0] for v in vector_values],
                       "y": [v[1] for v in vector_values]})
    sns.lmplot("x", "y", data=df, fit_reg=False, height=7)


def clustering(k, random_dot):
    color_cycle = itertools.cycle(["grey", "green"])

    for _ in range(k):
        random_dot.append(random.choice(vector_values))
    random_dot = np.array(random_dot)

    X = [vector_values[h][0] for h in range(len(vector_values))]
    Y = [vector_values[j][1] for j in range(len(vector_values))]
    plt.scatter(X, Y, c='g')

    for i in random_dot:
        plt.scatter(i[0], i[1], c=next(color_cycle))


def near_point(random_dot):
    for d in vector_values:
        if ((random_dot[0][0] - d[0]) ** 2 + (random_dot[0][1] - d[1]) ** 2) ** 0.5 < (
                (random_dot[0][0] - d[0]) ** 2 + (random_dot[1][1] - d[1]) ** 2) ** 0.5:
            plt.scatter(d[0], d[1], c='grey')
            df1.append([d[0], d[1]])
        else:
            plt.scatter(d[0], d[1], c='green')
            df2.append([d[0], d[1]])
    x = sorted(df1, key=lambda x: [x[0], x[1]])[len(df1) // 2][0]
    y = sorted(df1, key=lambda x: [x[0], x[1]])[len(df1) // 2][1]
    plt.scatter(x, y, marker= 's', c = 'b', s=100)
    x = sorted(df2, key=lambda x: [x[0], x[1]])[len(df1) // 2][0]
    y = sorted(df2, key=lambda x: [x[0], x[1]])[len(df1) // 2][1]
    plt.scatter(x, y,marker='s', c='r', s=100)



dot(100)

clustering(2, random_dot)
near_point(random_dot)
plt.title("2")
plt.show()