def get_pixel_rows(img_obj):
    """ get arrays of the image pixels. each array is a horizontal line, from left to right """
    img_width = img_obj.size[0]
    img_pixels = list(img_obj.getdata())
    return [img_pixels[i * 20:i * 20 + 20] for i in range(img_width)]


def get_pixel_columns(img_obj):
    """ get arrays of the image pixels. each array is a vertical line, from up to down """
    pixel_rows = get_pixel_rows(img_obj)
    return [[pixel_rows[row_num][column_num] for row_num in range(len(pixel_rows))] for column_num in range(img_obj.size[0])]


def _get_bws_from_pixel_array(pixel_arrays):
    """
    get bw strings of the pixel arrays
    [255, 255, 255, 0, 255, 0, 0] ---> "wwwbwbb" ---> ['b', 'bb'] ---> [1, 2]
    """
    return [[len(i) for i in (''.join([('w' if val == 255 else 'b') for val in row])).split('w') if i != ''] for row in pixel_arrays]


def get_black_rows(pixel_rows):
    """
    get bw strings of the pixel rows of the image
    """
    return _get_bws_from_pixel_array(pixel_rows)


def get_black_columns(pixel_columns):
    """
    get bw strings of the pixel columns of the image
    """
    return _get_bws_from_pixel_array(pixel_columns)
