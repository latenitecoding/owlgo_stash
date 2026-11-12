from __builtins__ import *

# This is the ninth program. Use it
# to unlock the following upgrades:
# - Variables
# - Functions
# - Import
# - Expand IV
# - Speed IV
# Note: You'll need to use 10_program.py to
# harvest the necessary Wood, and 11_program.py
# to harvest any necessary Hay

# [x] Needs 14x harvest() every 8400 ticks
# - Speed: 1350 ticks per second
# - Growth (Carrots): 6.0 s, or 8100 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: Harvesting 14x Carrots every 8400 ticks
# is the equivalent of harvesting 13.5 carrots every
# 8100 ticks. Since 300 ticks is less than a harvest()
# and move(), it's best to use those ticks to harvest
# one additional carrot every two passes.

while True:
    for i in range(14):
        while get_entity_type() != None and not can_harvest():
            continue
        harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        if not plant(Entities.Carrot):
            return

        if i < 3:
            move(North)
        elif i == 3:
            move(East)
        elif i < 7:
            move(South)
        elif i == 7:
            move(East)
        elif i < 10:
            move(North)
        elif i == 10:
            move(East)
        elif i < 13:
            move(South)
        else:
            move(East)

