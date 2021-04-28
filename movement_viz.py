from matplotlib import pyplot
import os
import random
import time

def update_grid(data, good_term_states, bad_term_states, obstacles, run_num):
    pyplot.figure(1)
    pyplot.clf()
    pyplot.imshow(data)
    pyplot.draw()
    pyplot.ylim(-1, 41)
    pyplot.xlim(-1,41)
    for x in good_term_states:
        pyplot.plot(x[0], x[1], marker="s", color = 'g')
    for y in bad_term_states:
        pyplot.plot(y[0], y[1], marker="s", color = 'r')
    for z in obstacles:
        pyplot.plot(z[0], z[1], marker="s", color = 'k')
    pyplot.show(block = False)
    pyplot.pause(0.0001)
    
    if not os.path.exists("./runs/attempt-{}".format(run_num)):
        os.makedirs("./runs/attempt-{}".format(run_num))
    pyplot.savefig("./runs/attempt-{}/output-plot.png".format(run_num))
