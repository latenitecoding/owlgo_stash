from __builtins__ import *
from _farming_novice import *

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
# grown by a second pass of the same 2x columns. We can do even
# better with Fertilizer and Water. A water level of at least 0.225
# ensures that the max grow time of a Pumpkin is <= 2 s, which
# is the growth reduction of Fertlizer. So a Pumpkin on a cell
# with a water level of at least 0.225 grows instantly when
# subjected to Fertilizer. Thus, we could know the outcome of
# each re-planted Pumpkin with just one farm action (~0.2 s).
# We could do the same for every Pumpkin from the beginning, but
# that would require a significant amount of Fertilizer. The
# tradeoff is that Fertilizer will infect the Pumpkin and thus
# also the mega-Pumpkin causing half its yield to be Weird Substance.
# Since the resulting mega-Pumpkin is just one Pumpkin, its
# fairly easy to cure the mega-Pumpkin of its infection with just
# 1x application of Weird Substance.

def fertilize_pumpkin():
    if (
            num_items(Items.Fertilizer) > 0
            and num_items(Items.Weird_Substance) > 0
    ):
        use_items(Items.Fertilizer)
        return True
    else:
        return False


def grow_pumpkin():
    if (
        get_entity_type() == Entities.Pumpkin
        and can_harvest()
    ):
        return False, True

    if (
            get_entity_type() == Entities.Pumpkin
            and (not can_harvest())
            and (not fertilize_pumpkin())
    ):
        return False, False

    while get_entity_type() != Entities.Pumpkin:
        farm_cell(Entities.Pumpkin, 0.25)

        if not fertilize_pumpkin():
            return False, False

    return True, True


def replant_pumpkins(N, M):
    is_infected = False

    for i in range(N // 2):
        needs_scan = True

        while needs_scan:
            needs_scan = False

            for y in range(2 * M):
                used_fertilizer, ok = grow_pumpkin()

                is_infected = is_infected or used_fertilizer
                need_scan = needs_scan or (not ok)

                if y + 1 < M:
                    move(North)
                elif y + 1 == M:
                    move(East)
                elif y + 1 < 2 * M:
                    move(South)

    return is_infected


def main():
    while farm_plot(6, 6, Entities.Pumpkin):
        go_home()

        if replant_pumpkins(6, 6):
            use_items(Items.Weird_Substance)

        go_home()
        harvest()

    clear_plot(6, 6)
    return


if __name__ == "__main__":
    main()

