import threading 
import time

def print_epoch(nameOfThread,delay):
    count = 0
    
    while count < 3:
        time.sleep(delay)
        count +=1
        
        print(nameOfThread,"-----",time.time())
        
def print_cube(num):
    print("cube = {}" .format(num**3))
    
def print_square(num):
    print("square = {}" .format(num**2))
    
if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(7,))
    t2 = threading.Thread(target=print_cube, args=(7,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("Finished!")