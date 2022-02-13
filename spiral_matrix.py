def spiralTraverse(array: list):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    num = 1
    while start_col <= end_col and start_row <= end_row:
        if num == 1:
            for i in range(start_col, end_col):
                result.append(array[start_row][i])
                num += 1
                start_row += 1
        if num == 2:
            for i in range(start_row + 1, end_row + 1):
                result.append(array[i][end_col])
                num += 1
                end_col -= 1
        if num == 3:
            for i in reversed(range(end_row, end_col)):
                result.append(array[i][end_row])
                num += 1
                end_row -= 1
        if num == 4:
            for i in reversed(range(start_col, end_row)):
                result.append(array[i][start_col])
                num = 1

    return result
