from __builtins__ import *
from _farm_utils import *

# This library provides an API for
# common behaviors related to farming
# plots of various sizes with mixed Entities
# and applications of various Items.
#
# This library can also be executed to clear
# the farm without losing planted resources.

def clear_it():
    if get_entity_type() == None:
        return

    if get_entity_type() != Entities.Dead_Pumpkin:
        while not can_harvest():
            continue

    harvest()


def clear_plot(plot, start_pos=[0, 0], return_home=True):
    if len(plot) != 2:
        return False
    if len(start_pos) != 0 and len(start_pos) != 2:
        return False

    if len(start_pos) == 2:
        goto(start_pos[0], start_pos[1])

    X = plot[0]
    Y = plot[1]
    plot_size = X * Y

    for x in range(X):
        for y in range(Y):
            i = x * Y + y

            clear_it()

            if i + 1 < plot_size:
                move(get_next_move(Y, i))

    if return_home:
        go_home()


def clear_plots(lo_plots, lo_starts=[], return_home=True):
    if len(lo_starts) == 0:
        go_home()

    for i in range(len(lo_plots)):
        start_pos = []
        if len(lo_starts) > 0:
            start_pos = lo_starts[i % len(lo_starts)]

        clear_plot(lo_plots[i], start_pos, False)

        if len(lo_starts) == 0 and i + 1 < len(lo_plots):
            move(East)

    if return_home:
        go_home()


def farm_it(etype, min_water=0, no_harvest=False):
    # Returns False if the drone fails after
    # attempting to plant in this cell
    if get_entity_type() == Entities.Dead_Pumpkin:
        harvest()

    if can_harvest() and not no_harvest:
        harvest()
    elif (
            not can_harvest()
            and get_water() < min_water
            and num_items(Items.Water) > 0
    ):
        use_item(Items.Water)

    if needs_till(etype):
        till()

    return (
            etype == Entities.Grass
            or etype == get_entity_type()
            or plant(etype)
    )


def farm_plot(plot, lo_etypes, start_pos=[], reverse=False):
    # Returns False if the drone fails after
    # attempting to plant in this plot
    if len(plot) != 2:
        return False
    if len(start_pos) != 0 and len(start_pos) != 2:
        return False

    if len(lo_etypes) < 1:
        lo_etypes = [Entities.Grass]

    if len(start_pos) == 2:
        goto(start_pos[0], start_pos[1])

    X = plot[0]
    Y = plot[1]
    plot_size = X * Y

    for x in range(X):
        for y in range(Y):
            i = x * Y + y

            etype = lo_etypes[i % len(lo_etypes)]
            min_water = get_min_water(plot_size, etype)

            if not farm_it(etype, min_water):
                return False

            if i + 1 < plot_size:
                move(get_next_move(Y, i, reverse))

    return True


def farm_plots(lo_plots, lolo_etypes, lo_starts=[], lo_reverse=[]):
    # Returns False if the drone fails after
    # attempting to plant in any plot
    if len(lolo_etypes) < 1:
        lolo_etypes = [[Entities.Grass]]

    for i in range(len(lo_plots)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_starts) > 0:
            start_pos = lo_starts[i % len(lo_starts)]

        reverse = len(lo_reverse) > 0 and lo_reverse[i % len(lo_reverse)]

        if not farm_plot(lo_plots[i], lo_etypes, start_pos, reverse):
            return False

        if len(lo_starts) == 0 and i + 1 < len(lo_plots):
            move(East)

    return True


