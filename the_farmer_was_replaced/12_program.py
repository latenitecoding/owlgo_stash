from __builtins__ import *

# REPLACES 09_program.py

# This is the twelfth program. Use it
# to unlock the following upgrades:
# - N/A
# Note: You'll need to use 13_program.py to
# harvest any necessary Wood, and 14_program.py
# to harvest any necessary Carrots

# [x] Needs 1x harvest() every 400 ticks
# - Speed: 2025 ticks per second
# - Growth (Grass): 0.5 s, or 1012.5 ticks
# - harvest(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: At this speed, the drone can harvest two
# cells with Grass before any one Grass grows
# back. As such, the harvest needs to harvest
# a 2x2 of Grass instead.

def farm_grass():
    if get_ground_type() != Grounds.Grassland:
        till()
    else:
        harvest()

    return


while True:
    for x in range(2):
        for y in range(2):
            farm_grass()

            if x + 1 == 2 and y + 1 == 2:
                continue

            if x % 2 == 0 and y + 1 < 2:
                move(North)
            elif x % 2 == 1 and y + 1 < 2:
                move(South)
            else:
                move(East)

    move(West)

