import time 
from PIL import Image, ImageFilter
import concurrent.futures

image_names = [
    "photp-12-34555.jpg",
    "photo-12-12345.jpg",
    "photo-aqw233.jpg",
    "photo-azxcd.123.jpg",
    "photo-asde345.jpg"
]


size = (1200, 1200)

def process_img(img_name):
    
    img = Image.open(img_name)
    
    img = img.filter(ImageFilter.GaussianBlur(15))
    
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_img, image_names)
    
