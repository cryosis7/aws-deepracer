import math

MAXIMUM_STEERING_ANGLE = 30


def test():
    # print(getReward({
    #     'x': 2, 'y': 2,
    #     'heading': -135,
    #     'closest_waypoints': [0, 1],
    #     'waypoints': [[2, 2, ], [0, 0]],
    #     'steering_angle': 10}))

    for steering_angle in range(-30, 31, 5):
        reward = getReward({
            'x': 0, 'y': 0,
            'heading': 25,
            'closest_waypoints': [0, 1],
            'waypoints': [[2, 2, ], [2, 2]],
            'steering_angle': steering_angle})
        print("Reward: ", reward, "\n")
        assert reward >= 0


def getReward(params):
    last_waypoint, next_waypoint = params['closest_waypoints']
    waypoints = params['waypoints']
    car_position = [params['x'], params['y']]
    heading = params['heading']
    steering_angle = params['steering_angle']

    # Calculating the % difference between angle to next waypoint and current orientation.
    waypoint_heading = angle(car_position, waypoints[next_waypoint])
    difference = abs(waypoint_heading - heading)
    heading_score = abs((180 - difference) / 180)
    # print("Difference: ", difference, " Heading Score: ", heading_score)

    # Adjust score based on whether we're steering towards goal.
    # The angle our current steering will take us from the waypoint. 0 = on the waypoint
    steering_innacuracy = steering_angle - difference
    steering_score = (180 - abs(steering_innacuracy)) / 180
    # print("Current Steering Angle: ", steering_angle, " Steering Innacuracy: ", steering_innacuracy)

    # Applying weightings to the score
    print(heading_score, steering_score)
    reward = (heading_score + steering_score) / 2
    # reward = ((heading_score * 2) + (steering_score * 1)) / 3

    return reward


def angle(a, b):
    x = math.degrees(math.atan2(
        b[1] - a[1],
        b[0] - a[0]
    ))
    return x


test()
