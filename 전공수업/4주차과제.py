import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

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


def fitting(num):
    k = KMeans(num)
    k.fit(vector_values)

    X = [vector_values[h][0] for h in range(len(vector_values))]
    Y = [vector_values[j][1] for j in range(len(vector_values))]

    plt.scatter(X, Y, c=k.labels_, cmap='rainbow')
    plt.title('K = {}'.format(num))
    print('K = {}, means: {}'.format(num, k.cluster_centers_))
    plt.show()


for i in range(1, 5):
    fitting(i)
