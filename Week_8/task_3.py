class Matrix:

    def __init__(self, matrix: list) -> None:

        # It contains exactly 2 dimensions.
        # checks if is a list of lists
        assert isinstance(matrix, list) and all(isinstance(row, list)
                                                for row in matrix), "Matrix needs to be of dimension 2"

        # All nested lists have the same length.
        row_length = next(len(row) for row in matrix if len(row) > 0)
        assert all(
            len(row) == row_length for row in matrix), "All rows must have the same length."

        # There has to be at least one non-empty row (in other words: [[]] would be invalid).
        assert len(matrix) > 0 and len(
            matrix[0]) > 0, "at least one non-empty row"

        # All values contained in nested lists are integers and/or floats.
        assert all(isinstance(scalar, (int, float))
                   for row in matrix for scalar in row), "All values in nested lists need to be integers and/or floats."

        self.__matrix = matrix

    def shape(self):

        return len(self.__matrix), len(self.__matrix[0]) if self.__matrix else 0

    def __add__(self, other):
        # Implement __add__ so that two instances of class Matrix can be added via the + operator.

        if not isinstance(other, Matrix):
            return NotImplemented

        assert self.shape() == other.shape(), "Matrices must have same shape to add"

        res = [[self.__matrix[i][j] + other.__matrix[i][j]]
               for j in range(len(self.__matrix[0]))for i in range(len(self.__matrix))]

        return Matrix(res)

    def __mul__(self, other):
       # Implement __mul__ so that two instances of class Matrix can be multiplied via the * operator.

        if not isinstance(other, Matrix):
            return NotImplemented

        assert self.shape() == other.shape, "Matrices must have same shape to multiply"

        res = [[self.__matrix[i][j] * other.__matrix[i][j]]
               for j in range(len(self.__matrix[0]))for i in range(len(self.__matrix))]

        return Matrix(res)

    def __eq__(self, other: object) -> bool:
        # Implement __eq__ so that two instances of class Matrix can be compared via the == operator.
        return isinstance(other, Matrix) and self.__matrix == other.__matrix

    def __hash__(self) -> int:
        # Implement __hash__ so that instances of class Matrix can be used as dictionary keys
        return hash(tuple(tuple(row for row in self.__matrix)))

    def __str__(self):

        return "\n".join(["[" + ", ".join(map(str, row)) + "]" for row in self.__matrix])


matrix = Matrix([[1, 2],
                 [3, 4]])
matrix_2 = Matrix([[6, 7],
                   [9, 8]])

print(matrix.__add__(matrix_2))
