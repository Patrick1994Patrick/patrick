import multiprocessing as mp
import threading as tp

def print_it(a,b):
	print(a+b)

print('all')
#print(mp.current_process())
if __name__ == '__main__' :
	p1 = mp.Process(target = print_it, args = (1,2))
	p2 = mp.Process(target = print_it, args = (4,56))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print('-------------------------')
	t1 = tp.Thread(target = print_it, args = (3,2))
	t2 = tp.Thread(target = print_it, args = (4,5))
	t1.start()
	t2.start()
	t1.join()
	t2.join()