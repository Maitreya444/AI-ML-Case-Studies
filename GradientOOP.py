from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np

X,y = make_regression(n_samples=100, n_features=1, n_informative=1, n_targets=1, noise=20)

plt.scatter(X,y)