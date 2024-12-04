import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100,1)
Y = 4 + 3 * X + np.random.randn(100, 1)

epochs = 50
lr = 0.01
n_samples, n_features = X.shape
w = np.random.randn(n_features,1)
b = np.random.randn(1)

for epoch in range(epochs):
    for i in range(n_samples):

        random_index = np.random.randint(n_samples)
        x_i = X[random_index:random_index + 1]
        y_i = Y[random_index:random_index + 1]

        y_pred = np.dot(x_i, w) +b
        error = y_pred - y_i

        dw = x_i.T @ error
        db = error

        w = w - lr * dw
        b = b - lr * db

    if epoch % 10 == 0:
        loss = (1 / n_samples) * np.sum((np.dot(X,w) + b -Y) **2)
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

print("Final wrights: ",w)
print("Final bias: ",b)