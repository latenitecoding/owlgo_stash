from __builtins__ import *
from _farm_utils import *


def clear_plot(N, M, x0=0, y0=0):
    farm_plot(N, M, Entities.Grass, x0, y0)
    go_home()


def farm_it(etype, min_water=0):
    if can_harvest():
        harvest()
    elif get_water() < min_water and num_items(Items.Water) > 0:
        use_item(Items.Water)

    if needs_till(etype):
        till()

    return (
            etype == Entities.Grass
            or etype == get_entity_type()
            or plant(etype)
    )


def farm_plot(N, M, etype, x0=-1, y0=-1):
    return farm_plot_alt(N, M, [etype], x0, y0)


def farm_plot_alt(N, M, etypes, x0=-1, y0=-1):
    if x0 >= 0 and y0 >= 0:
        goto(x0, y0)

    for x in range(N):
        for y in range(M):
            i = x * M + y

            etype = etypes[i % len(etypes)]
            min_water = get_min_water(N * M, etype)

            if not farm_it(etype, min_water):
                return False

            if i + 1 < N * M:
                move(get_next_move(M, i))

    return True


def get_next_move(M, i):
    if (i // M) % 2 == 0 and (i + 1) % M > 0:
        return North

    if (i // M) % 2 == 1 and (i + 1) % M > 0:
        return South

    return East


def plant_it(etype):
    if etype == Entities.Grass:
        return False, True

    if etype == get_entity_type() and can_harvest():
        return False, True

    if needs_till(etype):
        till()

    if not plant(etype):
        return False, False

    fertilizer_uses = 1
    grow_factor = get_mean_grow_time(etype) / 2

    while grow_factor >= 5:
        fertilizer_uses += 1
        grow_factor /= 2

    water_uses = grow_factor - 1

    if (
            num_items(Items.Fertilizer) < fertilizer_uses
            or num_items(Items.Water) < water_uses
    ):
        return False, True

    for _ in range(water_uses):
        use_item(Items.Water)

    for _ in range(fertilizer_uses):
        use_item(Items.Fertilizer)

    return True, True


def plant_plot(N, M, etype, x0=-1, y0=-1):
    if x0 >= 0 and y0 >= 0:
        goto(x0, y0)

    has_infected = False

    for x in range(N):
        for y in range(M):
            infected, ok = plant_it(etype)

            has_infected = infected or has_infected
            if not ok:
                return has_infected, False

            if i + 1 < N * M:
                move(get_next_move(M, i))

    return has_infected, True


def go_home():
    goto(0, 0)


def goto(x, y):
    if x < 0 or y < 0:
        return

    move_n_dir(dist_to(x), East)
    move_n_dir(dist_to(y), North)


def move_n_dir(n, dir):
    if n < 0:
        dir = rev_dir(dir)
        n = -n

    for _ in range(n):
        move(dir)
