import numpy as pd
import matplotlib.pyplot as plt

#1. Gradient Descent is an algo which will find minima of a function which is differential.
#2. It is used to minimize loss or cost function
#3. Differentiation is just a way to measure how steep or curvy something is
#4. Formula : Xnew = Xold - n * F(Xold)     n = [learning rate]

#Q = f(x)=(x−3)^2
#Starting point = 8

def derivative(x):
    #2x -6
    return 2*x - 6

random_value = 8
learning_rate = 0.01

for steps in range(10):
    gradient = derivative(random_value)
    Xnew = random_value - learning_rate * gradient
    print(f"Step {steps + 1}: x = {Xnew}, f(x) = {(Xnew - 3)**2}")
    #print(random_value)
    random_value = Xnew
