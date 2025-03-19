import re
import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "vt_multiapi_single",
    "description": "Test cases for vt_multiapi_single API calls"
}

# Initialize correctness tracking
correctness = []

def pre_initialization():
    """Reset the correctness list before each test run"""
    global correctness
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
    correctness.append({"get_random_object_from_list": locals()})
    return list_of_objects[0] if list_of_objects else None

def get_first_object_from_list(
    list_of_objects: List[Any]
) -> Any:
    """
    Retrieves the first object from a given list. If the list is empty, it return `None`.

    Args:
    - list_of_objects: List containing objects.
    """
    correctness.append({"get_first_object_from_list": locals()})
    return list_of_objects[0] if list_of_objects else None

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
    correctness.append({"calculate_sum_of_numbers": locals()})
    return (num1 or 0) + (num2 or 0)

def extract_resolution_date(
    dns_res_obj: Dict
) -> int:
    """
    Extracts the date of DNS resolution from a DNS resolution object. The date is returned as a Unix timestamp.

    Args:
    - dns_res_obj: object, required, The DNS resolution object from which the date of resolution is to be extracted.
    """
    correctness.append({"extract_resolution_date": locals()})
    return 1678886400  # Unix timestamp for 2023-03-15

def count_items_in_list(
    input_list: List[Any]
) -> int:
    """
    This function takes a list as an input and returns the number of items present in the list.

    Args:
    - input_list: list, required, List whose items are to be counted
    """
    correctness.append({"count_items_in_list": locals()})
    return len(input_list) if input_list else 0

def vt_get_majority_vote(
    votes: Dict[str, int]
) -> str:
    """
    This function takes a dictionary of votes returns the name with the majority votes. If the votes are equal, it will return the first encountered key in the dictionary.

    Args:
    - votes: dictionary, required, dictionary of votes
    """
    correctness.append({"vt_get_majority_vote": locals()})
    if not votes:
        return ""
    return max(votes.items(), key=lambda x: x[1])[0]

