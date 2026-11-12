from __builtins__ import *

# This is the sixth program. Use it
# to unlock the following upgrades:
# - Carrots I
# - Debug
# - Senses
# - Hats
# Note: You'll need to use 07_program.py to
# harvest the necessary Hay

# [x] Needs 6x harvest() every 3600 ticks
# - Speed: 900 ticks per second
# - Growth (Bush): 4.0 s, or 3600 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

while True:
    for i in range(6):
        while not can_harvest():
            continue
        harvest()
        plant(Entities.Bush)

        if i < 2:
            move(North)
        elif i == 2:
            move(East)
        elif i < 5:
            move(South)
        else:
            move(West)

