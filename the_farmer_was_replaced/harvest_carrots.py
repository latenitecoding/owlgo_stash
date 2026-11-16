from __builtins__ import *
from _farming_novice import *

# REPLACES 10_program.py

# This program provides an option
# to farm any necessary Carrots.

# [x] Needs 16x harvest() every 9600 ticks
# - Speed: 3037.5 ticks per second
# - Growth (Carrots): 3.0 s, or 9112.5 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# Note: Farming a plot around the mean growth of
# a plant is most efficient when the growth rate
# of the plant is reduced by half. This requires
# additional Water up front, but the same amount
# of Water to maintain as the typical farming
# approach for mean growth. Farming 16x cells
# is the most efficient in this case for Carrots, so
# we use two adjacent plots of 4x3 and 2x2. Our approach
# to mean growth farming is to Water a cell when it
# can't be harvested. As such, decreasing the plot size
# naturally pushes cells to receive more Water.

def main():
    while True:
        if not farm_plot(4, 3, Entities.Carrot):
            clear_plot(4, 3)
            return

        move(East)

        if not farm_plot(2, 2, Entities.Carrot):
            clear_plot(2, 2, 4, 0)
            return

        go_home()

    return


if __name__ == "__main__":
    main()

