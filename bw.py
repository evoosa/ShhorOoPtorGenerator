from PIL import Image
import os

dir = "C:\\temp"
img_name = "resized.png"
img = os.path.join(dir, img_name)
# comes BEFORE resizing!!!

image = Image.open(img)
image = image.convert('1') # convert image to black and white
image.save(os.path.join(dir, "fitted.jpg"))
