def get_pixel_arrays(img_obj):
    """ get arrays of the image pixels. each array is a horizontal line, from left to right """
    img_width = img_obj.size[0]
    img_pixels = list(img_obj.getdata())
    return [img_pixels[i * 20:i * 20 + 20] for i in range(img_width)]
