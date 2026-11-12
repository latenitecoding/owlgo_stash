from __builtins__ import *
from farm_utils import *


def clear_rect(N, M, x0 = 0, y0 = 0):
    ok = harvest_rect(N, M, Entities.Grass, x0, y0)
    go_home()

    return ok


def farm_cell(etype, min_water = 0):
    while get_entity_type() != None and not can_harvest():
        continue
    harvest()

    if get_ground_type() != get_gtype(etype):
        till()

    if get_entity_type() != etype and etype != Entities.Grass:
        if not plant(etype):
            return False

    if get_water() < min_water and num_items(Items.Water) > 0:
        use_item(Items.Water)

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
    move_n_dir(dist_to(x), East)
    move_n_dir(dist_to(y), North)

    return


def harvest_rect(N, M, etype, x0 = 0, y0 = 0):
    goto(x0, y0)

    min_water = get_min_water(N * M, etype)

    for x in range(N):
        for y in range(M):
            if not farm_cell(etype, min_water):
                return False

            if x * M + y + 1 < N * M:
                move(get_next_move(M, x * M + y))

    return True


def move_n_dir(n, dir):
    if n < 0:
        dir = rev_dir(dir)
        n = -n

    for _ in range(n):
        move(dir)

    return


if __name__ == "__main__":
    go_home()

