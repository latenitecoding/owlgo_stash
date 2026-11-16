from __builtins__ import *

# REPLACES 04_program.py

# This is the fifth program. Use it
# to unlock the following upgrades:
# - Speed II
#
# Then REPLACE 03_program.py with 06_program.py
# AND MOVE to 06_program.py.

# [x] Needs 6x harvest() every 3600 ticks
# - Speed: 600 ticks per second
# - Growth (Bush): 4.8 s, or 2880 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: We could instead harvest 4x Bush to be
# closer to the mean time or even 5x Bush to be
# closer to the max time. We instead opt for farming
# 6x Bush so that this program doesn't need to be
# replaced after the next Speed upgrade.

while True:
    for i in range(6):
        if can_harvest():
            harvest()
            plant(Entities.Bush)

        if i <= 1:
            move(North)
        elif i == 2:
            move(East)
        elif i <= 4:
            move(South)
        else:
            move(West)

