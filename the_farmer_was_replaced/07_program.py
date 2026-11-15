from __builtins__ import *

# REPLACES 05_program.py

# This is the seventh program. Use it
# to unlock the following upgrades:
# - Carrots I
# - Debug
# Note: You'll need to use 06_program.py to
# harvest the necessary Hay
#
# Then MOVE to 08_program.py

# [x] Needs 7x harvest() every 4200 ticks
# - Speed: 900 ticks per second
# - Growth (Bush): 4.8 s, or 4320 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: A mean-time strategy without growth
# rate improvements doesn't harvest resources
# as efficiently as a max-time strategy. Since
# 4320 ticks does not evenly divide into 600 ticks,
# we can use 7x Bush to get close. We could
# use 8x Bush, but the extra 480 ticks would
# be lost and wasted. By getting as close to
# 4320 ticks as we can, we can maximize the
# amaount of Bush that is ready to be harvested.
# Farming 7 cells in a 3x3 is quite strange at
# first glance, but there is a neat way to
# accomplish this due to how moves can wrap around
# the farm. There is no proper name for this, so
# I just call it wraparound mowing. Normally, a
# mowing strategy always results in the drone
# returning the starting row every two columns.
# Having to mow an odd column leaves the drone on
# the opposite side of the farm. However, since
# the drone can move with wraparound, it can simply
# mow the starting row after finishing the first
# two columns to wrap back to the origin cell.

while True:
    for i in range(7):
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
            move(East)

