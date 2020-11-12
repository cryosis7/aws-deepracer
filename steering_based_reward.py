import math

RADIUS_MODIFIER = 1
DEBUG = False

def debug(params):
    DEBUG = True
    return reward_function(params)

def reward_function(params):
    '''
    Rewards the car if it is pointing towards the nearest waypoint.

    The heading is converted from -180 - 180 to 0 - 360.
    '''

    # Read input parameters
    last_waypoint, next_waypoint = params['closest_waypoints']
    waypoints = params['waypoints']
    car_position = [params['x'], params['y']]
    steering_angle = params['steering_angle']
    heading = params['heading']
    track_width = params['track_width']

    if heading < 0:
        heading = 360 + heading

    # Upsamples waypoints and determines the next point to travel to.
    target_waypoint = get_target_point(waypoints, car_position, track_width)
    target_steering_angle = get_angle(car_position, target_waypoint)
    absolute_steering_angle = get_absolute_steering_angle(
        heading, steering_angle)

    angle = abs(absolute_steering_angle - target_steering_angle)
    steering_error = min(angle, 360 - angle)
    steering_penalty = min(steering_error / 60.0, 1.0)

    if debug:
        print("Params: ", params,
              "\nHeading: ", heading,
              "\nTarget Waypoint: ", target_waypoint,
              "\nTarget Steering Angle: ", target_steering_angle,
              "\nAbsolute Steering Angle", absolute_steering_angle,
              "\nError: ", steering_error,
              "\nSteering Penalty: ", steering_penalty)

    reward = 1.0 - abs(steering_penalty)
    return reward or 0.01


def get_absolute_steering_angle(heading, steering_angle):
    angle = (heading + steering_angle) % 360
    return angle if angle >= 0 else 360 - angle


def get_target_point(waypoints, car_position, track_width):
    upsampled_waypoints = up_sample(waypoints, 20)
    dist_from_car = [get_dist(point, car_position)
                     for point in upsampled_waypoints]
    min_dist = min(dist_from_car)
    closest_waypoint_index = dist_from_car.index(min_dist)

    n = len(upsampled_waypoints)
    waypoints_starting_with_closest = [
        upsampled_waypoints[(i + closest_waypoint_index) % n] for i in range(n)]

    radius = track_width * RADIUS_MODIFIER
    inside_radius = [get_dist(p, car_position) <
                     radius for p in waypoints_starting_with_closest]
    first_point_outside_radius_index = inside_radius.index(False)

    return waypoints_starting_with_closest[first_point_outside_radius_index]


def get_dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def get_angle(a, b):
    x = math.degrees(math.atan2(
        b[1] - a[1],
        b[0] - a[0]
    ))
    return x if x >= 0 else 360 + x


def up_sample(waypoints, factor):
    """
    Adds extra waypoints in between provided waypoints
    :param waypoints:
    :param factor: integer. E.g. 3 means that the resulting list has 3 times as many points.
    :return:
    """
    p = waypoints
    n = len(p)

    return [[i / factor * p[(j+1) % n][0] + (1 - i / factor) * p[j][0],
             i / factor * p[(j+1) % n][1] + (1 - i / factor) * p[j][1]] for j in range(n) for i in range(factor)]
