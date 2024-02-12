import re
from pathlib import Path
from typing import Literal


class Game:
    def __init__(self, info: str, nth: int):
        self.info = info
        self.nth = nth

        self.red_reg = re.compile(r"(\d+) red")
        self.blue_reg = re.compile(r"(\d+) blue")
        self.green_reg = re.compile(r"(\d+) green")

    def get_max(self, color: Literal["red", "blue", "green"]):
        match color:
            case "red":
                return max(map(int, self.red_reg.findall(self.info)))
            case "blue":
                return max(map(int, self.blue_reg.findall(self.info)))
            case "green":
                return max(map(int, self.green_reg.findall(self.info)))
            case _:
                raise ValueError("Invalid color")

    @classmethod
    def from_line(cls, line: str):
        game, info = line.split(":")
        nth = int(game.split(" ")[1])

        return cls(info, nth)


def part1(inputs: list[str]):
    total = 0

    for line in inputs:
        game = Game.from_line(line)

        red_max = game.get_max(color="red")
        if red_max > 12:
            continue

        green_max = game.get_max(color="green")
        if green_max > 13:
            continue

        blue_max = game.get_max(color="blue")
        if blue_max > 14:
            continue

        total += game.nth

    return total


def part2(inputs: list[str]):
    total = 0

    for line in inputs:
        game = Game.from_line(line)

        mult = (
            game.get_max(color="red")
            * game.get_max(color="green")
            * game.get_max(color="blue")
        )

        total += mult

    return total


if __name__ == "__main__":
    CUR_DIR = Path(__file__).parent

    with open(CUR_DIR / "case.txt", "r") as input_file:
        lines = input_file.readlines()

    print(part1(inputs=lines))
    print(part2(inputs=lines))
