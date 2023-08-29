def matrix_divided(matrix, div):
    """ divides matrix by input divisor"""
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    new = []
    for row in matrix:
        # This line creates a new list to store the elements of the current row,
        # after dividing them by the divisor.
        sub = [round((i / div), 2) for i in row]
        new.append(sub)
    # This line returns the new list of rows.
    return new
