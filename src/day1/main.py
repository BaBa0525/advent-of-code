import pathlib
import re

# fmt: off
number_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_regex = f"(?=([0-9]|{"|".join(number_letters)}))"
num_pattern = re.compile(num_regex)
# fmt: on


class Calibration:
    def __init__(self):
        self.calibration_values: list[int] = []

    def parse_num(self, num: str):
        if num.isdigit():
            return int(num)
        else:
            return number_letters.index(num) + 1

    def parse_doc(self, doc: str):
        match = num_pattern.finditer(doc)

        nums = [i[1] for i in match]

        first_digit = self.parse_num(nums[0])
        last_digit = self.parse_num(nums[-1])

        self.calibration_values.append(10 * first_digit + last_digit)

    def sum_calibrations(self):
        return sum(self.calibration_values)


if __name__ == "__main__":
    CUR_DIR = pathlib.Path(__file__).parent.absolute()

    machine = Calibration()

    with open(CUR_DIR / "case.txt", "r") as f:
        docs = f.readlines()

    for doc in docs:
        machine.parse_doc(doc)

    print(machine.sum_calibrations())
