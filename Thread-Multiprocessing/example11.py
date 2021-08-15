from multiprocessing import Process, current_process
import os
import time

def square(num):
    for number in num:
        result = number**2
        time.sleep(1)
        process_id = os.getpid()
        print(f'Process ID: {process_id}')
    
        process_name = current_process().name
        print(f'process name: {process_name}')
    
        print(f'The number {number} squares to {result}')
    
if __name__ =="__main__":
    processes = list()
    numbers = range(20)
    for i in range(18):
        process = Process(target=square, args=(numbers,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
           
print(f'Process is over!')