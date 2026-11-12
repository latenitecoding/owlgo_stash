from __builtins__ import *

# This is the eighth program. Use it
# to unlock the following upgrades:
# - Expand III
# - Speed III
# - Trees I
# Note: You'll need to use 06_program.py to
# harvest the necessary Wood, and 07_program.py
# to harvest any necessary Hay

# [x] Needs 9x harvest() every 5400 ticks
# - Speed: 900 ticks per second
# - Growth (Carrots): 6.0 s, or 5400 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

while True:
    for i in range(9):
        while get_entity_type() != None and not can_harvest():
            continue
        harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        if not plant(Entities.Carrot):
            return

        if i < 2:
            move(North)
        elif i < 4:
            move(East)
        elif i == 4:
            move(South)
        elif i == 5:
            move(West)
        elif i == 6:
            move(South)
        else:
            move(East)

