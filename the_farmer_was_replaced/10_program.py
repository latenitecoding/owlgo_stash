from __builtins__ import *

# This is the tenth program. Use it
# to unlock the following upgrades:
# - Carrots II/III/IV
# - Grass III/IV
# - Watering I/II/III/IV
# - Expand IV
# Note: You'll need to use 10_program.py to
# harvest the necessary Wood, and 11_program.py
# to harvest any necessary Hay

# [x] Needs 15x harvest() every 9000 ticks
# - Speed: 1350 ticks per second
# - Growth (Tree): 7.0 s, or 9450 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: We can harvest 8/7x Tree/Bush every 9000 ticks, which
# leaves 450 ticks remaining. This is only slightly more
# than the number of ticks required to harvest() and move(),
# so we can harvest 8/7x Tree/Bush and one Grass.

while True:
    for x in range(4):
        for y in range(4):
            while get_entity_type() != None and not can_harvest():
                continue
            harvest()

            if get_ground_type() != Grounds.Grassland:
                till()

            if x * 4 + y + 1 == 4 * 4:
                move(East)
                continue

            if (x * 4 + y) % 2 == 0:
                plant(Entities.Tree)
            else:
                plant(Entities.Bush)

            if x % 2 == 0 and get_pos_y() + 1 < 4:
                move(North)
            elif x % 2 == 1 and get_pos_y() > 0:
                move(South)
            else:
                move(East)

