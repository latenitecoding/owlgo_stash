from __builtins__ import *

# REPLACES 07_program.py

# This is the ninth program. Use it
# to unlock the following upgrades:
# - Variables
# - Functions
# - Import
# - * Expand IV
# - * Speed IV
# * Wait to unlock last
# Note: You'll need to use 06_program.py
# to harvest any necessary Hay, and the 08_program.py
# to harvest any necessary Wood. You'll need to
# use the clear() script from the README to
# return the farm to grassland when harvesting Hay.
#
# Then REPLACE with 10_program.py AND
# MOVE to 10_program.py.

# [x] Needs 14x harvest() every 8400 ticks
# - Speed: 1350 ticks per second
# - Growth (Carrots): 6.0 s, or 8100 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: Harvesting 14x Carrots every 8400 ticks
# ensures that we meet or exceed the mean time
# for growing Carrots. It is always better to
# go slightly over mean time since it provides
# more Carrots more time to grow.

while True:
    for i in range(14):
        if can_harvest():
            harvest()
        elif (
                get_water() < 14 * 600 / 1350 * 0.01 + 1.2 / 6
                and num_items(Items.Water) > 0
        ):
            use_item(Items.Water)

        if get_ground_type() != Grounds.Soil:
            till()

        if get_entity_type() != Entities.Carrot:
            plant(Entities.Carrot)

        if i <= 2:
            move(North)
        elif i == 3:
            move(East)
        elif i <= 6:
            move(South)
        elif i == 7:
            move(East)
        elif i <= 9:
            move(North)
        elif i == 10:
            move(East)
        elif i <= 12:
            move(South)
        else:
            move(East)

