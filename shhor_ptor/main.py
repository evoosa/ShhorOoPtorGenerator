from PIL import Image

from shhor_ptor import config
from shhor_ptor.utils.convert_bw import convert_to_bw
from shhor_ptor.utils.get_pixels import get_pixel_arrays
from shhor_ptor.utils.misc import get_user_data
from shhor_ptor.utils.resize import resize_img, resize_img_keep_ratio

if __name__ == '__main__':

    # get user data
    save_ratio, width, height = get_user_data()

    # get  Image object
    img_obj = Image.open(config.input_img_file)

    # resize
    if save_ratio:
        img_obj = resize_img_keep_ratio(img_obj, width)
    else:
        img_obj = resize_img(img_obj, width, height)

    # bw
    img_obj = convert_to_bw(img_obj)

    # save image
    img_obj.save(config.output_img_file)

    # get pixel arrays from image
    pixel_arrays = get_pixel_arrays(img_obj)
    for i in pixel_arrays:
        print(i)
