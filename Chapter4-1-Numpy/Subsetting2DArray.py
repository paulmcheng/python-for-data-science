# Import numpy package
import numpy as np

# baseball is available as a regular list of lists
b = np.array([[74, 72, 72, 73, 69, 69, 71, 76, 71], [215, 210, 210, 188, 176, 209, 200, 231, 180]])

# Create np_baseball (2 cols)
np_baseball = b.transpose()

# Print out the 7th row of np_baseball
print(np_baseball[7,:])

# The indexes before the comma refer to the rows, while those after the comma refer to the columns.
# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 4th player
print(np_baseball[3, 0])
