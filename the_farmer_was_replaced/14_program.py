from __builtins__ import *

# REPLACES 11_program.py

# This is the fourteenth program. Use it
# to unlock the following upgrades:
# - * Speed V
# Note: You'll need to use 12_program.py to
# harvest any necessary Hay, and 13_program.py
# to harvest any necessary Wood
# * Wait to unlock last

# [x] Needs 22x harvest() every 13_200 ticks
# - Speed: 2025 ticks per second
# - Growth (Carrot): 6.0 s, or 12_150 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: Using 22x Carrots with a mower strategy
# over a 4x5 grid provides the most time effective
# mean-time strategy for harvesting Carrots. While
# the time required is slightly larger than the mean
# it is still less than the max. This means that the
# likelihood that carrots are harvestable is slightly
# higher and no time is wasted. Since the farm is a
# 6x6 plot, we can farm the first cells on the
# fifth and sixth columns on our way to the origin cell.

def farm_carrots():
    if can_harvest():
        harvest()
    elif (
            get_water() < 13200 / 2025 * 0.01 + 1.2 / 6
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

    farm_carrots()
    move(East)

