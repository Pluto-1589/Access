class MagicDrawingBoard:
    def __init__(self, x, y):

        if x < 1:
            raise ValueError("Invalid input, must be greater than 0")
        if y < 1:
            raise ValueError("Invalid input, must be greater than 0")

        self.x = x
        self.y = y
        self.board = [[0 for _ in range(x)] for _ in range(y)]

    def pixel(self, coordinate: tuple):
        # You implementation should have two methods to draw on the board. pixel just fills the pixel at the x/y tuple that is provided as the argument.
        x, y = coordinate

        if not (0 <= x < self.x and 0 <= y < self.y):
            raise ValueError("Out of bound coordinates")
        else:
            self.board[x][y] = 1

            return 1

    def rect(self, top_left: tuple, bottom_right: tuple):
        # fills a rectangle that is spanned by the two x/y coordinate tuples. The rectangle must be "positive", i.e., the end coordinates must be to the lower right of the start coordinates.
        x1, y1 = top_left
        x2, y2 = bottom_right

        if x2 <= x1 or y2 <= y1:
            raise ValueError(
                "Coordinates must be greater than start coordinates")

        if not (0 <= x1 < self.x and 0 <= y1 < self.y):
            raise ValueError("Top left coordinates are out of bounds")

        if not (0 < x2 <= self.x and 0 < y2 <= self.y):
            raise ValueError("Bottom right coordinates are out of bounds")

        for row in range(y1, y2):
            for column in range(x1, x2):
                self.board[row][column] = 1

    def img(self):
        return "\n".join("".join(str(cell) for cell in row)for row in self.board)

    def reset(self):
        # A call to reset should clear the entire board. The board size itself is provided in the constructor.
        self.board = [[0 for _ in range(self.x)] for _ in range(self.y)]

        return self.board


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(1, 1)
    # db.pixel((-1,0))


db = MagicDrawingBoard(6, 4)  # instantiation of a specific size
print(db.pixel((1, 1)))  # draw at one coordinate
print(db.rect((2, 2), (5, 4)))  # draw a rectangle
img = db.img()
print(img)  # return the drawn image
db.reset()  # reset the field again
