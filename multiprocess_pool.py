import multiprocessing as mp

def mathmping(a):

	print('now run %s' %a)
		
def multiping():
	pool = mp.Pool()
	for i in range(10):
		pool.apply_async(mathmping, args = (i,))

	pool.close()
	pool.join()
	print('Done')
	
if __name__ == '__main__': 
	multiping()
