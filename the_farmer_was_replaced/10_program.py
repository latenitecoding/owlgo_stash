from __builtins__ import *

# REPLACES 07_program.py

# This is the tenth program. Use it
# to unlock the following upgrades:
# - Carrots II/III/IV
# - Grass III/IV
# - Watering II/III/IV
# - * Expand IV
# Note: You'll need to use 09_program.py to
# harvest the necessary Hay, and 11_program.py
# to harvest any necessary Carrots
# * Wait to unlock last

# [x] Needs 16x harvest() every 9600 ticks
# - Speed: 1350 ticks per second
# - Growth (Tree): 7.0 s, or 9450 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: We can harvest 8/8x Tree/Bush every 9600 ticks,
# which is as close to the mean-grow time of a Tree.
# Since this is still less than the max-grow time, the
# additional 150 ticks that the drone waits will still
# give more Trees and Bushes time to grow.

while True:
    for x in range(4):
        for y in range(4):
            if can_harvest():
                harvest()
            elif (
                    get_water() < 7 * 0.01 + 1.4 / 7
                    and num_items(Items.Water) > 0
                    and (x * 4 + y) % 2 == 0
            ):
                use_item(Items.Water)

            if (x * 4 + y) % 2 == 0:
                plant(Entities.Tree)
            else:
                plant(Entities.Bush)

            if x % 2 == 0 and y + 1 < 4:
                move(North)
            elif x % 2 == 1 and y + 1 < 4:
                move(South)
            else:
                move(East)

