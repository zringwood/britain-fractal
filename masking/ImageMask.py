from PIL import Image
from PIL import ImageEnhance

im = Image.open('greatbritain.webp')
# Convert to grayscale for easier processing
im_gr = im.convert("L")
mask = ImageEnhance.Contrast(im_gr)
#By converting to greyscale and increasing the contrast an arbitrary amount, we get a 
# black-and-white image that can serve as a key for determining the coastline of great britain. 
#Some manual correction is still needed. 
mask.enhance(3000).save("mask.png")
