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
    if etype == Entities.Grass:
        return 0.5

    if etype == Entities.Bush:
        return 4

    if etype == Entities.Carrot:
        return 6

    if etype == Entities.Tree:
        return 7

    if etype == Entities.Pumpkin:
        return 2

    if etype == Entities.Sunflower:
        return 7

    if etype == Entities.Cactus:
        return 1

    if etype == Entities.Rice:
        return 6

    return 0.2


def get_min_water(plot_size, etype):
    plot_ticks = plot_size * 600
    grow_factor = (get_mean_grow_time(etype) * get_drone_speed()) / plot_ticks
    latency = (plot_ticks / get_drone_speed()) * 0.01

    if grow_factor <= 1:
        return 0

    if grow_factor >= 5:
        return 1.0

    return (grow_factor - 1) * 0.25 + latency


def needs_till(etype):
    if etype == Entities.Grass:
        return get_ground_type() != Grounds.Grassland

    if etype == Entities.Carrot or etype == Entities.Pumpkin:
        return get_ground_type() != Grounds.Soil

    return False


def rev_dir(dir):
    if dir == North:
        return South
    elif dir == South:
        return North
    elif dir == East:
        return West
    else:
        return East
