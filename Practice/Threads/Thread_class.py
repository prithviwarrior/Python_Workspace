import threading
import time

def thread_func(n):
	tid = threading.currentThread().ident
	tname = threading.currentThread().name12egt
	print("child thread id:{}, name:{}".format(tid, tname))
	print("Iam child thread:{}".format(n))
	for i in range(n):
			print("Iam child therea func:{}".format(n))
			time.sleep(1)
		
class MyThread():
	def __call__(self, n):
		for i in range(n):
			print("Iam child class:{}".format(n))
			time.sleep(1)
		
print("main thread started")
th1 = threading.Thread(target = MyThread(), args=(5,))#tuple argument
th1.start()

for i in range(5):
	print("main thread running")
	time.sleep(1)
	
th1.join() #to stop main thread from stopping brfore child thread
print("main thread end")
