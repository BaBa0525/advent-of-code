import unittest
from main import Calibration


# fmt: off
PART1_CASES = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
PART2_CASES = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
# fmt: on


class CalibrationTestCase(unittest.TestCase):
    def setUp(self):
        self.machine = Calibration()

    def test_part1(self):
        for doc in PART1_CASES:
            self.machine.parse_doc(doc)
        self.assertEqual(self.machine.sum_calibrations(), 142)

    def test_part2(self):
        for doc in PART2_CASES:
            self.machine.parse_doc(doc)
        self.assertEqual(self.machine.sum_calibrations(), 281)


if __name__ == "__main__":
    unittest.main()
