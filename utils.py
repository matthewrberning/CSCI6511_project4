import matplotlib.pyplot as plt

def plot_learning(worldId, epoch, cumulative_average, rn):
    plt.figure(2)
    plt.plot(cumulative_average)
    plt.xscale('log')
    plt.savefig(f'runs/attempt-{rn}/world_{worldId}_epoch{epoch}learning.png')