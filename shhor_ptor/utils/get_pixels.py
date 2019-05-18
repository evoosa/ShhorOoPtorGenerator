from PIL import Image

def get_pixel_arrays(img_obj):
    """ get arrays of the image pixels. each array is a horizontal line, from left to right """
    img_width = img_obj.size[0]
    img_pixels = list(img_obj.getdata())
    return [img_pixels[i * 20:i * 20 + 20] for i in range(img_width)]


def get_pixel_columns(img_obj):
    """ get arrays of the image pixels. each array is a vertical line, from up to down """
    pixel_arrays = get_pixel_arrays(img_obj)
    return [[pixel_arrays[array_num][column_num] for array_num in range(len(pixel_arrays))] for column_num in range(img_obj.size[0])]

def get_black_arrays():
    pass


def get_black_columns():
    pass
