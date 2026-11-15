from __builtins__ import *

# REPLACES 03_program.py

# This is the sixth program. Use it
# to unlock the following upgrades:
# - Debug
# - Senses
# - Hats
# Note: You'll need to use 07_program.py to
# harvest the necessary Wood
#
# Then MOVE to 08_program.py

# [x] Needs 1x harvest() every 400 ticks
# - Speed: 900 ticks per second
# - Growth (Grass): 0.5 s, or 450 ticks
# - harvest(): 200 ticks
# - move(): 200 ticks
# Note: It takes 450 ticks for Grass to grow,
# but only 400 ticks to harvest() and move()

while True:
    for i in range(2):
        harvest()

        if i == 0:
            move(North)
        else:
            move(South)

