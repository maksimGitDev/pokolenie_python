def print_operation_table(operation, rows, cols):
    result_matrix = [[1 for i in range(cols)] for j in range(rows)]

    for r in range(1, rows+1):
        for c in range(1, cols+1):
            result_matrix[r-1][c-1] = operation(r, c)

    for m in result_matrix:
        print(*m)
