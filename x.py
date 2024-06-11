def draw_x(size):
    if size < 3 or size % 2 == 0:
        print("Size must be an odd number greater than or equal to 3.")
        return

    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

#for the X shape
size = 5
draw_x(size)