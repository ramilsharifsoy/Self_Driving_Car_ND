import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

# Network size
N_input = 4
N_hidden = 3
N_output = 2

np.random.seed(42)
# Create random Xs
X = np.random.randn(4)
print('Created random Xs:', '\n', X, '\n')

weights_input_to_hidden = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
weights_hidden_to_output = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))
print('Weights Input to Hidden:\n', weights_input_to_hidden,  '\n\n',
      'Weights Hidden to Output:\n', weights_hidden_to_output, '\n')

#Make a forward pass through the network
hidden_layer_in = np.dot(X, weights_input_to_hidden)
print('h is hidden layer in:', '\n', hidden_layer_in, '\n')

hidden_layer_out = sigmoid(hidden_layer_in)
print('Hidden-layer Output:', '\n', hidden_layer_out, '\n')

output_layer_in = np.dot(hidden_layer_out, weights_hidden_to_output)
print('h is output layer in:', '\n', output_layer_in, '\n')

output_layer_out = sigmoid(output_layer_in)
print('Output-layer Output:', '\n', output_layer_out, '\n')