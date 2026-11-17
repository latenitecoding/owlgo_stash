from __builtins__ import *
from _farm_utils import *
from _farmhand import *

# This library provides an API for
# farming plots using fertilizer.


def fart_it(etype, min_water=0, max_farts=1, no_harvest=False):
    # Returns a tuple of:
    # - True if fertilizer was used causing
    #   the plant to be infected, and
    # - False if the drone fails after
    #   attempting to plant in this cell.
    if (
            (can_harvest() and not no_harvest)
            or get_entity_type() == Entities.Dead_Pumpkin
    ):
        harvest()

    if (
        (get_entity_type() == etype and can_harvest())
        or etype == Entities.Grass
    ):
        return False, True

    if needs_till(etype):
        till()

    while get_water() < min_water and num_items(Items.Water) > 0:
        use_item(Items.Water)

    farts = 0

    while (
            not (get_entity_type() == etype and can_harvest())
            and farts < max_farts
            and num_items(Items.Fertilizer) > 0
            and get_water() >= min_water
    ):
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()

        if get_entity_type() != etype and not plant(etype):
            return farts > 0, False

        use_item(Items.Fertilizer)
        farts += 1

    return farts > 0, True


def fart_plot(plot, lo_etypes, no_harvest=False, start_pos=[], reverse=False):
    # Returns a triple of:
    # - number of plants infected,
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

    c_inf = 0
    c_grow = 0

    for x in range(X):
        for y in range(Y):
            i = x * Y + y

            # The target time of 2 represents 1x application
            # of Fertilizer. We do not need a larger target time
            # since the largest max growth time for any plant
            # is 8.4 s, which is <2 s with a water level of 0.75.
            etype = lo_etypes[i % len(lo_etypes)]
            min_water = get_max_water(plot_size, etype, 2)

            # There are only two cases in which more than 1x Fertilizer
            # would be needed, which are (1) we run out of Water, or
            # (2) the plant is a Pumpkin, which can die. If we run out
            # of Water, then we don't waste Fertilizer. So we only
            # need to worry about (2). There is a 0.2 chance of a Pumpkin
            # dying. Each application of Fertilizer represents 1x additional
            # attempt at a Pumpkin, so 2x uses means that there is a
            # 0.2^3 chance that there is still a Dead Pumpkin. 
            is_infected, ok = fart_it(etype, min_water, 3, no_harvest)
            if not ok:
                return c_inf, c_grow, False

            if is_infected:
                c_inf += 1

            if not can_harvest():
                c_grow += 1

            if i + 1 < plot_size:
                move(get_next_move(Y, i, reverse))

    return c_inf, c_grow, True


def fart_plots(lo_plots, lolo_etypes, no_harvest, lo_start=[], lo_reverse=[]):
    # Returns a triple of:
    # - number of plants infected,
    # - number of plants growing, and
    # - False if the drone fails after attempting
    #   to plant in any plot, or bad args.
    if len(lolo_etypes) < 1:
        return 0, 0, False

    c_inf = 0
    c_grow = 0

    for i in range(len(lo_plots)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_starts) > 0:
            start_pos = lo_starts[i % len(lo_starts)]

        reverse = len(lo_reverse) > 0 and lo_reverse[i % len(lo_reverse)]

        n_inf, n_grow, ok = fart_plot(
            lo_plots[i],
            lo_etypes,
            no_harvest,
            start_pos,
            reverse
        )

        c_inf += n_inf
        c_grow += n_grow

        if not ok:
            return c_inf, c_grow, False

        if len(lo_starts) == 0 and i + 1 < len(lo_plots):
            move(East)

    return c_inf, c_grow, True
