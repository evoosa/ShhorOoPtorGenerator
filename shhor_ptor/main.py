from PIL import Image

from shhor_ptor import config
from shhor_ptor.utils.convert_bw import convert_to_bw
from shhor_ptor.utils.get_pixels import get_black_columns, get_black_rows, get_pixel_columns, get_pixel_rows
from shhor_ptor.utils.misc import get_user_data
from shhor_ptor.utils.resize import resize_img, resize_img_keep_ratio
from shhor_ptor.utils.diagram import fill_rows

if __name__ == '__main__':

    # get user data
    user_data = get_user_data()

    # get  Image object
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

    # get the number of blacks in the rows and columns of the image
    # [print(i) for i in get_pixel_rows(img_obj)]
    b_rows = get_black_rows(get_pixel_rows(img_obj))
    b_columns = get_black_columns(get_pixel_columns(img_obj))

    a = fill_rows(b_rows, img_obj.size[0])
    for i in a:
        print(i)
