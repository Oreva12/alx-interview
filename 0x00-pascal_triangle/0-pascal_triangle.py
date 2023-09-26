#!/usr/bin/python3
    """0-pascal_triangle.py"""

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for n <= 0

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Build each subsequent row
    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Calculate other elements based on the previous row
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
