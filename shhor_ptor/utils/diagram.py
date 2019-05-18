from shhor_ptor.config import fill_chr


# get the number of blacks in the rows and columns of the image
# [print(i) for i in get_pixel_rows(img_obj)]
# b_rows = get_black_rows(get_pixel_rows(img_obj))
# b_columns = get_black_columns(get_pixel_columns(img_obj))


def fill_row(row, max_row_len, img_width):
    """ fill an array of rows with empty cells, to build the shhor-ptor diagram """
    row_beginning = (max_row_len - len(row)) * [fill_chr]
    row_ending = img_width * [fill_chr]
    return row_beginning + row + row_ending


def columns_to_rows(b_columns, max_row_len):
    """ convert array of columns, to rows - READY TO BE PUSHED TO THE DIAGRAM"""
    longest_col_len = len(max(b_columns, key=len))
    for i in range(len(b_columns)):
        col = b_columns[i]
        filling = (longest_col_len - len(col)) * [fill_chr]
        b_columns[i] = filling + col
    return [(max_row_len * [fill_chr] + [col[j] for col in b_columns]) for j in range(longest_col_len)]


b_cols = [[], [], [], [], [2], [1], [1], [1], [2], [2], [2], [1], [3], [1, 1], [2, 1], [2, 1], [4], [2, 1], [2, 2], [4, 1], [5], [1, 1, 2], [3, 3], [4, 2], [1, 2, 2], [4, 2], [1, 2, 2], [5, 2]]
a = columns_to_rows(b_cols, 5)
for i in a:
    print(len(i))


def get_diagram(filled_rows):
    """ build a shhor-ptor diagram using the img_obj """
    pass
