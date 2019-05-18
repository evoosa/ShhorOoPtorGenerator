from PIL import Image


def resize_img_keep_ratio(img_obj, width, height):
    """ resize image, keep ratio. relying on the wanted height """
    wpercent = (width / float(img_obj.size[0]))
    hsize = int((float(img_obj.size[1]) * float(wpercent)))
    return img_obj.resize((width, hsize), Image.ANTIALIAS)

def resize_img(img_obj, width, height):
    """ resize image, don't keep ratio """
    return img_obj.resize((width, height), Image.ANTIALIAS)
