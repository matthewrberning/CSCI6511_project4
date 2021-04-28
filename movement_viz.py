from matplotlib import pyplot
import random
import time

def update_grid(data, good_term_states, bad_term_states, obstacles):
    pyplot.figure(1)
    pyplot.clf()
    pyplot.imshow(data)
    pyplot.draw()
    for x in good_term_states:
        pyplot.plot(x[0], x[1], marker="s", color = 'g')
    for y in bad_term_states:
        pyplot.plot(y[0], y[1], marker="s", color = 'r')
    for z in obstacles:
        pyplot.plot(z[1], z[0], marker="s", color = 'k')
    pyplot.show(block = False)
    pyplot.pause(0.0001)
    pyplot.savefig("./runs/output-plot.png")
