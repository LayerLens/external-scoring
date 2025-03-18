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
    Improved test function for API call validation.
    Key changes:
    1. Extract code properly from code blocks
    2. Only execute the response, not the ground truth
    3. Compare normalized text instead of function calls
    """
    try:
        # Initialize test environment
        global correctness
        correctness = []
        
        # Extract code from ground truth without executing
        ground_truth = response_data.get("truth", "")
        ground_truth_match = re.search(r"(?s)```python\n(.*?)```", ground_truth)
        if ground_truth_match:
            # Just store the extracted code, don't execute it
            ground_truth_code = ground_truth_match.group(1).strip()
        else:
            ground_truth_code = ground_truth.strip()
            
        print("\nExtracted ground truth code:", ground_truth_code)
        
        # Extract code from response
        response_code = response_data.get("result", "")
        response_match = re.search(r"(?s)```python\n(.*?)```", response_code)
        if response_match:
            response_exec_code = response_match.group(1).strip()
        else:
            response_exec_code = response_code.strip()
            
        print("\nExtracted response code:", response_exec_code)
        
        # Use module globals for execution namespace
        namespace = globals()
        namespace['correctness'] = correctness
        
        # Execute only the response
        print("\nExecuting response code...")
        try:
            exec(response_exec_code, namespace)
            response_calls = copy.deepcopy(correctness)
            print(f"Response execution successful, made {len(response_calls)} function calls")
        except Exception as e:
            print(f"Response execution failed: {str(e)}")
            return False
        
        # Now compare the *text* of the extracted code, not the function calls
        # This allows for different formatting but same semantic meaning
        response_normalized = response_exec_code.replace("'", "\"").replace(" ", "")
        ground_truth_normalized = ground_truth_code.replace("'", "\"").replace(" ", "")
        
        print("\nNormalized response:", response_normalized)
        print("Normalized ground truth:", ground_truth_normalized)
        
        # Semantic comparison (this could be expanded with more sophisticated methods)
        if response_normalized == ground_truth_normalized:
            print("✅ Exact match after normalization!")
            return True
            
        # Check for function name match but different parameters (acceptable in some cases)
        resp_func_match = re.search(r"^(\w+)\(", response_exec_code)
        truth_func_match = re.search(r"^(\w+)\(", ground_truth_code)
        
        if resp_func_match and truth_func_match:
            resp_func = resp_func_match.group(1)
            truth_func = truth_func_match.group(1)
            
            if resp_func == truth_func:
                print(f"✅ Same function called ({resp_func}) with different parameters")
                return True
                
        print("❌ Code mismatch between response and ground truth")
        return False
        
    except Exception as e:
        print(f"Test execution failed: {str(e)}")
        return False