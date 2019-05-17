from PIL import Image
import os

dir = "C:\\temp"
img_name = "fitted.jpg"

output_img = "resized.png"

input_img = os.path.join(dir, img_name)

choice = input("save ratio? n/y: ")
height = int(input("height: "))
width = int(input("width: "))

if choice == "n":
    # don't keep ratio
    image = Image.open(input_img)
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(os.path.join(dir, output_img))

elif choice == "y":
    # keep ratio. relying on the wanted height.
    image = Image.open(input_img)
    wpercent = (width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((width, hsize), Image.ANTIALIAS)
    image.save(os.path.join(dir, output_img))


