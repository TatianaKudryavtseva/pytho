class Matrix:
    def __init__(self, ls):
        self.ls = ls

    def __str__(self):
        return '\n'.join(map(str, self.ls))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.ls)):
            temp = []
            for j in range(len(other.ls)):
                temp.append(self.ls[i][j] + other.ls[i][j])
            sum_matrix.append(temp)
        return '\n'.join(map(str, sum_matrix))

list_1 = [[1, 3, 5], [7, 5, 4], [3, 9, 5]]
list_2 = [[3, 7, 3], [6, 0, 1], [2, 4, 8]]
matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)


