from api import API
from matplotlib import pyplot
import random
import time

def update_grid(data):
    pyplot.imshow(data)
    pyplot.draw()
    pyplot.show(block = False)
    pyplot.pause(1)

# testing api
a = API()
print(a.locate_me())

#initializing grid
fig = pyplot.figure(figsize=(5,5))

# testing grid display
data = [[random.randint(a=0,b=1) for x in range(0,8)], # row 1
        [random.randint(a=0,b=1) for x in range(0,8)], # row 2
        [random.randint(a=0,b=1) for x in range(0,8)], # row 3
        [random.randint(a=0,b=1) for x in range(0,8)], # row 4
        [random.randint(a=0,b=1) for x in range(0,8)], # row 5
        [random.randint(a=0,b=1) for x in range(0,8)], # row 6
        [random.randint(a=0,b=1) for x in range(0,8)], # row 7
        [random.randint(a=0,b=1) for x in range(0,8)]] # row 8
update_grid(data)

# testing display update in same window
data[0][0] = 4000
update_grid(data)

data[0][1] = 4000
update_grid(data)