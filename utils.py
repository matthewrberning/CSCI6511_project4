import matplotlib.pyplot as plt

def plot_learning(worldId, epoch, cumulative_average)
	plt.plot(cumulative_average)
    plt.xscale('log')
    plt.savefig(f'runs/world_{worldId}_epoch{epoch}learning.png')