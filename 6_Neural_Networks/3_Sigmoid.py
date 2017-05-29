import numpy as np

def sigmoid(x):
    # TODO: Implement sigmoid function
    return 1/(1 + np.exp(-x))

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# TODO: Calculate the output
output = sigmoid(np.dot(inputs, weights) + bias)

print('Output:')
print(output)

# sigmoid(x) = 1 /( 1 + e ** (−x))
# The sigmoid function is bounded between 0 and 1, 
# and as an output can be interpreted as a probability for success.