from PIL import Image

from shhor_ptor import config
from shhor_ptor.utils.convert_bw import convert_to_bw
from shhor_ptor.utils.misc import get_user_data
from shhor_ptor.utils.plot import plot_shhor_ptor
from shhor_ptor.utils.resize import resize_img, resize_img_keep_ratio

if __name__ == '__main__':

    # get user data
    user_data = get_user_data()

    # get Image object
    img_obj = Image.open(config.input_img_file)

    # resize
    if len(user_data) == 1:
        img_obj = resize_img_keep_ratio(img_obj, user_data[0])
    else:
        img_obj = resize_img(img_obj, user_data[0], user_data[1])

    # bw
    img_obj = convert_to_bw(img_obj)

    # save image
    img_obj.save(config.output_img_file)

    # plot the shhor-ptor diagram # TODO - HURRAY !
    print(plot_shhor_ptor(img_obj))
