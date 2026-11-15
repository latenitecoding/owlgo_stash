from __builtins__ import *

# REPLACES 10_program.py

# This is the thirteenth program. Use it
# to unlock the following upgrades:
# - N/A
# Note: You'll need to use 12_program.py to
# harvest any necessary Hay, and 14_program.py
# to harvest any necessary Carrots

# [x] Needs 24x harvest() every 14_400 ticks
# - Speed: 2025 ticks per second
# - Growth (Tree): 7.0 s, or 14_175 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

def farm_wood(x, y):
    if can_harvest():
        harvest()
    elif (
            get_water() < 14400 / 2025 * 0.01 + 1.4 / 7
            and num_items(Items.Water) > 0
            and (x * 4 + y) % 2 == 0
    ):
        use_item(Items.Water)

    if (x * 4 + y) % 2 == 0:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

    return



while True:
    for x in range(6):
        for y in range(4):
            farm_wood()

            if x % 2 == 0 and y + 1 < 4:
                move(North)
            elif x % 2 == 1 and y + 1 < 4:
                move(South)
            else:
                move(East)

