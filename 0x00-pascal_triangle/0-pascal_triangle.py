def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize Pascal's triangle with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Calculate each element of the row based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
