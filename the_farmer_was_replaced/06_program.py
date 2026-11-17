from __builtins__ import *

# REPLACES 03_program.py

# This is the sixth program. Use it
# to unlock the following upgrades:
# - Debug
# - Senses
# - Hats
# Note: You'll need to use 05_program.py to
# harvest the necessary Wood.
#
# Then MOVE to 07_program.py. DO NOT
# DELETE THIS YET.

# [x] Needs 1x harvest() every 400 ticks
# - Speed: 900 ticks per second
# - Growth (Grass): 0.5 s, or 450 ticks
# - harvest(): 200 ticks
# - move(): 200 ticks
# Note: It takes 450 ticks for Grass to grow,
# but only 400 ticks to harvest() and move(). It
# is now therefore slower to busy wait on Grass to
# grow and is more efficient to farm multiple cells.
# We only need to farm 2x cells at this time, but
# farming more is just as efficient and would allow
# this program to be reused even up to Speed V.

while True:
    for i in range(4):
        harvest()

        if i == 0:
            move(North)
        elif i == 1:
            move(East)
        elif i == 2:
            move(South)
        else:
            move(West)
