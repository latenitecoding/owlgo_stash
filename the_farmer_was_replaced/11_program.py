from __builtins__ import *

# This is the eleventh program. Use it
# to unlock the following upgrades:
# - Trees II/III/IV
# Note: You'll need to use 10_program.py to
# harvest any necessary Wood, and 09_program.py
# to harvest any necessary Carrots

# [x] Needs 1x harvest() every 400 ticks
# - Speed: 1350 ticks per second
# - Growth (Grass): 0.5 s, or 675 ticks
# - harvest(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick

while True:
    for i in range(2):
        while get_entity_type() != None and not can_harvest():
            continue
        harvest()

        if get_ground_type() != Grounds.Grassland:
            till()

        if i == 0:
            move(North)
        else:
            move(South)

