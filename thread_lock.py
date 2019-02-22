import threading

A = 1
f = open('C:\\Users\\Marvin\\Desktop\\jishu2.txt','a')
lock = threading.Lock()

def change_math(n):
	global A,f,lock
	lock.acquire()
	A = A + n
	print(A)	
	f.write(str(A)+'\n')
	lock.release()
	
	
def arange(n):
	for i in range(n):
		change_math(n)
		
if __name__ == '__main__':
	t1 = threading.Thread(target = arange, args = (5,))
	t2 = threading.Thread(target = arange, args = (6,))
	t1.start()
	t2.start()
	t2.join()
	t1.join()
	f.close()
