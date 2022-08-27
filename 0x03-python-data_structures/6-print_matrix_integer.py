def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        a = 0
        b = len(item) - 1
        for c in item:
            if a < b:
                print("{} ".format(c), end="")
            else:
                print("{}".format(c), end="")
            a += 1
        print()
