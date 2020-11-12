import abel_tasman as deepRacer

'''
A function for testing the reward function with specific paramters
'''


def test():
    params = {'x': 3, 'y': 3, 'heading': -155, 'closest_waypoints': [0, 1], 'waypoints': [(0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)], 'steering_angle': 30, 'track_width': 1, 'progress': 0}

    print(deepRacer.debug(params))


test()
