class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result

    def __str__(self):
        # for i in range(len(self.matrix)):
        #     for j in range(len(self.matrix[i])):
        #         print(str(self.matrix[i][j]), end=' ')
        #     print()
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

matrix1= Matrix([[1,2],[3,4],[5,6]])
matrix2 = Matrix([[7,8],[9,10],[11,12]])
print(matrix1)