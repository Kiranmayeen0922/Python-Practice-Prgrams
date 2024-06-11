def generate_triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            print(j, end="")
        print()
# rows for the triangle
rows = 5
generate_triangle(rows)