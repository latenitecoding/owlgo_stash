from __builtins__ import *
from _farmhand import *

# REPLACES 08_program.py

# This program provides an option
# to farm any necessary Wood.

# [x] Needs 18x harvest() every 10800 ticks
# - Speed: 3037.5 ticks per second
# - Growth (Tree): 3.5 s, or 10631.25 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# Note: Farming a plot around the mean growth of
# a plant is most efficient when the growth rate
# of the plant is reduced by half. This requires
# additional Water up front, but the same amount
# of Water to maintain as the typical farming
# approach for mean growth. Farming 18x cells
# is the most efficient in this case for Wood, so
# we use two adjacent plots of 4x4 and 2x2. Our approach
# to mean growth farming is to Water a cell when it
# can't be harvested. As such, decreasing the plot size
# naturally pushes cells to receive more Water.
PLOTS = [[4, 4], [2, 2]]


def main():
    go_home()

    while farm_plots(PLOTS, [[Entities.Tree, Entities.Bush]]):
        go_home()

    clear_plots(PLOTS)


if __name__ == "__main__":
    main()
