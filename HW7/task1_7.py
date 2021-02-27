class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([str(i) for i in self.matrix])

    def __add__(self, other):
        result = [[0 for a in range(len(self.matrix))] for b in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return f"{result}"


m = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
f = Matrix([[11, 11, 11], [22, 22, 22], [33, 33, 33]])
print(m.matrix)
print(m)
print(m +f)
