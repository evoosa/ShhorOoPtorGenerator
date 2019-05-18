from PIL import Image


def resize_img_keep_ratio(img_obj, width):
    """ resize image, keep ratio. relying on the wanted width """
    width_percentage = (width / float(img_obj.size[0]))
    calculated_height = int((float(img_obj.size[1]) * float(width_percentage)))
    return img_obj.resize((width, calculated_height), Image.ANTIALIAS)


def resize_img(img_obj, width, height):
    """ resize image, don't keep ratio """
    return img_obj.resize((width, height), Image.ANTIALIAS)
