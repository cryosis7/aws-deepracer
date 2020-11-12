import steering_based_reward as deepRacer


def test():
    params = {'x': 0, 'y': 0, 'heading': 15, 'closest_waypoints': [0, 1], 'waypoints': [
        (0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)], 'steering_angle': -15, 'track_width': 1}
    print(deepRacer.debug(params))


test()
