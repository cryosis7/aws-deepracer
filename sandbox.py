import math
import aim_for_waypoint as deepRacer

MAXIMUM_STEERING_ANGLE = 30


def test():
    params = {'x': -2, 'y': -2, 'heading': -165, 'closest_waypoints': [0, 1], 'waypoints': [(0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)], 'steering_angle': -30}

    print(deepRacer.reward_function(params))


def angle(a, b):
    x = math.degrees(math.atan2(
        b[1] - a[1],
        b[0] - a[0]
    ))
    return x


test()
