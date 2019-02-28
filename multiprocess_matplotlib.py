import multiprocessing as mp
import numpy as np
import matplotlib.pyplot as plt

def text1():
	x = np.linspace(-1,1,50)
	y = 3*x+1
	return figure_tx(x,y)
	
def text2():
	x = np.arange(0, 3*np.pi, 0.1)
	y = np.sin(x)
	return figure_tx(x,y)
	
def figure_tx(x,y):
	plt.figure()
	plt.plot(x,y)
	plt.show()
	
if __name__ == '__main__':
	t1 = mp.Process(target = text1)
	t2 = mp.Process(target = text2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	


	