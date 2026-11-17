from __builtins__ import *


def dist_to(x0, x1):
    if x0 == x1:
        return 0

    if x0 < x1:
        dist = x1 - x0
        wrap_dist = x0 + get_world_size() - x1

        if wrap_dist < dist:
            return -wrap_dist

        return dist

    dist = x0 - x1
    wrap_dist = x1 + get_world_size() - x0

    if wrap_dist < dist:
        return wrap_dist

    return -dist


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


def get_max_grow_time(etype):
    if etype == Entities.Grass:
        return 0.5

    if etype == Entities.Bush:
        return 4.8

    if etype == Entities.Carrot:
        return 7.2

    if etype == Entities.Tree:
        return 8.4

    if etype == Entities.Pumpkin:
        return 3.8

    if etype == Entities.Sunflower:
        return 8.4

    if etype == Entities.Cactus:
        return 1

    if etype == Entities.Rice:
        return 7.2

    return 0.22


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


def get_max_water(plot_size, etype, target_time=0):
    return get_target_water(
        plot_size,
        etype,
        get_max_grow_time(etype),
        target_time
    )


def get_mean_water(plot_size, etype, target_time=0):
    return get_target_water(
        plot_size,
        etype,
        get_mean_grow_time(etype),
        target_time
    )


def get_target_water(plot_size, etype, grow_time, target_time=0):
    if etype == Entities.Grass:
        return 0

    # It takes 600 ticks to farm each plot in plot_size. The
    # target grow time is the mean grow time of the subject
    # plant. At that grow time, it is expected that 0.5 of
    # the plants will be harvestable. Each plant that can
    # be harvested requires that farm time of 600 ticks. The
    # other 0.5 of the plants will require 400 ticks for
    # applying water and moving.
    plot_ticks = plot_size // 2 * 600 + (plot_size + 1) // 2 * 400

    if target_time > 0:
        # The grow factor can be scaled to a particular time
        # instead, which is useful when applying fertilizer.
        plot_ticks = target_time * get_drone_speed()
    elif etype == Entities.Pumpkin:
        # With Pumpkins, we spend our time replacing Dead Pumpkins
        # and skipping live Pumpkins.
        plot_ticks = plot_size * 200 + plot_size // 5 * 400

    grow_factor = (grow_time * get_drone_speed()) / plot_ticks
    latency = (plot_ticks / get_drone_speed()) * 0.01

    if grow_factor <= 1:
        return 0

    if grow_factor >= 5:
        return 1.0

    return (grow_factor - 1) * 0.25 + latency


def goto(x, y):
    if x < 0 or y < 0:
        return

    move_n_dir(dist_to(get_pos_x(), x), East)
    move_n_dir(dist_to(get_pos_y(), y), North)


def move_n_dir(n, dir):
    if n < 0:
        dir = rev_dir(dir)
        n = -n

    for _ in range(n):
        move(dir)


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
