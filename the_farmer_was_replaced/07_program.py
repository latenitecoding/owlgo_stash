from __builtins__ import *

# This is the seventh program. Use it
# to unlock the following upgrades:
# - * Expand III
# - * Speed III
# - Watering I (unlock first)
# - Trees I
# * Wait to unlock last
# Note: You'll need to use 05_program.py to
# harvest the necessary Wood, and 06_program.py
# to harvest any necessary Hay. You'll need to
# use the clear() script from the README to
# return the farm to grassland when harvesting Hay.
#
# Then REPLACE with 09_program.py AND
# REPLACE 05_program.py with 08_program.py AND
# MOVE to 08_program.py and 09_program.py.

# [x] Needs 9x harvest() every ~5400 ticks
# - Speed: 900 ticks per second
# - Growth (Carrots): 6.0 s, or 5400 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: There are only 9x cells, so the max time
# that we can use is 5400 ticks for all 9x cells
# if we havest-plant-move on each cell. We do not
# count till as that only happens on the first pass.
# As such, we must go for a mean-time strategy rather
# than a max-time strategy. With a mean-time strategy,
# it's important not to busy-wait on any growing
# carrots as this could lead to increasing delays
# across passes. For example, if the first carrots
# continues to have a large growth time, then we
# would have to busy wait on the first carrots when we
# go to harvest them for the first time. However, the
# time that we wait on those carrot to grow won't count
# towards the wait time of the next carrots that
# we plant as those carrots have not been planted yet.
# Thus, these first carrots can continue to add to
# the cumulative total of wasted ticks on each pass.
# Since the grid is still a 3x3, a traditional mower
# strategy would require the drone to use two wraparound
# moves to return to the origin cell. In order to have
# the drone return to the origin cell in one move, we
# use a snake-mowing strategy with a final wrapround move.

while True:
    for i in range(9):
        if can_harvest():
            harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        if get_entity_type() != Entities.Carrot:
            plant(Entities.Carrot)

        if i < 2:
            move(North)
        elif i < 4:
            move(East)
        elif i == 4:
            move(South)
        elif i == 5:
            move(West)
        elif i == 6:
            move(South)
        else:
            move(East)
