import csv

import matplotlib.pyplot as plt

with open('c:\\temp\\pas.csv', 'r') as csvfile:
    tb = []
    r = csv.reader(csvfile)
    for i in r:
        tb.append(i)

print(tb)
# do that every number in the csv will be a number + color code - the one in here is grey, it's good

# colors = [[(0.95, 0.95, 0.95) for c in range(7)] for r in range(8)] # columns, rows
grey = (0.8, 0.8, 0.8)
white = (1, 1, 1)
colors = [[grey if cell != '' else white for cell in row] for row in tb] # colors numbered cells in grey
print(colors)
plt_tbl = plt.table(cellText=tb,
                    loc='upper left',
                    cellLoc='center',
                    # colWidths=7 * [0.04], # width * number of columns
                    cellColours=colors, # colors of allllll cells!
                    bbox=[0.01, 0, 0.8, 0.8] # better than colWidths actually
                    )
plt.axis('off')
plt.show()