def vt_get_ip_address_report(
    ip_address: str = None,
    ip: str = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to get an IP address report from VirusTotal.

    Args:
    - ip_address: string, required, IP address to retrieve the report for
    - ip: string, alternative parameter name for ip_address
    - x_apikey: string, required, Your API key
    """
    # Handle both 'ip_address' and 'ip' parameters for backward compatibility
    address = ip_address or ip
    correctness.append({"vt_get_ip_address_report": {"ip_address": address, "x_apikey": x_apikey}})
    return {"data": "mock_ip_report"}

def vt_get_domain_report(
    domain: str = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to get a domain report from VirusTotal.

    Args:
    - domain: string, required, Domain name to retrieve the report for
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_domain_report": locals()})
    return {"data": "mock_domain_report"}

def vt_get_domain_reports(
    domains: List[str] = None,
    x_apikey: str = None
) -> List[Dict]:
    """
    Mock function to get multiple domain reports in a single call.

    Args:
    - domains: list of strings, required, List of domain names
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_domain_reports": locals()})
    return [{"data": "mock_domain_report"} for _ in domains] if domains else []

def vt_get_multiple_domain_reports(
    domains: List[str],
    x_apikey: str
) -> List[Dict]:
    """
    Retrieves reports for a list of domains provided. For each domain in the list, it requests the collected information regarding that domain from VirusTotal.

    Args:
    - domains: list of strings, required, A list of Domain names
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_multiple_domain_reports": locals()})
    return [{"data": {"key": "value"}} for _ in domains] if domains else []

def vt_get_last_analysis_date_from_report(
    report: Dict
) -> int:
    """
    This function retrieves the last analysis date from the domain report collected by VirusTotal. The returned date is in Unix timestamp format.

    Args:
    - report: dict, required, The domain report collected by vt_get_domain_report function.
    """
    correctness.append({"vt_get_last_analysis_date_from_report": locals()})
    return 1640995200  # Unix timestamp for 2022-01-01

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
    correctness.append({"vt_is_date_within_range": locals()})
    return True

def vt_get_comments_on_domain(
    domain: str = None,
    x_apikey: str = None,
    limit: int = None
) -> List[str]:
    """
    Mock function to get comments on a domain.

    Args:
    - domain: string, required, Domain name
    - x_apikey: string, required, Your API key
    - limit: int, optional, Maximum number of comments to retrieve
    """
    correctness.append({"vt_get_comments_on_domain": locals()})
    return ["comment1", "comment2"]

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
    correctness.append({"vt_get_comments_on_multiple_domains": locals()})
    return ["comment1", "comment2", "comment3"]

def vt_get_comments_on_ip_address(
    ip: str = None,
    x_apikey: str = None
) -> List[str]:
    """
    Mock function to get comments on an IP address.

    Args:
    - ip: string, required, IP address
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_comments_on_ip_address": locals()})
    return ["comment1", "comment2"]

def vt_add_comment_to_ip_address(
    ip: str = None,
    comment: str = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to add a comment to an IP address.

    Args:
    - ip: string, required, IP address
    - comment: string, required, The comment to add
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_add_comment_to_ip_address": locals()})
    return {"data": {"id": "mock_comment_id"}}

def vt_add_votes_to_ip_address(
    ip: str = None,
    votes: Dict = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to add votes to an IP address.

    Args:
    - ip: string, required, IP address
    - votes: dict, required, Vote information
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_add_votes_to_ip_address": locals()})
    return {"data": {"attributes": {"votes": votes}}}

def vt_get_votes_on_ip_address(
    ip: str = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to get votes on an IP address.

    Args:
    - ip: string, required, IP address
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_votes_on_ip_address": locals()})
    return {"data": {"attributes": {"votes": {"harmless": 10, "malicious": 2}}}}

def convert_unix_timestamp_to_date(
    unix_timestamp: int
) -> str:
    """
    Converts a UNIX timestamp to a human-readable date in the format 'YYYY/MM/DD'.

    Args:
    - unix_timestamp: integer, required, The UNIX timestamp to be converted.
    """
    correctness.append({"convert_unix_timestamp_to_date": locals()})
    return "2023-03-15" if unix_timestamp else None

def vt_get_dns_resolution_object(
    id: str = None,
    x_apikey: str = None
) -> Dict:
    """
    Mock function to get a DNS resolution object.

    Args:
    - id: string, required, The ID of the DNS resolution
    - x_apikey: string, required, Your API key
    """
    correctness.append({"vt_get_dns_resolution_object": locals()})
    return {"domain": "example.com", "ip_address": "192.168.1.1", "date": 1678886400}

def vt_get_objects_related_to_ip_address(
    ip: str = None,
    relationship_type: str = None,
    x_apikey: str = None,
    limit: int = None
) -> List[str]:
    """
    Mock function to get objects related to an IP address.

    Args:
    - ip: string, required, IP address
    - relationship_type: string, required, Type of relationship
    - x_apikey: string, required, Your API key
    - limit: int, optional, Maximum number of objects to retrieve
    """
    correctness.append({"vt_get_objects_related_to_ip_address": locals()})
    return ["related_obj1", "related_obj2"]

def vt_get_objects_related_to_domain(
    domain: str = None,
    relationship_type: str = None,
    x_apikey: str = None,
    limit: int = None
) -> List[str]:
    """
    Mock function to get objects related to a domain.

    Args:
    - domain: string, required, Domain name
    - relationship_type: string, required, Type of relationship
    - x_apikey: string, required, Your API key
    - limit: int, optional, Maximum number of objects to retrieve
    """
    correctness.append({"vt_get_objects_related_to_domain": locals()})
    return ["related_obj1", "related_obj2"]

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
    correctness.append({"vt_validate_historical_ssl_certificates": locals()})
    return True

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
    correctness.append({"vt_get_threat_actors_latest_modification_date": locals()})
    return 1678886400  # Unix timestamp for 2023-03-15

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
    correctness.append({"vt_get_threat_actors_main_source_region": locals()})
    return "North America"  # Example region

def ll_run_tests(response_data):
    """
    Test function that executes both response and ground truth code,
    comparing the functions called to determine if they match.
    """
    try:
        # Initialize test environment
        global correctness
        correctness = []
        
        # Extract code from response
        response_code = response_data.get("result", "") or ""
        ground_truth = response_data.get("ground_truth", "") or ""
        
        # First try with standard pattern for response
        response_match = re.search(r"```python\n(.*?)\n```", response_code, re.DOTALL)
        if response_match:
            response_exec_code = response_match.group(1).strip()
        else:
            # Try with indented code pattern
            response_match = re.search(r"```python\n\s+(.*?)\n```", response_code, re.DOTALL)
            if response_match:
                response_exec_code = response_match.group(1).strip()
            else:
                # Try without the newlines requirement
                response_match = re.search(r"```python(.*?)```", response_code, re.DOTALL)
                if response_match:
                    response_exec_code = response_match.group(1).strip()
                else:
                    response_exec_code = response_code.strip()
            
        print("\nExtracted response code:", response_exec_code)
        
        # Extract ground truth code if it exists
        if ground_truth:
            truth_match = re.search(r"```python\n(.*?)\n```", ground_truth, re.DOTALL)
            if truth_match:
                truth_exec_code = truth_match.group(1).strip()
            else:
                # Try with indented code pattern
                truth_match = re.search(r"```python\n\s+(.*?)\n```", ground_truth, re.DOTALL)
                if truth_match:
                    truth_exec_code = truth_match.group(1).strip()
                else:
                    # Try without the newlines requirement
                    truth_match = re.search(r"```python(.*?)```", ground_truth, re.DOTALL)
                    if truth_match:
                        truth_exec_code = truth_match.group(1).strip()
                    else:
                        truth_exec_code = ground_truth.strip()
                
            print("Extracted ground truth code:", truth_exec_code)
        else:
            truth_exec_code = None
        
        # Skip execution if response code is empty
        if not response_exec_code:
            print("Response code is empty, skipping execution")
            return False
            
        # Check if response code matches a function call pattern
        if not bool(re.match(r'\w+\(.*\)', response_exec_code.strip())):
            print("Response does not contain a valid function call")
            return False
        
        # Prepare execution namespace with all mock functions
        exec_namespace = globals().copy()
        
        # Reset correctness list for response execution
        correctness = []
        
        # Execute response code and track function calls
        print("\nExecuting response code...")
        try:
            exec(response_exec_code, exec_namespace)
            response_calls = copy.deepcopy(correctness)
            print(f"Response execution successful, made {len(response_calls)} function calls")
            
            # If no ground truth provided, return True if execution was successful
            if not truth_exec_code:
                return True
                
            # Reset correctness list for ground truth execution
            correctness = []
            
            # Execute ground truth code and track function calls
            print("\nExecuting ground truth code...")
            try:
                exec(truth_exec_code, exec_namespace)
                truth_calls = copy.deepcopy(correctness)
                print(f"Ground truth execution successful, made {len(truth_calls)} function calls")
                
                # Compare the function calls
                calls_match = response_calls == truth_calls
                print(f"Function calls match: {calls_match}")
                
                return calls_match
                
            except Exception as e:
                print(f"Ground truth execution failed: {str(e)}")
                # If ground truth fails to execute, return False
                return False
            
        except Exception as e:
            print(f"Response execution failed: {str(e)}")
            return False
        
    except Exception as e:
        print(f"Test execution failed: {str(e)}")
        return False

# For direct testing
if __name__ == "__main__":
    # Sample test case
    test_data = {
        "result": "```python\nvt_is_date_within_range(timestamp=vt_get_last_analysis_date_from_report(report=vt_get_ip_address_report(ip='176.762.91.012', x_apikey='6A47Z90')), start='2022/01/01', end='2022/12/31')\n```"
    }
    
    # Run the test
    result = ll_run_tests(test_data)
    print(f"\nTest result: {'PASS' if result else 'FAIL'}")