import time
import concurrent.futures



def take_action(sec):
    print(f'Sleeping {sec} seconds...')
    time.sleep(sec)
    return f'Done sleeping...{sec}'
    
def main():
    seconds = [6,7,2,3,4,5]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(take_action,seconds)      #[executor.submit(take_action,tm ) for tm in seconds]
    
        for result in results:                                       # for f in concurrent.futures.as_completed(results):
            print(result)                                                                 # print(f.result())
            
if __name__ == "__main__":
    main()
 
