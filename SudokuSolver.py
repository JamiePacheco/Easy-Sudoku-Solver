

def solver(puzzle):

    def Check_Row(row):
        missing = []
        for x in range(0, 10):
            if x not in puzzle[row]:
                missing.append(x)
        
        return missing

    def Check_Column(column):

        i = 0
        Inside_Column = []
        while i < 9:
            if puzzle[i][column] != 0:
                Inside_Column.append(puzzle[i][column])
            i += 1
        
        return Inside_Column

    def Check_Square(column, row):
        
        if column in range(0, 3):
            c_range = (0, 3)
        elif column in range(3, 6):
            c_range = (3, 6)
        elif column in range(6, 9):
            c_range = (6, 9)

        if row in range (0, 3):
            r_range = (0, 3)
        elif row in range (3, 6):
            r_range = (3, 6)
        elif row in range (6, 9):
            r_range = (6, 9)

        Inside_Square = []
        for x in range(r_range[0], r_range[1]):
            for y in range(c_range[0], c_range[1]):
                if puzzle[x][y] != 0:
                    Inside_Square.append(puzzle[x][y])

        return Inside_Square

    def comparing(c, r):

        possible_values = []
        Square_Checked = Check_Square(c, r)
        Column_Checked = Check_Column(c)
        Row_Checked = Check_Row(r)

        if puzzle[r][c] == 0:
            for x in range(0, len(Row_Checked)):
                if Row_Checked[x] not in Column_Checked and Row_Checked[x] not in Square_Checked:
                    possible_values.append(Row_Checked[x]) 

        return possible_values

    while 0 in puzzle[0] or 0 in puzzle[1] or 0 in puzzle[2]or 0 in puzzle[3]or 0 in puzzle[4]or 0 in puzzle[5]or 0 in puzzle[6]or 0 in puzzle[7]or 0 in puzzle[8]:
        for x in range(0,9):
            for y in range(0,9):
                result = comparing(y, x)

                if int(len(result)) == 1:
                    puzzle[x][y] = result[0]
                else:
                    continue

    for x in range(0,9):
        print(puzzle[x])


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


solver(puzzle)