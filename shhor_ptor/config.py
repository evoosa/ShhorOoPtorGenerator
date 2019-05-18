from os.path import join

output_dir = "C:\\temp"

img_name = "poop"

input_img = "{}.png".format(img_name)

output_img = "done_{}.png".format(img_name)

input_img_file = join(output_dir, input_img)

output_img_file = join(output_dir, output_img)

# will be used to fill the rows in order to build a shhor-ptor diagram
fill_chr = ''

# plotting configuration
grey = (0.8, 0.8, 0.8)
white = (1, 1, 1)
