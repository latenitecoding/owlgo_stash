from __builtins__ import *

# REPLACES 02_program.py

# This is the third program. Use it
# to unlock the following upgrades:
# - * Expand I
# - Plant
# * Wait to unlock last
#
# Then MOVE to 04_program.py. DO NOT
# DELETE THIS YET.

# [x] Needs 1x harvest() every 300 ticks
# - Speed: 600 ticks per second
# - Growth (Grass): 0.5 s, or 300 ticks
# - harvest(): 200 ticks
# - can_harvest(): 1 tick

while True:
    if can_harvest():
        harvest()
