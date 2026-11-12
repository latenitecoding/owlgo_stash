from __builtins__ import *

# This is the fourth program. Use it
# to unlock the following upgrades:
# - Speed II

# [x] Needs 4x harvest() every 2400 ticks
# - Speed: 600 ticks per second
# - Growth (Bush): 4.0 s, or 2400 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

while True:
    for i in range(4):
        while not can_harvest():
            continue
        harvest()
        plant(Entities.Bush)

        if i == 0:
            move(North)
        elif i == 1:
            move(East)
        elif i == 2:
            move(South)
        else:
            move(West)

