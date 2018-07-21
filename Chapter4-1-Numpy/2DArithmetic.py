# Import numpy package
import numpy as np

# baseball is available as a regular list of lists
b = np.array([[74, 72, 72, 73, 69, 69, 71, 76, 71], [215, 210, 210, 188, 176, 209, 200, 231, 180]])

# Create np_baseball (2 cols)
np_baseball = b.transpose()

# Create numpy array: conversion
conversion = [0.0254, 0.453592]

# Print out product of np_baseball and conversion
print(np_baseball * conversion)