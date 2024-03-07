#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1
        if i > 0:
            prev_row = triangle[-1]  # Get the previous row
            for j in range(1, i):
                # Calculate each element in the current row
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
