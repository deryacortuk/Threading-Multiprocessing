import threading
import time

class ThreadExam(threading.Thread):
    def __init__(self, threadId, name, count):
        
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
        
    def run(self):
        print("start:" + self.name + "\n")
        lock.acquire()
        print_time(self.name, 1, self.count)
        lock.release()
        print("exiting:" + self.name +"\n")
        
def print_time(name,delay,count):
    while count:
        time.sleep(delay)
        print("%s: %s: %s" %(name,time.ctime(time.time()),count) + "\n")
        
        count -= 1
        
lock =threading.Lock()
   
thread1 = ThreadExam(1,"thread1", 10)
thread2 = ThreadExam(2,"thread2", 5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done!")