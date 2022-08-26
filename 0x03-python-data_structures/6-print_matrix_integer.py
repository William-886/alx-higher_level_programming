def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        my_string = ' '.join(map(str, item))
        print("{}".format(my_string))
