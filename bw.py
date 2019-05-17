from PIL import Image
import os

dir = "C:\\Users\\evoosa\\Desktop\\"
img_name = "illumaor.png"
img = os.path.join(dir, img_name)
# comes BEFORE resizing!!!

image = Image.open(img)
image = image.convert('L') # convert image to black and white
image.save(os.path.join(dir, "fitted.jpg"))
