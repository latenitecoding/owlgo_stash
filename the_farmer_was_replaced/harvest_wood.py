from __builtins__ import *
from _farming_novice import *

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

def main():
    while True:
        if not farm_plot_alt(4, 4, [Entities.Tree, Entities.Bush]):
            clear_plot(4, 4)
            return

        move(East)

        if not farm_plot_alt(2, 2, [Entities.Tree, Entities.Bush]):
            clear_plot(2, 2, 4, 0)
            return

        go_home()

    return


if __name__ == "__main__":
    main()

