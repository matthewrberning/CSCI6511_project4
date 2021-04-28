from matplotlib import pyplot
import random
import time
import movement_viz as v

#initializing grid
fig = pyplot.figure(figsize=(10,10))

# testing grid display
data = [[0] * 40 for temp in range(40)]
v.update_grid(data)

# testing display update in same window
data[0][0] = 1
v.update_grid(data)
data = [[0] * 40 for temp in range(40)]

data[0][1] = 1
v.update_grid(data)
data = [[0] * 40 for temp in range(40)]