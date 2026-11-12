from __builtins__ import *
from behaviors import *

# This is the twelfth program. Use it
# to unlock the following upgrades:
# - Speed V
# Note: You'll need to use 10_program.py to
# harvest any necessary Wood, and 11_program.py
# to harvest any necessary Hay

# [x] Needs 18x harvest() every 10_800 ticks
# - Speed: 2025 ticks per second
# - Growth (Carrot): 6.0 s, or 12_150 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# - can_harvest(): 1 tick
# Note: A 6x3 rectangle is of sufficiently large
# size that the expected time to farm all 18 cells
# is nearly the same as the mean time for a carrot
# to grow. A single application of water on each
# cell ensures that the carrots grow quickly enough,
# and the water needed is consumed at a rate of 0.82 s,
# which is very close to the restock rate of 0.8 s.

def main():
    while harvest_rect(6, 3, Entities.Carrot):
        continue

    clear_rect(6, 3)
    return


if __name__ == "__main__":
    main()
