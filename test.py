import threading
import time

def T1_job():
	start1 = time.time()
	print('this is job1:', threading.current_thread())
	try:
		f = open('eee.text','r+')
	except Exception as e:
		print(' error \n no file') 
		reply = input('do you wanna create one? \n')
		if reply == 'yes':
			f = open('eee.text','w+')
			content = input('please wirte: \n')
			f.write(content)

		else:
			pass
	else:
		f.write('ok')
	f.close()
	end1 = time.time()
	print('T1 ok', end1-start1)
	
def T2_job():
	start2 = time.time()
	print('this is job2:', threading.current_thread())
	end2 = time.time()
	print('T2 ok', end2-start2)
	
thread_1 = threading.Thread(target = T1_job, name = 'T1')
thread_2 = threading.Thread(target = T2_job, name = 'T2')

thread_1.setDaemon(True)
thread_2.setDaemon(True)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print('all done')