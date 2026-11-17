from __builtins__ import *

# This is the fourth program. Use it
# to unlock the following upgrades:
# - * Expand II
# - Operators
# * Wait to unlock last
# Note: You'll need to use 03_program.py to
# harvest the necessary Hay.
#
# Then REPLACE with 05_program.py AND
# MOVE to 05_program.py.

# [x] Needs 2x harvest() every 2400 ticks
# - Speed: 600 ticks per second
# - Growth (Bush): 4.0 s (mean), or 2400 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: The best rate for harvesting Wood is
# 3x harvest() every 2400 ticks. However, it takes
# only 1800 ticks to plant 3x Bush. This means that
# harvesting 3x Bush requires busy waiting anywhere
# between 600-1080 ticks. It is possible to also
# harvest 2-3x Grass in that same waiting period. My
# recommendation is to harvest 2x Bush and 3x Grass
# every 2400 ticks to best utilize that time. A neat
# way to accomplish this is to slide which two cells
# have the Bush.

while True:
    while True:
        if can_harvest():
            break
        continue
    harvest()
    plant(Entities.Bush)
    move(North)

    while True:
        if can_harvest():
            break
        continue
    harvest()
    plant(Entities.Bush)
    move(North)

    while True:
        if can_harvest():
            break
        continue
    harvest()
    while True:
        if can_harvest():
            break
        continue
    harvest()
