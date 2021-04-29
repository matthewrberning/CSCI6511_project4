import matplotlib.pyplot as plt
import os

def plot_learning(worldId, epoch, cumulative_average, rn):
    plt.figure(2)
    plt.plot(cumulative_average)
    plt.xscale('log')
    if not os.path.exists(f'runs/world_{worldId}/attempt_{rn}'):
        os.makedirs(f'runs/world_{worldId}/attempt_{rn}')
    plt.savefig(f'runs/world_{worldId}/attempt_{rn}/world_{worldId}_epoch{epoch}learning.png')