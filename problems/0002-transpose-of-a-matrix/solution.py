# Cell 1
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    pass
    a_tr = []
    for i in range(len(a[0])):
        a_tr.append([])
        for j in range(len(a)):
            a_tr[i].append(a[j][i])


    return a_tr