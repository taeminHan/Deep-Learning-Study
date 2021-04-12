import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import seaborn as sb

data = np.genfromtxt('cancer_data.csv', delimiter=',', dtype=np.string_)
print(data.shape)