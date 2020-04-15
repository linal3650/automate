tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData, rightWidth):
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len(max(tableData[i], key=len))

    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(rightWidth), end='')
        print()


printTable(tableData, 8)


