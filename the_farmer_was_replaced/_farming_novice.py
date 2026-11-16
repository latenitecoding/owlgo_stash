from __builtins__ import *
from _farm_utils import *


def clear_plot(N, M, x0 = 0, y0 = 0):
    ok = farm_plot(N, M, Entities.Grass, x0, y0)
    go_home()

    return ok


def farm_cell(etype, min_water = 0):
    if can_harvest():
        harvest()
    elif (
            get_water() < min_water
            and num_items(Items.Water) > 0
    ):
        use_item(Items.Water)

    if needs_till(etype):
        till()

    if get_entity_type() != etype and etype != Entities.Grass:
        if not plant(etype):
            return False

    return True


def farm_plot(N, M, etype, x0 = -1, y0 = -1):
    return farm_plot_alt(N, M, [etype], x0, y0)


def farm_plot_alt(N, M, etypes, x0 = -1, y0 = -1):
    if x0 >= 0 and y0 >= 0:
        goto(x0, y0)

    for x in range(N):
        for y in range(M):
            i = x * M + y

            etype = etypes[i % len(etypes)]
            min_water = get_min_water(N * M, etype)

            if not farm_cell(etype, min_water):
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


def go_home():
    goto(0, 0)
    return


def goto(x, y):
    if x < 0 or y < 0:
        return

    move_n_dir(dist_to(x), East)
    move_n_dir(dist_to(y), North)

    return


def move_n_dir(n, dir):
    if n < 0:
        dir = rev_dir(dir)
        n = -n

    for _ in range(n):
        move(dir)

    return

