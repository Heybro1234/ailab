import numpy as np

class MCPNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
    
    def activate(self, inputs):
        if len(inputs) != len(self.weights):
            raise ValueError("Number of inputs does not match number of weights.")
        total = sum(w * x for w, x in zip(self.weights, inputs))
        return 1 if total >= self.threshold else 0

# Define the weights and thresholds for the MCP neurons
and_weights = [1, 1]
and_threshold = 2
or_weights = [1, 1]
or_threshold = 1
xor_weights1 = [1, 1]
xor_threshold1 = 1
xor_weights2 = [-1, -1]
xor_threshold2 = -1
andnot_weights = [-1, 1]
andnot_threshold = 0

# Create the MCP neurons
and_neuron = MCPNeuron(and_weights, and_threshold)
or_neuron = MCPNeuron(or_weights, or_threshold)
xor_neuron1 = MCPNeuron(xor_weights1, xor_threshold1)
xor_neuron2 = MCPNeuron(xor_weights2, xor_threshold2)
andnot_neuron = MCPNeuron(andnot_weights, andnot_threshold)

# Define the inputs and the expected output for the logical functions
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
expected_and_output = [0, 0, 0, 1]
expected_or_output = [0, 1, 1, 1]
expected_xor_output = [0, 1, 1, 0]
expected_andnot_output = [1, 0, 0, 0]

# Iterate over the inputs and print the output of the MCP network for each function
for x, y in inputs:
    and_output = and_neuron.activate([x, y])
    or_output = or_neuron.activate([x, y])
    xor_output1 = xor_neuron1.activate([x, y])
    xor_output2 = xor_neuron2.activate([x, y])
    xor_output = xor_neuron1.activate([xor_output1, xor_output2])
    andnot_output = andnot_neuron.activate([x, y])
    print(f"Input: ({x}, {y}) AND Output: {and_output} OR Output: {or_output} XOR Output: {xor_output} AND NOT Output: {andnot_output}")
