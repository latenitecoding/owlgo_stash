from __builtins__ import *
from behaviors import *

# This is the thirteenth program. Use it
# to unlock the following upgrades:
# - Lists
# - Sunflowers
# - Pumpkins I
# Note: You'll need to use 10_program.py to
# harvest any necessary Wood, and 11_program.py
# to harvest any necessary Hay

# [x] Needs 24x harvest() every 14_400 ticks
# - Speed: 3037.5 ticks per second
# - Growth (Carrot): 6.0 s, or 18_225 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: A 6x4 rectangle is of sufficiently large
# size that the expected time to farm all 18 cells
# is nearly the same as the mean time for a carrot
# to grow. A single application of water on each
# cell ensures that the carrots grow quickly enough,
# and the water needed is consumed at a rate of 1.26 s,
# which is close enough to the restock rate of 0.8 s.

def main():
    while harvest_rect(6, 4, Entities.Carrot):
        continue

    clear_rect(6, 4)
    return


if __name__ == "__main__":
    main()