def plant_plot(plot, lo_etypes, start_pos=[], reverse=False):
    # Returns a triple of:
    # - number of plants planted,
    # - number of plants growing, and
    # - False if the drone fails after attempting
    #   to plant in this plot
    if len(plot) != 2:
        return 0, 0, False
    if len(start_pos) != 0 and len(start_pos) != 2:
        return 0, 0, False

    if len(lo_etypes) < 1:
        return 0, 0, True

    if len(start_pos) == 2:
        goto(start_pos[0], start_pos[1])

    X = plot[0]
    Y = plot[1]
    plot_size = X * Y

    total_planted = 0
    total_growing = 0

    for x in range(X):
        for y in range(Y):
            i = x * Y + y

            etype = lo_etypes[i % len(lo_etypes)]
            min_water = get_min_water(plot_size, etype)

            prev_etype = get_entity_type()
            if not farm_it(etype, min_water, True):
                return False

            if prev_etype != etype and get_entity_type() == etype:
                total_planted += 1

            if not can_harvest():
                total_growing += 1

            if i + 1 < plot_size:
                move(get_next_move(Y, i, reverse))

    return total_planted, total_growing, True


def plant_plots(lo_plots, lolo_etypes, lo_start=[], lo_reverse=[]):
    # Returns a triple of:
    # - number of plants planted,
    # - number of plants growing, and
    # - False if the drone fails after attempting
    #   to plant in any plot
    if len(lolo_etypes) < 1:
        return 0, 0, True

    total_planted = 0
    total_growing = 0

    for i in range(len(lo_plots)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_starts) > 0:
            start_pos = lo_starts[i % len(lo_starts)]

        reverse = len(lo_reverse) > 0 and lo_reverse[i % len(lo_reverse)]

        num_planted, num_growing, ok = plant_plot(lo_plots[i], lo_etypes, start_pos, reverse)

        total_planted += num_planted
        total_growing += num_growing

        if not ok:
            return total_planted, total_growing, False

        if len(lo_starts) == 0 and i + 1 < len(lo_plots):
            move(East)

    return total_planted, total_growing, True


def fast_grow(etype):
    fertilizer_uses = 1
    grow_factor = get_mean_grow_time(etype) / 2

    while grow_factor >= 5:
        fertilizer_uses += 1
        grow_factor /= 2

    min_water = (grow_factor - 1) * 0.25
    if min_water < 0:
        min_water = 0

    water_uses = 0
    while get_water() + water_uses * 0.25 < min_water:
        water_uses += 1

    if (
            num_items(Items.Fertilizer) < fertilizer_uses
            or num_items(Items.Water) < water_uses
    ):
        return False, True

    for _ in range(water_uses):
        use_item(Items.Water)

    while not can_harvest():
        if get_entity_type() != etype:
            if not plant(etype):
                return False, True

        if num_items(Items.Fertilizer) < 1:
            return True, True

        use_item(Items.Fertilizer)

    return True, True


def get_next_move(M, i, reverse=False):
    if (i + 1) % M == 0:
        return East

    if (i // M) % 2 == 0 or reverse:
        return North

    return South


def go_home():
    goto(0, 0)


def seed_it(etype, use_fertilizer=False):
    if etype == Entities.Grass:
        return False, True

    if etype == get_entity_type() and can_harvest():
        return False, True

    if needs_till(etype):
        till()

    if get_entity_type() != etype and not plant(etype):
        return False, False

    if not use_fertilizer:
        return False, True

    return fast_grow(etype)


def seed_plot(N, M_signed, etype, use_fertilizer=False, x0=-1, y0=-1):
    if x0 >= 0 and y0 >= 0:
        goto(x0, y0)

    M = M_signed
    if M_signed < 0:
        M = -1 * M_signed

    num_growing = 0
    num_infected = 0

    for x in range(N):
        for y in range(M):
            i = x * M + y

            infected, ok = seed_it(etype, use_fertilizer)
            if not ok:
                return num_growing, num_infected, False

            if get_entity_type() == etype and not can_harvest():
                num_growing += 1

            if infected:
                num_infected += 1

            if i + 1 < N * M:
                move(get_next_move(M_signed, i))

    return num_growing, num_infected, True


if __name__ == "__main__":
    clear_plot([get_world_size(), get_world_size()])
