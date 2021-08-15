import time
from multiprocessing import Process, Lock, Value

def iterate_n(total, lock):
    for i in range(50):
        time.sleep(0.3)
        lock.acquire()
        total.value += 2
        lock.release()
    

def iterate_num(total, lock):
    for i in range(50):
        time.sleep(0.3)
        lock.acquire()
        total.value += 1
        lock.release()
   

if __name__ == "__main__":
    
    total = Value('i', 100)
    lock = Lock()
    
    process1 = Process(target = iterate_n, args=(total, lock))
    process2 = Process(target = iterate_num, args=(total, lock))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print(total.value)
    

    
    
   
    
    