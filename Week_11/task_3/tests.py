#!/usr/bin/env python3
import unittest
from HS24.INF.ACCESS.Week_11.task_3.script import evolve


class TestEvolveFunction(unittest.TestCase):
    def test_valid_world(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        expected = (
            "--------------",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "|            |",
            "--------------"
        )
        result_world, populated_count = evolve(world, 4)
        self.assertEqual(result_world, expected)
        self.assertEqual(populated_count, 5)

    def test_invalid_world_type(self):
        with self.assertRaises(Warning) as context:
            evolve(["---", "|#|", "---"], 1)
        self.assertIn(
            "Invalid input: world must be a tuple of strings.", str(context.exception))

    def test_invalid_world_size(self):
        world = (
            "------",
            "|    |",
            "------"
        )
        with self.assertRaises(Warning) as context:
            evolve(world, 1)
        self.assertIn("Invalid input: world rows must have the same length and be at least 3x3.", str(
            context.exception))

    def test_invalid_characters(self):
        world = (
            "--------------",
            "|  ###       |",
            "|  $         |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning) as context:
            evolve(world, 1)
        self.assertIn(
            "Invalid input: world contains invalid characters.", str(context.exception))

    def test_invalid_steps(self):
        world = (
            "--------------",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning) as context:
            evolve(world, -1)
        self.assertIn(
            "Invalid input: steps must be a positive integer.", str(context.exception))

    def test_edge_cases(self):
        # Single step evolution
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|            |",
            "|            |",
            "--------------"
        )
        expected = (
            "--------------",
            "|            |",
            "|   #        |",
            "|  # #       |",
            "|            |",
            "--------------"
        )
        result_world, populated_count = evolve(world, 1)
        self.assertEqual(result_world, expected)
        self.assertEqual(populated_count, 3)


if __name__ == "__main__":
    unittest.main()
