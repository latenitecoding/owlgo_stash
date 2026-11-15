from __builtins__ import *

# REPLACES 04_program.py

# This is the fifth program. Use it
# to unlock the following upgrades:
# - * Speed II
# Then REPLACE with 07_program.py AND
# REPLACE 03_program.py with 06_program.py
# * Wait to unlock last

# [x] Needs 4x harvest() every 2400 ticks
# - Speed: 600 ticks per second
# - Growth (Bush): 4.0 s, or 2400 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

while True:
    for i in range(4):
        if can_harvest():
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

