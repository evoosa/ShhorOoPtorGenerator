

def get_user_data():
    save_ratio = input("save ratio? n/y: ")
    save_ratio = True if save_ratio == "y" else False
    height = int(input("height: "))
    width = int(input("width: "))
    return save_ratio, width, height

