import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "vt_multiapi_single",
    "description": "Test cases for vt_multiapi_single API calls"
}

# Initialize correctness tracking
correctness = []

# API Function Definitions
def get_random_object_from_list(
    list_of_objects: List[Any]
) -> Any:
    """

        This function selects and returns a random object from a list of objects. It is designed to handle any list length, including empty lists.

        Args:
        - list_of_objects: list, required, List containing objects from which the function will pick out a random object.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"get_random_object_from_list": locals()})

def get_first_object_from_list(
    list_of_objects: List[Any]
) -> Any:

    """
    Retrieves the first object from a given list. If the list is empty, it return `None`.

    Args:
    - list_of_objects: List containing objects.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"get_first_object_from_list": locals()})

def calculate_sum_of_numbers(
    num1: Union[int, float],
    num2: Union[int, float]
) -> Union[int, float]:
    """

        Computes the sum of two numbers provided. Input numbers can be either integer or floating-point values.

        Args:
        - num1: Integer or Float, required, The first number
        - num2: Integer or Float, required, The second number
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"calculate_sum_of_numbers": locals()})

def extract_resolution_date(
    dns_res_obj: Dict
) -> int:
    """

        Extracts the date of DNS resolution from a DNS resolution object. The date is returned as a Unix timestamp.

        Args:
        - dns_res_obj: object, required, The DNS resolution object from which the date of resolution is to be extracted.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"extract_resolution_date": locals()})

def count_items_in_list(
    input_list: List[Any]
) -> int:
    """

        This function takes a list as an input and returns the number of items present in the list.

        Args:
        - input_list: list, required, List whose items are to be counted
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"count_items_in_list": locals()})

def vt_get_majority_vote(
    votes: Dict[str, int]
) -> str:
    """

        This function takes a dictionary of votes returns the name with the majority votes. If the votes are equal, it will return the first encountered key in the dictionary.

        Args:
        - votes: dictionary, required, dictionary of votes
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_majority_vote": locals()})

def vt_get_multiple_domain_reports(
    domains: List[str],
    x_apikey: str
) -> List[Dict]:
    """

        retrieves reports for a list of domains provided. For each domain in the list, it requests the collected information regarding that domain from VirusTotal.

        Args:
        - domains: list of strings, required, A list of Domain names
        - x_apikey: string, required, Your API key
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_multiple_domain_reports": locals()})

def vt_get_comments_on_multiple_domains(
    domains: List[str],
    x_apikey: str,
    limit: int = None,
    cursor: str = None
) -> List[Dict]:
    """

        This function will retrieve comments for each specified domain in the given list.

        Args:
        - domains, list of strings, required, List of domain names
        - x_apikey, string, required, Your API key
        - limit, int32, optional, Maximum number of comments to retrieve for each domain
        - cursor, string, optional, Continuation cursor
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_comments_on_multiple_domains": locals()})

def vt_get_last_analysis_date_from_report(
    report: Dict
) -> int:
    """

        This function retrieves the last analysis date from the domain report collected by VirusTotal. The returned date is in Unix timestamp format.

        Args:
        - report: dict, required, The domain report collected by vt_get_domain_report function.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_last_analysis_date_from_report": locals()})

def vt_is_date_within_range(
    timestamp: int,
    start: str = None,
    end: str = None
) -> bool:
    """

        Checks if a given Unix timestamp is within a specified date range. The range is specified by 'start' and 'end' dates formatted as 'YYYY/MM/DD'. It's permissible for only one of 'start' or 'end' to be present in the function call. If 'start' is not provided, the function checks if the timestamp is earlier than or equal to the 'end' date. Similarly, If 'end' is not provided, the function checks if the timestamp is later than or equal to the 'start' date.

        Args:
        - timestamp: int, required, Unix timestamp
        - start: string, optional, Start of the date range in 'YYYY/MM/DD' format
        - end: string, optional, End of the date range in 'YYYY/MM/DD' format
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_is_date_within_range": locals()})

def convert_unix_timestamp_to_date(
    unix_timestamp: int
) -> str:
    """

        Converts a UNIX timestamp to a human-readable date in the format 'YYYY/MM/DD'.

        Args:
        - unix_timestamp: integer, required, The UNIX timestamp to be converted.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"convert_unix_timestamp_to_date": locals()})

def vt_get_threat_actors_latest_modification_date(
    threat_actor_objects: List[Dict],
    x_apikey: str
) -> int:
    """

        This function retrieves the latest modification date from a list of threat actor objects. It iterates through each threat actor object, checks its modification date, and returns the most recent modification date.

        Args:
        - threat_actor_objects: list of objects, required, A list of threat actor objects.
        - x_apikey: string, required, Your API key.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_threat_actors_latest_modification_date": locals()})

def vt_get_threat_actors_main_source_region(
    threat_actors: List[Dict],
    x_apikey: str
) -> str:
    """

        This function takes a list of threat actor objects and returns the primary source region among them. Each threat actor object has an attribute 'source region', and the function analyses this attribute across all objects to determine and return the most common source region, deemed as the 'main' source region.

        Args:
        - threat_actors: list, required, List of threat actor objects
        - x_apikey: string, required, Your API key.
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_get_threat_actors_main_source_region": locals()})

def vt_validate_historical_ssl_certificates(
    historical_ssl_certificates: List[Dict],
    x_apikey: str
) -> bool:
    """

        This function takes historical SSL certificates as input and checks if there is at least one valid SSL certificate present inside the provided historical data. It validates the SSL certificate by checking whether it is not expired and its issuing authority is trustworthy.

        Args:
        - historical_ssl_certificates: list, required, List of SSL certificates in the history
        - x_apikey: string, required, Your API key
    """
    args_dict = locals()
    return_dict = {}
    for key, value in args_dict.items():
        if value:
            return_dict[key] = value
    correctness.append({"vt_validate_historical_ssl_certificates": locals()})


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
