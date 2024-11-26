def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.extend(list_)
        for j in range(m):
            list_.insert(j, value)
    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)
