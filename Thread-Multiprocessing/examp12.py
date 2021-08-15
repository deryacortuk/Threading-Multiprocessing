from multiprocessing import Pool
import time


def square(number):
    start = time.perf_counter()
    result = 0
    
    for i in range(number+1):
        result += i**2
    finish = time.perf_counter()   
    print(f'{finish-start} seconds') 
    return result

 

if __name__== "__main__":
    numbers = range(17)
    pool = Pool()
    result = pool.map(square,numbers)
    print(result)
    
    pool.close()
    pool.join()