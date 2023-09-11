def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate through the rows in the input matrix
    for row in matrix:
        # Create a new row for the squared_matrix
        squared_row = []
        
        # Iterate through the elements in the current row and square each value
        for element in row:
            squared_row.append(element ** 2)
        
        # Append the squared_row to the squared_matrix
        squared_matrix.append(squared_row)
    
    return squared_matrix
