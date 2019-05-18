from PIL import Image


def convert_to_bw(img_obj):
    return img_obj.convert('1') # convert image to black and white - L ? FIXME
