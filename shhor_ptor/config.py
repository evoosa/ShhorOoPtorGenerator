from os.path import join

output_dir = "C:\\temp"

img_name = "dino"

img_file_name = "{}.jpg".format(img_name)

output_img = "done_{}.png".format(img_name)

input_img = join(output_dir, img_file_name)
