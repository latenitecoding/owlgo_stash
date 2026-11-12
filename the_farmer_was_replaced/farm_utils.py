from __builtins__ import *


def dist_to(x):
    wdpx = get_world_size() - get_pos_x()
    wdx = get_world_size() - x

    dist_between = wdpx - wdx

    if dist_between < 0 and wdpx + x + dist_between < 0:
        return wdpx + x

    if dist_between > 0 and wdx + get_pos_x() < dist_between:
        return -(wdx + get_pos_x())

    return dist_between


def get_gtype(etype):
    if etype == Entities.Grass:
        return Grounds.Grassland

    if etype == Entities.Carrot:
        return Grounds.Soil

    return get_ground_type()


def get_drone_speed():
    if num_unlocked(Unlocks.Speed) == 1:
        return 600

    if num_unlocked(Unlocks.Speed) == 2:
        return 900

    if num_unlocked(Unlocks.Speed) == 3:
        return 1350

    if num_unlocked(Unlocks.Speed) == 4:
        return 2025

    if num_unlocked(Unlocks.Speed) == 5:
        return 3037.5

    return 400


def get_mean_grow_time(etype):
    if etype == Entities.Bush:
        return 4.0

    if etype == Entities.Carrot:
        return 6.0

    if etype == Entities.Tree:
        return 7.0

    return 0.5


def get_min_water(i, etype):
    grow_factor = (get_mean_grow_time(etype) * get_drone_speed()) / (i * 600)

    if grow_factor <= 1:
        return 0

    if grow_factor >= 5:
        return 1.0

    return (grow_factor - 1) * 0.25


def rev_dir(dir):
    if dir == North:
        return South
    elif dir == South:
        return North
    elif dir == East:
        return West
    else:
        return East

