import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "PlacesAPIBenchmark",
    "description": "Test cases for PlacesAPIBenchmark API calls"
}

# Initialize correctness tracking
correctness = []

# API Function Definitions
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

def sort_results(
    places: List[Dict],
    sort: str,
    ascending: bool
) -> List[Dict]:
    """
    Sorts the results by either 'distance', 'rating' or 'price'.

    Args
    - places: The output list from the recommendations.
    - sort (str): If set, sorts by either 'distance' or 'rating' or 'price'. ONLY supports 'distance' or 'rating' or 'price'.
    - ascending (bool): If ascending is set, setting this boolean to true will sort the results by lower values first.
    """
    args_dict = locals()
    global correctness
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"sort_results": locals()})

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

def get_distance(
    place_1: str,
    place_2: str
) -> float:
    """
    Provides distance between two locations. Do NOT provide latitude longitude, but rather, provide the string descriptions.

    Args
    - place_1: The first location.
    - place_2: The second location.
    """
    args_dict = locals()
    global correctness
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_distance": locals()})

def get_recommendations(
    topics: List[str],
    lat_long: Tuple[float, float]
) -> List[Dict]:
    """
    Returns the recommendations for a specific topic that is of interest. Remember, a topic IS NOT an establishment. For establishments, please use anothher function.

    Args
    - topics (list): A list of topics of interest to pull recommendations for. Can be multiple words.
    - lat_long (tuple): The lat_long of interest.
    """
    args_dict = locals()
    global correctness
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_recommendations": locals()})

def find_places_near_location(
    type_of_place: List[str],
    location: str,
    radius_miles: int = 50
) -> List[Dict]:
    """
    Find places close to a very defined location.

    Args
    - type_of_place (list): The type of place. This can be something like 'restaurant' or 'airport'. Make sure that it is a physical location. You can provide multiple words.
    - location (str): The location for the search. This can be a city's name, region, or anything that specifies the location.
    - radius_miles (int): Optional. The max distance from the described location to limit the search. Distance is specified in miles.
    """
    args_dict = locals()
    global correctness
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"find_places_near_location": locals()})

def get_some_reviews(
    place_names: List[str],
    location: str = None
) -> List[Dict]:
    """
    Given an establishment (or place) name, return reviews about the establishment.

    Args
    - place_names (list): The name of the establishment. This should be a physical location name. You can provide multiple inputs.
    - location (str) : The location where the restaurant is located. Optional argument.
    """
    args_dict = locals()
    global correctness
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value

    correctness.append({"get_some_reviews": locals()})


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
        correctness = []
        
        # Use module globals for execution namespace
        namespace = globals()
        namespace['correctness'] = correctness
        
        # Execute ground truth
        ground_truth = response_data.get("truth", "")
        exec(ground_truth, namespace)
        ground_truth_calls = copy.deepcopy(correctness)
        
        # Reset correctness for response execution
        correctness = []
        namespace['correctness'] = correctness
        
        # Execute response
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
