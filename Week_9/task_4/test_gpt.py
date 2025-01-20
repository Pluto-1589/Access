#!/usr/bin/env python3
from unittest import TestCase
from task.script import move


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
        self.assertEqual(expected, actual)

    def test_move_up(self):
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
                "###  o #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        self.assertEqual(expected, actual)

    def test_invalid_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "diagonal")
        self.assertEqual(str(context.exception), "Invalid direction: diagonal")

    def test_invalid_state_characters(self):
        state = (
            "#####   ",
            "###x   #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "right")
        self.assertIn("invalid characters", str(context.exception))

    def test_multiple_players(self):
        state = (
            "#####   ",
            "###o   #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "right")
        self.assertIn("exactly one player", str(context.exception))

    def test_no_possible_moves(self):
        state = (
            "#####   ",
            "###### #",
            "#   o###",
            "   #####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "right")
        self.assertIn("Invalid move", str(context.exception))
