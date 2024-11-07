matrix = [["a", "d", "g"],
            ["b", "e", "h"],
            ["c", "f", "i"]]

index_row = 0
index_col = 0
cur_col = [None, None, None]
for _ in range(9):
    num = matrix[index_row][index_col]
    cur_col[index_row] = num

    index_row += 1
    if index_row % 3 == 0:
        


        index_col += 1
        index_row = 0

    


    #if all(map(lambda x: x == 1, [matrix[0][0], matrix[1][0], matrix[2][0]]))