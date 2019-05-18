from os.path import join

output_dir = "C:\\temp"

img_name = "dino"

input_img = "{}.jpg".format(img_name)

output_img = "done_{}.png".format(img_name)

input_img_file = join(output_dir, input_img)

output_img_file = join(output_dir, output_img)