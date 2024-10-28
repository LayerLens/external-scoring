import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "ClimateAPIBenchmark",
    "description": "Test cases for ClimateAPIBenchmark API calls"
}

# Initialize correctness tracking
correctness = []

# API Function Definitions
def get_latitude_longitude(
    location: str
) -> List[float]:
    """
    Given a city name, this function provides the latitude and longitude of the specific location.

    Args:
    - location: This can be a city like 'Austin', or a place like 'Austin Airport', etc.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_latitude_longitude": locals()})

def get_current_location() -> str:
    """
    Returns the current location. ONLY use this if the user has not provided an explicit location in the query.

    Returns a string representation of the city, such as "Austin". This will not return a latitude or longitude.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_current_location": locals()})

def find_nearby_stations(
    lat_long: Tuple[float, float]
) -> List[Dict]:
    """
    This endpoint provides a list of nearby weather stations for a given geographical location. Please provide the geographical location as a latitude and longitude.

    Args:
        - lat_long: This argument should be a tuple of the latitude as the first element and the longitude as the second element.

    Returns:
        - A list of dictionaries about the various stations near you.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"find_nearby_stations": locals()})

def get_nearest_station_id(
    nearby_stations: List[Dict]
) -> str:
    """
    Given a list of nearby stations, returns the one nearest to you and provides the system ID for it alone.

    Args:
        - nearby_stations: A list of nearby stations in dictionary format.

    Returns:
        The station_id alone for the nearest station in the list of the stations provided.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_nearest_station_id": locals()})

def get_timezone(
    lat_long: Tuple[float, float]
) -> str:
    """
    This gets the timezone for a given latlong.

    Args:
      - lat_long: The latitude and longitude of the area you want to query the timezone for.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_timezone": locals()})

def get_hourly_observation(
    station_id: str,
    start_time: str,
    end_time: str,
    time_zone: str
) -> List[Dict]:
    """
    Returns hourly observations between start_time and end_time.

    Please ensure that the start and end times are provided in the format "YYYY-MM-DD".
    Please provide the timezone for your input as well!

    Args:
        - station_id: The station_id for the station you're interested in
        - start_time : The time span to start pulling hourly observations for. Should be in format of "YYYY-MM-DD".
        - end_time: The time span to end pulling hourly observations for. Should be in format of "YYYY-MM-DD".
        - timezone: The timezone string id for the location you're asking for.

    Returns:
        The list of hourly observations for your station and timespan.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_hourly_observation": locals()})

def subtract_time_delta(
    date_time_str: str,
    delta_days: int
) -> str:
    """
    Subtracts a time delta from the date part of a given date time string and returns
    the new date string with the updated date.

    DO NOT use this if delta_days is 0.

    :param date_time_str: The date time string in format 'YYYY-MM-DD'.
    :param delta_days: Number of days to subtract. HAS TO BE LARGER THAN 0.
    :return: New date string with the updated date after subtracting the delta.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"subtract_time_delta": locals()})

def get_current_time_at_location(
    lat_long: Tuple[float, float]
) -> str:
    """
    Returns the current time at a given location.

    Args:
      - lat_long: The latitude and longitude of the location of interest.
    """
    args_dict = locals()
    global correctness
    return_dict = {
    }
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_current_time_at_location": locals()})


def ll_run_tests(response_data):
    """
    Main test function for API call validation.
    Args:
        response_data: Dict containing response and ground truth
    Returns:
        bool: True if test passes
    """
    try:
        # Initialize test environment
        global correctness
        
        # Execute ground truth
        correctness = []
        namespace = {"correctness": correctness}
        ground_truth = response_data.get("truth", "")
        exec(ground_truth, namespace)
        ground_truth_calls = copy.deepcopy(correctness)
        
        # Execute response
        correctness = []
        namespace = {"correctness": correctness}
        response_code = response_data.get("parsed_result", response_data.get("result", ""))
        exec(response_code, namespace)
        response_calls = copy.deepcopy(correctness)
        
        # Compare function calls and arguments
        if len(response_calls) != len(ground_truth_calls):
            print(f"Expected {len(ground_truth_calls)} function calls, got {len(response_calls)}")
            return False
        
        for expected, actual in zip(ground_truth_calls, response_calls):
            if expected != actual:
                print(f"Function call mismatch:\nExpected: {expected}\nGot: {actual}")
                return False
        
        return True
        
    except Exception as e:
        print(f"Test execution failed: {str(e)}")
        return False
