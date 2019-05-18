from shhor_ptor.config import fill_chr
from shhor_ptor.utils.get_pixels import *

# get the number of blacks in the rows and columns of the image
# [print(i) for i in get_pixel_rows(img_obj)]
# b_rows = get_black_rows(get_pixel_rows(img_obj))
# b_columns = get_black_columns(get_pixel_columns(img_obj))


def fill_row(row, max_row_len, img_width):
    """ fill an array of rows with empty cells, to build the shhor-ptor diagram """
    row_beginning = (max_row_len - len(row)) * [fill_chr]
    row_ending = img_width * [fill_chr]
    return row_beginning + row + row_ending


def columns_to_rows():
    """ convert array of columns, to rows """
    pass


def get_diagram(filled_rows):
    """ build a shhor-ptor diagram using the img_obj """
    pass
