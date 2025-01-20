from unittest import TestCase
from script_4 import move

# The provided game state is valid if:
# ... it only contains the defined characters (" ", "#", "o").
# ... each line has same length.
# ... it contains exactly one player.
# ... it has a sensible size (both dimensions are greater than 0).
# ... at least one move is possible.


class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        # uncomment the following line once you've implemented move
        # self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("left", "right", "down")
        )
        # uncomment the following line once you've implemented move
        # self.assertEqual(expected, actual)
