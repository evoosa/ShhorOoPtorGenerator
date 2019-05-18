

def get_user_data():
    save_ratio = input("save ratio? n/y: ")
    save_ratio = True if save_ratio == "y" else False

    width = int(input("width: "))
    if not save_ratio:
        height = int(input("height: "))
        return [width, height]
    else:
        return [width]

