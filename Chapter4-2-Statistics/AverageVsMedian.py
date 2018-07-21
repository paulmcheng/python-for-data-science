# np_baseball is available

# Import numpy
import numpy as np

b = np.array([[74., 72., 72., 73., 69., 69., 71., 76., 150.], [74., 72., 72., 73., 69., 69., 71., 76., 71.]])
np_baseball = b.transpose()

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))