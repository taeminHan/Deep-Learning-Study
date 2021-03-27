import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

num_vectors = 100
num_steps = 100
vector_values = []

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


def draw(k):
    sort_group = []
    dot = random.choice(vector_values)
    plt.scatter(dot[0], dot[1], c='red')
    for i, j in enumerate(vector_values):
        sort_group.append([((j[0] - dot[0]) ** 2 + (j[1] - dot[1]) ** 2) ** 0.5, i])
    q = sorted(sort_group, key=lambda x: x[0])

    for a in q[1:k + 1]:
        plt.scatter(vector_values[a[1]][0], vector_values[a[1]][1], c='red', marker='s')
    plt.show()


draw(5)
