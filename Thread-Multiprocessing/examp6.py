import requests
import time
import concurrent.futures

urls = [
    "https://unsplash.com/photos/X0y-PB-3emw",
     "https://unsplash.com/photos/V72xxgvew-A",
     "https://unsplash.com/photos/5QJEIR7D018",
    "https://unsplash.com/photos/2UAX18QFEjQ",    
    "https://unsplash.com/photos/wdUjA_RN-p0",
    "https://unsplash.com/photos/4mmMstrqt-k",
    "https://unsplash.com/photos/jGibIXR2NVE"    
]

time1 = time.perf_counter()

def download_image(img_url):
    image_bytes = requests.get(img_url).content
    image_name = img_url.split('/')[3]
    image_name = f'{image_name}.jpg'
    
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print('f{image_name} was downloaded.')
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, urls)
    
        
time2 = time.perf_counter()

print(f'Finished in {time2-time1} seconds')