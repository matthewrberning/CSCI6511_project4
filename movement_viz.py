from matplotlib import pyplot
import os
import random
import time

def update_grid(data, good_term_states, bad_term_states, obstacles, run_num, epoch, world):
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
    
    if not os.path.exists("./runs/world-{}/attempt-{}/epoch-{}".format(world,run_num, epoch)):
        os.makedirs("./runs/world-{}/attempt-{}/epoch-{}".format(world,run_num, epoch))
    pyplot.savefig("./runs/world-{}/attempt-{}/epoch-{}/epoch.png".format(world, run_num, epoch))
