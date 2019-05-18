import os

from PIL import Image

from shhor_ptor import config
from shhor_ptor.utils.convert_bw import convert_to_bw
from shhor_ptor.utils.misc import get_user_data
from shhor_ptor.utils.resize import resize_img, resize_img_keep_ratio

if __name__ == '__main__':

    # get user data
    save_ratio, width, height = get_user_data()

    # get  Image object
    img_obj = Image.open(config.input_img)

    # resize
    if save_ratio:
        img_obj = resize_img_keep_ratio(img_obj, width, height)
    else:
        img_obj = resize_img(img_obj, width, height)

    # bw
    img_obj = convert_to_bw(img_obj)

    # save image
    img_obj.save(os.path.join(config.output_dir, config.output_img))
