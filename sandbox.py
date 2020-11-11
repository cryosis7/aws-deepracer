import aim_for_waypoint as deepRacer


def test():
    params = {'x': -2, 'y': 1, 'heading': -10, 'closest_waypoints': [0, 1], 'waypoints': [
        (0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)], 'steering_angle': -5}

    print(deepRacer.reward_function(params))


test()
