from datetime import datetime, timedelta

def find_optimal_route(trains_route_list_with_start_st):
    if len(trains_route_list_with_start_st) == 1:
        return trains_route_list_with_start_st[0]

    optimal_route = None
    min_time_difference = None

    for train_route in trains_route_list_with_start_st:
        start_time = train_route[0][2]  # 3rd element of the first tuple (datetime.time object)
        reach_time = train_route[-1][3]  # 4th element of the last tuple (datetime.time object)

        # Calculate the time difference (accounting for possible overnight travel)
        start_datetime = datetime.combine(datetime.today(), start_time)
        reach_datetime = datetime.combine(datetime.today(), reach_time)
        if reach_datetime < start_datetime:
            reach_datetime += timedelta(days=1)

        time_difference = reach_datetime - start_datetime

        # If this is the first route or the smallest time difference found
        if min_time_difference is None or time_difference < min_time_difference:
            min_time_difference = time_difference
            optimal_route = train_route

    return optimal_route


