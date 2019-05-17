from PIL import Image
import os

def resize_img(img_obj, save_ratio, width, height):
    if save_ratio == "n":
        # don't keep ratio
        img_obj.resize((width, height), Image.ANTIALIAS)

    elif save_ratio == "y":
        # keep ratio. relying on the wanted height.
        wpercent = (width / float(img_obj.size[0]))
        hsize = int((float(img_obj.size[1]) * float(wpercent)))
        img_obj.resize((width, hsize), Image.ANTIALIAS)


def convert_to_bw(img_obj):
    img_obj.convert('1') # convert image to black and white - L ? FIXME


def get_user_data():
    save_ratio = input("save ratio? n/y: ")
    height = int(input("height: "))
    width = int(input("width: "))
    return save_ratio, width, height


if __name__ == "__main__":

    # configure
    dir = "C:\\temp"
    name = "poop"
    img_name = "{}.png".format(name)
    output_img = "done_{}.png".format(name)
    input_img = os.path.join(dir, img_name)

    # get user data
    save_ratio, width, height = get_user_data()

    # get  Image object
    img_obj = Image.open(input_img)

    # resize
    resize_img(img_obj, save_ratio, width, height)

    # convert to black and white
    convert_to_bw(img_obj)

    # save image
    img_obj.save(os.path.join(dir, output_img))
