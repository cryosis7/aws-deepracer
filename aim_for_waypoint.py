import math

def reward_function(params):
    '''
    Rewards the car if it is pointing towards the nearest waypoint.
    '''

    # Read input parameters
    last_waypoint, next_waypoint = params['closest_waypoints']
    waypoints = params['waypoints']
    car_position = [params['x'], params['y']]
    steering_angle = params['steering_angle']
    heading = params['heading']

    if heading < 0:
        heading = 360 + heading


    # Calculating the % difference between angle to next waypoint and current orientation of car.
    waypoint_heading = angle(car_position, waypoints[next_waypoint])
    angle_difference = abs(waypoint_heading - heading)
    heading_score = abs((180 - angle_difference) / 180)  # Converting this orientation into a % score

    # The angle our current steering will take us from the waypoint. 0 = on the waypoint
    steering_difference = abs(angle_difference - steering_angle)
    steering_score = abs((180 - steering_difference) / 180)


    # print(params,
    #     "\nWaypoint Heading: ", waypoint_heading, " Heading: ", heading,
    #     "\nAngle Difference: ", angle_difference,
    #     "\nSteering Angle: ", steering_angle,
    #     "\nSteering_innacuracy: ", steering_difference,
    #     "\nSteering Score: ", steering_score,
    #     "\n", heading_score, steering_score)

    # Applying weightings to the score
    reward = (heading_score + steering_score) / 2
    # reward = ((heading_score * 2) + (steering_score * 1)) / 3

    return reward


def angle(a, b):
    x = math.degrees(math.atan2(
        b[1] - a[1],
        b[0] - a[0]
    ))
    return x
