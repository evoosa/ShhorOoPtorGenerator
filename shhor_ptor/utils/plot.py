import matplotlib.pyplot as plt

from shhor_ptor.config import grey, white
from shhor_ptor.utils.diagram import get_diagram

numbers_color = grey
cell_color = white


def get_cell_colors(diagram, img_width, img_height):
    """ get the plot cell colors from the diagram """

    cell_colors = []
    for i in range(len(diagram)):
        row = diagram[i]
        # if the row is a row of numbers (not for filling), turn it grey
        if i < (len(diagram) - img_height):
            cell_colors.append(len(row) * [grey])
        else:
            row_colors = []
            row_colors += (len(row) - img_width) * [grey]
            row_colors += img_width * [white]
            cell_colors.append(row_colors)
    return cell_colors


def plot_shhor_ptor(img_obj):
    """ plot the damn shhor ptor ! """

    diagram = get_diagram(img_obj)
    img_width = img_obj.size[0]
    img_height = img_obj.size[1]
    cell_colors = get_cell_colors(diagram, img_width, img_height)

    plt.table(cellText=diagram,
                        loc='center',
                        cellLoc='center',
                        colWidths=len(diagram[0]) * [0.025], # width * number of columns
                        cellColours=cell_colors, # colors of allllll cells!
                        )
    plt.axis('off')
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()
