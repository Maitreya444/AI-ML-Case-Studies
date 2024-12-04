import random

# Define the derivative of the cost function
def derivative(x):
    return 2 * x - 6

# Simulated dataset: random data points
dataset = [random.uniform(0, 10) for _ in range(100)]  # 100 random data points

# Initialize parameters
learning_rate = 0.01
x_current = 0  # Initial parameter value
iterations = 10

print("Stochastic Gradient Descent:")
for step in range(iterations):
    # Step 4: Randomly pick a data point
    data_point = random.choice(dataset)
    
    # Step 5: Compute the gradient for the selected data point
    gradient = derivative(data_point)
    
    # Step 5: Update the parameter
    x_new = x_current - learning_rate * gradient
    
    # Calculate the cost function
    cost = (x_new - 3) ** 2
    print(f"Step {step + 1}: x = {x_new:.4f}, f(x) = {cost:.4f}")
    
    # Update the current parameter
    x_current = x_new
