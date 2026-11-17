from __builtins__ import *
from _farmhand import *

# This program provides an option
# to farm any necessary Pumpkins.

# [x] Needs 36x plant() every 21600 ticks
# - Speed: 3037.5 ticks per second
# - Growth (Pumpkins): 2.0 s, or 6075 ticks
# - harvest(): 200 ticks
# - plant(): 200 ticks
# - move(): 200 ticks
# Note: The yield of farming Pumpkins increases with
# the size of the mega-Pumpkin, so a 6x6 mega-Pumpkin
# yields far more than 36x Pumpkins. The only problem
# is that each Pumpkin has a 20% of dying after a full
# growth period. Given that Pumpkins have a mean growth
# time of 2.0 s, we can farm (harvest-plant-move) roughly
# 10x cells in the time it takes 1x Pumpkin to grow or die.
# Therefore, it makes more sense to plant all 36x Pumpkins
# before replanting those that have died. At which point, we
# can farm the same plot again to replant those Pumpkins that
# have died. It would take too long to re-farm the entire plot
# for each dead Pumpkin, so it would be better to scan the
# plot in pairs of columns. Given the death rate of Pumpkins,
# it takes approximately 1 s to farm the 12x cells in the 2x
# columns. If only water is being used, then mean growth time
# can be easily reduced to 1 s if a Pumpkin has not finished
# growing while ensuring that all re-planted Pumpkins will have
# grown by a second pass of the same 2x columns. 


def main():
    while farm_plot([6, 6], [Entities.Pumpkin], [0, 0]):
        total_growing = 6 * 6
        start_pos = [0, 0]

        while total_growing > 0:
            num_growing = 2 * 6

            while num_growing > 0:
                _, num_growing, ok = plant_plot([2, 6], [Entities.Pumpkin], start_pos)
                if not ok:
                    clear_plot([6, 6])
                    return

            total_growing -= 2 * 6
            start_pos = [start_pos[0] + 2, 0]

        harvest()

    clear_plot(6, 6)
    return


if __name__ == "__main__":
    main()
