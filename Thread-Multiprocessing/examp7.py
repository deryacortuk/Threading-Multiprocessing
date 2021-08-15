import multiprocessing
from multiprocessing.spawn import freeze_support
import time


start = time.perf_counter()

def cube(x):
    print(x**3)
    time.sleep(1)
    print('Wake up!!!')
    
p1 = multiprocessing.Process(target=cube, args=(7,))
p2 = multiprocessing.Process(target=cube, args=(17,))

p1.start()
p2.start()

p1.join()
p2.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

