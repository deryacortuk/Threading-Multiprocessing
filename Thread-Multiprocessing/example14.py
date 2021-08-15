from multiprocessing import Process, Queue

def cube_(numbers,queue):
    for i in numbers:
        queue.put(i**3)
def square(numbers,queue):
    for i in numbers:
        queue.put(i**2)
        
if __name__== "__main__":
    numbers = range(17)
    queue = Queue()
    
    cube_process = Process(target=cube_, args=(numbers,queue))
    square_process = Process(target=square, args=(numbers,queue))
    
    cube_process.start()
    square_process.start()
    
    cube_process.join()
    square_process.join()
    
    while not queue.empty():
        print(queue.get())