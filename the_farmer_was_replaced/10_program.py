from __builtins__ import *

# REPLACES 09_program.py

# This is the tenth program. Use it
# to unlock the following upgrades:
# - Lists
# - Pumpkins I
# - * Speed V
# * Wait to unlock last
# Note: You'll need to use 06_program.py
# to harvest any necessary Hay, and the 08_program.py
# to harvest any necessary Wood. You'll need to
# use the clear() script from the README to
# return the farm to grassland when harvesting Hay.
#
# Then REPLACE with harvest_carrots.py AND
# REPLACE 06_program.py with harvest_hay.py AND
# REPLACE 08_program.py with harvest_wood.py AND
# MOVE to go_home.py and harvest_carrots.py and
# harvest_hay.py and harvest_pumpkins.py and
# harvest_wood.py.

# [x] Needs 22x harvest() every 13200 ticks
# - Speed: 2025 ticks per second
# - Growth (Carrots): 6.0 s, or 12150 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: Harvesting 22x Carrots follows the same
# reasoning that formed the basis of 09_program.py.
# Only now, the drone is faster and the plot is larger,
# so an additional cell must be traversed to reach the
# origin. We might as well farm that cell, since we can
# do so and still stay under the max growth time
# for Carrots.

def farm_carrots():
    if can_harvest():
        harvest()
    elif (
            get_water() < 22 * 600 / 2025 * 0.01 + 1.2 / 6
            and num_items(Items.Water) > 0
    ):
        use_item(Items.Water)

    if get_ground_type() != Grounds.Soil:
        till()

    if get_entity_type() != Entities.Carrot:
        plant(Entities.Carrot)

    return


while True:
    for x in range(4):
        for y in range(5):
            farm_carrots()

            if x % 2 == 0 and y + 1 < 5:
                move(North)
            elif x % 2 == 1 and y + 1 < 5:
                move(South)
            else:
                move(East)

    for _ in range(2):
        farm_carrots()
        move(East)

