from pathlib import Path
import unittest
from main import part1, part2


class TestDay2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cur_dir = Path(__file__).parent

    def test_part1(self):
        with open(self.cur_dir / "example.txt", "r") as input_file:
            inputs = input_file.readlines()
            self.assertEqual(part1(inputs), 8, msg="Example 1 failed")

        with open(self.cur_dir / "case.txt", "r") as input_file:
            inputs = input_file.readlines()
            self.assertEqual(part1(inputs), 2685, msg="Case 1 failed")

    def test_part2(self):
        with open(self.cur_dir / "example.txt", "r") as input_file:
            inputs = input_file.readlines()
            self.assertEqual(part2(inputs), 2286, msg="Example 2 failed")

        with open(self.cur_dir / "case.txt", "r") as input_file:
            inputs = input_file.readlines()
            self.assertEqual(part2(inputs), 83707, msg="Case 2 failed")


if __name__ == "__main__":
    unittest.main()
