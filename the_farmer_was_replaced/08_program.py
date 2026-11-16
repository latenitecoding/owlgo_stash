from __builtins__ import *

# REPLACES 05_program.py

# This is the eighth program. Use it
# to unlock the following upgrades:
# - Grass II/III/IV
# - Carrots II/III/IV
# - Trees II/III/IV
# - Watering II/III/IV (unlock early)
# - Fertilizer I/II (unlock early)
# - * Expand IV
# * Wait to unlock last
# Note: You'll need to use 06_program.py
# to harvest any necessary Hay, and the 11_program.py
# to harvest any necessary Carrots. You'll need to
# use the clear() script from the README to
# return the farm to grassland when harvesting Hay.

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

