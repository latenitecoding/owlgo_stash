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
        return
    if len(start_pos) != 0 and len(start_pos) != 2:
        return

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
    # attempting to plant in this cell.
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
    # attempting to plant in this plot, or bad args.
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
            min_water = get_mean_water(plot_size, etype)

            if not farm_it(etype, min_water):
                return False

            if i + 1 < plot_size:
                move(get_next_move(Y, i, reverse))

    return True


def farm_plots(lo_plots, lolo_etypes, lo_starts=[], lo_reverse=[]):
    # Returns False if the drone fails after
    # attempting to plant in any plot, or bad args.
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
    #   to plant in this plot, or bad args.
    if len(plot) != 2:
        return 0, 0, False
    if len(start_pos) != 0 and len(start_pos) != 2:
        return 0, 0, False
    if len(lo_etypes) < 1:
        return 0, 0, False

    if len(start_pos) == 2:
        goto(start_pos[0], start_pos[1])

    X = plot[0]
    Y = plot[1]
    plot_size = X * Y

    c_plant = 0
    c_grow = 0

    for x in range(X):
        for y in range(Y):
            i = x * Y + y

            etype = lo_etypes[i % len(lo_etypes)]
            min_water = get_mean_water(plot_size, etype)

            prev_etype = get_entity_type()
            if not farm_it(etype, min_water, True):
                return c_plant, c_grow, False

            if prev_etype != etype and get_entity_type() == etype:
                c_plant += 1

            if not can_harvest():
                c_grow += 1

            if i + 1 < plot_size:
                move(get_next_move(Y, i, reverse))

    return c_plant, c_grow, True


def plant_plots(lo_plots, lolo_etypes, lo_start=[], lo_reverse=[]):
    # Returns a triple of:
    # - number of plants planted,
    # - number of plants growing, and
    # - False if the drone fails after attempting
    #   to plant in any plot, or bad args.
    if len(lolo_etypes) < 1:
        return 0, 0, False

    c_plant = 0
    c_grow = 0

    for i in range(len(lo_plots)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_starts) > 0:
            start_pos = lo_starts[i % len(lo_starts)]

        reverse = len(lo_reverse) > 0 and lo_reverse[i % len(lo_reverse)]

        n_plant, n_grow, ok = plant_plot(
            lo_plots[i],
            lo_etypes,
            start_pos,
            reverse
        )

        c_plant += n_plant
        c_grow += n_grow

        if not ok:
            return c_plant, c_grow, False

        if len(lo_starts) == 0 and i + 1 < len(lo_plots):
            move(East)

    return c_plant, c_grow, True


def get_next_move(M, i, reverse=False):
    if (i + 1) % M == 0:
        return East

    if (i // M) % 2 == 0 or reverse:
        return North

    return South


def go_home():
    goto(0, 0)


if __name__ == "__main__":
    clear_plot([get_world_size(), get_world_size()])
