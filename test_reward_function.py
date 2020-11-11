import aim_for_waypoint as deepRacer


def setupParams():
    return {
        'x': 0,
        'y': 0,
        'heading': 0,
        'closest_waypoints': [0, 1],
        'waypoints': [(0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)],
        'steering_angle': 0}


def test_iterate_through_all_locations():
    params = setupParams()

    for x in range(-2, 7):
        params['x'] = x
        for y in range(-2, 5):
            params['y'] = y
            for i in range(0, 7):
                params['closest_waypoints'] = [i, i + 1]
                for heading in range(-180, 181, 5):
                    params['heading'] = heading
                    for steering_angle in range(-30, 31, 5):
                        params['steering_angle'] = steering_angle

                        reward = deepRacer.reward_function(params)
                        if reward < 0 or reward > 1:
                            print("Error: params:", params)
                        assert reward >= 0
                        assert reward <= 1
