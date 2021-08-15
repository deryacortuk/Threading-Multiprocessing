import threading
 

x = 1

def thread_task(lock):
    global x
    
    for i in range(17):
        
        lock.acquire()
        x += 1
        lock.release()
        
def main_task():
    
    lock = threading.Lock()
    
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args= (lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main_task()
    print("{0}".format(x))


