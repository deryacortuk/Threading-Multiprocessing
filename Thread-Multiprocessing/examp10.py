from multiprocessing import Process,current_process
import os
def cube(number):
    result = number**3
    process_id = os.getpid()
    print(f'process ID: {process_id}')
    process_name = current_process().name
    print(f'process name: {process_name} ')
    print(f'The number {number} cube to {result}.')

if __name__=="__main__":
    number_list = []
    numbers = [2,3,5,7,11,13,17]
    
    for number in numbers:
        process = Process(target=cube,args = (number,))
        number_list.append(process)
        
        process.start()
   