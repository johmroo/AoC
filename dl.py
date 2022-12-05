from aocd import get_data
import argparse

parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
parser.add_argument("year",type=int, help="The year to run.")
parser.add_argument("day",type=int, help="The day to run.")
args = parser.parse_args()

year = args.year
day = args.day
with open(f"{year}/day{day:02}.txt", "w") as f:
    f.write(get_data(day=day, year=year))
