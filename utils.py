import matplotlib.pyplot as plt
import os
import numpy as np

def plot_learning(worldId, epoch, cumulative_average, rn):
    plt.figure(2)
    plt.plot(cumulative_average)
    plt.xscale('log')
    if not os.path.exists(f'runs/world_{worldId}/attempt_{rn}'):
        os.makedirs(f'runs/world_{worldId}/attempt_{rn}')
    plt.savefig(f'runs/world_{worldId}/attempt_{rn}/world_{worldId}_epoch{epoch}learning.png')

def epsilon_decay(epsilon, epoch, epochs):
	'''
	function to exponentially decrease the episilon value 
	acroccs the total number of epochs we train on
	this leads us to explore less as we progress through epochs 
	'''
    
    epsilon = epsilon*np.exp(-.01*epoch)
    
    print(f"\nNEW EPSILON: {epsilon}\n")
    return epsilon

