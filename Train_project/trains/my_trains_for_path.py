# train_utils.py
from .models import Train

def get_trains_by_path(stations):
    """
    Get a list of trains for each pair of consecutive stations.
    
    Parameters:
    - stations: List of station names in order.

    Returns:
    - A list of lists where each inner list contains tuples of train names and start stations.
    """
    # List of lists to store trains for each pair of stations
    trains_by_route = []

    # Iterate over pairs of consecutive stations
    for i in range(len(stations) - 1):
        start_station = stations[i]
        end_station = stations[i + 1]
        trains_between = []

        # Query the Train model for trains going from start_station to end_station
        trains = Train.objects.filter(start=start_station, destination=end_station)

        for train in trains:
            # Append a tuple of (train_name, start_station, starting_time, reaching_time) to trains_between
            trains_between.append((train.train_name, start_station, train.starting_time, train.reaching_time))

        # Add the list of trains to the result list
        trains_by_route.append(trains_between)
    
    return trains_by_route
