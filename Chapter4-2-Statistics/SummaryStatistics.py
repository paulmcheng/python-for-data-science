# Import numpy
import numpy as np

# np_baseball is available
b = np.array([[74., 72., 72., 73., 69., 69., 71., 76., 71.], [74., 72., 72., 73., 69., 69., 71., 76., 71.]])
np_baseball = b.transpose()

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))