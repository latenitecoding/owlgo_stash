from __builtins__ import *

# REPLACES 08_program.py

# This is the eleventh program. Use it
# to unlock the following upgrades:
# - Variables
# - Functions
# - Import
# - * Expand IV
# - * Speed IV
# Note: You'll need to use 09_program.py to
# harvest the necessary Hay, and 10_program.py
# to harvest any necessary Wood
#
# Then REPLACE with 14_program.py AND
# REPLACE 06_program.py with 12_program.py AND
# REPLACE 07_program.py with 13_program.py
# * Wait to unlock last

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
# one additional carrot every two passes. To farm 14x
# Carrots on a 4x4, we can farm one less cell in the
# last two columns.

while True:
    for i in range(14):
        if can_harvest():
            harvest()
        elif (
                get_water() < 6 * 0.01 + 1.2 / 6
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

