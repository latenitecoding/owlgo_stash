from __builtins__ import *
from _farmhand import *

# REPLACES 06_program.py

# This program provides an option
# to farm any necessary Hay.

# [x] Needs 1x harvest() every 400 ticks
# - Speed: 3037.5 ticks per second
# - Growth (Grass): 0.5 s, or 1518.75 ticks
# - harvest(): 200 ticks
# - move(): 200 ticks
# Note: A 2x2 plot of 4x cells is the most
# efficient means for havesting Hay at the
# drone's max Speed without Power.
PLOT = [2, 2]


def main():
    while farm_plot(PLOT, [Entities.Grass], [0, 0]):
        continue


if __name__ == "__main__":
    main()
