import abel_tasman as deepRacer


'''
A testing function to confirm that the reward doesnt exceed the bounds.
To run:
install pytest with 'pip install pytest'
in a console, cd here and run 'pytest'
'''

def setupParams():
    return {
        'x': 3,
        'y': 3,
        'heading': 0,
        'closest_waypoints': [0, 1],
        'waypoints': [(0, 0), (2, 0), (4, 1), (5, 2), (4, 3), (2, 3), (1, 2), (0, 1)],
        'steering_angle': 0,
        'track_width': 1,
        'progress': 0}


def test_iterate_through_all_locations():
    params = setupParams()

    # for x in range(-2, 7):
    #     params['x'] = x
    #     for y in range(-2, 5):
    #         params['y'] = y
    for i in range(0, 7):
        params['closest_waypoints'] = [i, i + 1]
        for heading in range(-180, 181, 5):
            params['heading'] = heading
            for steering_angle in range(-30, 31, 5):
                params['steering_angle'] = steering_angle
                for progress in [0, 25, 50, 75, 100]:
                    params['progress'] = progress

                    reward = deepRacer.reward_function(params)
                    if reward <= 0 or (reward > 1 and (reward != 30 or progress != 100)):
                        print("Error: params:", params)
                    assert reward > 0
                    assert reward <= 1 or (reward == 30 and progress == 100)