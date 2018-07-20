# height and weight are available as a regular lists
weight = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180]
height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[5])

# Print out sub-array of np_height: index 1 up to and including index 5
print(np_height[1:5])