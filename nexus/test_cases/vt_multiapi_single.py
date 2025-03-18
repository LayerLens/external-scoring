import re
import json
import copy

# Global tracking list for function calls
correctness = []

# MOCK FUNCTIONS - these simulate the VirusTotal API functions
def vt_get_ip_address_report(ip=None, x_apikey=None):
    """Mock function that simulates retrieving an IP address report"""
    correctness.append({"vt_get_ip_address_report": locals()})
    return {"data": "mock_report"}

def vt_get_domain_report(domain=None, x_apikey=None):
    """Mock function that simulates retrieving a domain report"""
    correctness.append({"vt_get_domain_report": locals()})
    return {"data": "mock_domain_report"}

def vt_get_last_analysis_date_from_report(report=None):
    """Mock function that simulates extracting the last analysis date"""
    correctness.append({"vt_get_last_analysis_date_from_report": locals()})
    return 1640995200  # Example timestamp: 2022-01-01

def vt_is_date_within_range(timestamp=None, start=None, end=None):
    """Mock function that simulates checking if a date is within a range"""
    correctness.append({"vt_is_date_within_range": locals()})
    return True

def vt_get_multiple_domain_reports(domains=None, x_apikey=None):
    """Mock function that simulates retrieving multiple domain reports"""
    correctness.append({"vt_get_multiple_domain_reports": locals()})
    return [{"data": "mock_report"}]

def vt_get_comments_on_domain(domain=None, x_apikey=None, limit=None):
    """Mock function that simulates retrieving comments on a domain"""
    correctness.append({"vt_get_comments_on_domain": locals()})
    return ["comment1", "comment2"]

def vt_get_comments_on_ip_address(ip=None, x_apikey=None):
    """Mock function that simulates retrieving comments on an IP address"""
    correctness.append({"vt_get_comments_on_ip_address": locals()})
    return ["comment1", "comment2"]

def count_items_in_list(input_list=None):
    """Mock function that simulates counting items in a list"""
    correctness.append({"count_items_in_list": locals()})
    return len(input_list) if input_list else 0

def calculate_sum_of_numbers(num1=None, num2=None):
    """Mock function that simulates calculating the sum of two numbers"""
    correctness.append({"calculate_sum_of_numbers": locals()})
    return (num1 or 0) + (num2 or 0)

def extract_resolution_date(dns_res_obj=None):
    """Mock function that simulates extracting a resolution date"""
    correctness.append({"extract_resolution_date": locals()})
    return 1678886400  # Example timestamp

def vt_get_dns_resolution_object(id=None, x_apikey=None):
    """Mock function that simulates retrieving a DNS resolution object"""
    correctness.append({"vt_get_dns_resolution_object": locals()})
    return {"domain": "example.com", "ip_address": "192.168.1.1", "date": 1678886400}

def vt_get_objects_related_to_ip_address(ip=None, relationship=None, x_apikey=None):
    """Mock function that simulates retrieving objects related to an IP address"""
    correctness.append({"vt_get_objects_related_to_ip_address": locals()})
    return ["object1", "object2"]

def vt_get_objects_related_to_domain(domain=None, relationship=None, x_apikey=None):
    """Mock function that simulates retrieving objects related to a domain"""
    correctness.append({"vt_get_objects_related_to_domain": locals()})
    return ["subdomain1", "subdomain2"]

def vt_validate_historical_ssl_certificates(historical_ssl_certificates=None, x_apikey=None):
    """Mock function that simulates validating historical SSL certificates"""
    correctness.append({"vt_validate_historical_ssl_certificates": locals()})
    return True

def get_random_object_from_list(list_of_objects=None):
    """Mock function that simulates getting a random object from a list"""
    correctness.append({"get_random_object_from_list": locals()})
    return list_of_objects[0] if list_of_objects else None

def vt_add_comment_to_ip_address(ip=None, comment=None, x_apikey=None):
    """Mock function that simulates adding a comment to an IP address"""
    correctness.append({"vt_add_comment_to_ip_address": locals()})
    return True

def vt_get_threat_actors_latest_modification_date(threat_actor_objects=None, x_apikey=None):
    """Mock function that simulates retrieving the latest modification date for threat actors"""
    correctness.append({"vt_get_threat_actors_latest_modification_date": locals()})
    return 1646092800  # Example timestamp: 2022-03-01

def pre_initialization():
    """
    Called by the test runner before running tests.
    This function resets the global state.
    """
    global correctness
    correctness = []

def ll_run_tests(response_data):
    """
    Test function for API call validation following the Nexus benchmark approach.
    Key points:
    1. Compare actual function calls made rather than code text
    2. Execute both response and ground truth code separately
    3. Track and compare function calls through the global correctness list
    4. Robust error handling and code extraction
    """
    try:
        # Initialize test environment
        global correctness
        correctness = []
        
        # Extract code from ground truth - handle empty or null cases
        ground_truth = response_data.get("truth", "") or ""
        ground_truth_match = re.search(r"```python\n(.*?)\n```", ground_truth, re.DOTALL)
        if ground_truth_match:
            ground_truth_code = ground_truth_match.group(1).strip()
        else:
            # Try without the newlines requirement
            ground_truth_match = re.search(r"```python(.*?)```", ground_truth, re.DOTALL)
            if ground_truth_match:
                ground_truth_code = ground_truth_match.group(1).strip()
            else:
                ground_truth_code = ground_truth.strip()
            
        print("\nExtracted ground truth code:", ground_truth_code)
        
        # Extract code from response - handle empty or null cases
        response_code = response_data.get("result", "") or ""
        response_match = re.search(r"```python\n(.*?)\n```", response_code, re.DOTALL)
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
        
        # Skip execution if code is empty
        if not response_exec_code:
            print("Response code is empty, skipping execution")
            return False
            
        # Check if response code matches a function call pattern
        if not bool(re.match(r'\w+\(.*\)', response_exec_code.strip())):
            print("Response does not contain a valid function call")
            return False
        
        # Prepare execution namespace with all mock functions
        exec_namespace = {
            'correctness': correctness,
            'vt_get_ip_address_report': vt_get_ip_address_report,
            'vt_get_domain_report': vt_get_domain_report,
            'vt_get_last_analysis_date_from_report': vt_get_last_analysis_date_from_report,
            'vt_is_date_within_range': vt_is_date_within_range,
            'vt_get_multiple_domain_reports': vt_get_multiple_domain_reports,
            'vt_get_comments_on_domain': vt_get_comments_on_domain,
            'vt_get_comments_on_ip_address': vt_get_comments_on_ip_address,
            'count_items_in_list': count_items_in_list,
            'calculate_sum_of_numbers': calculate_sum_of_numbers,
            'extract_resolution_date': extract_resolution_date,
            'vt_get_dns_resolution_object': vt_get_dns_resolution_object,
            'vt_get_objects_related_to_ip_address': vt_get_objects_related_to_ip_address,
            'vt_get_objects_related_to_domain': vt_get_objects_related_to_domain,
            'vt_validate_historical_ssl_certificates': vt_validate_historical_ssl_certificates,
            'get_random_object_from_list': get_random_object_from_list,
            'vt_add_comment_to_ip_address': vt_add_comment_to_ip_address,
            'vt_get_threat_actors_latest_modification_date': vt_get_threat_actors_latest_modification_date,
        }
        
        # Execute response code and track function calls
        print("\nExecuting response code...")
        try:
            exec(response_exec_code, exec_namespace)
            response_calls = copy.deepcopy(correctness)
            print(f"Response execution successful, made {len(response_calls)} function calls")
        except Exception as e:
            print(f"Response execution failed: {str(e)}")
            return False
        
        # Skip comparison if ground truth is empty or no function calls were made
        if not ground_truth_code:
            print("Ground truth code is empty, skipping comparison")
            return False
            
        if not response_calls:
            print("No function calls were made by the response code")
            return False
        
        # Reset correctness list and execute ground truth
        correctness = []
        try:
            exec(ground_truth_code, exec_namespace)
            ground_truth_calls = copy.deepcopy(correctness)
            print(f"Ground truth execution successful, made {len(ground_truth_calls)} function calls")
        except Exception as e:
            print(f"Ground truth execution failed: {str(e)}")
            return False
        
        # Reset correctness list for future use
        correctness = []
        
        # Compare function calls (this is the key approach - comparing actual calls not code text)
        if response_calls == ground_truth_calls:
            print("✅ Function calls match exactly!")
            return True
        else:
            # Print detailed comparison for debugging
            print("❌ Function calls mismatch")
            print(f"Response calls: {response_calls}")
            print(f"Ground truth calls: {ground_truth_calls}")
            return False
        
    except Exception as e:
        print(f"Test execution failed: {str(e)}")
        return False

# For direct testing
if __name__ == "__main__":
    # Sample test case
    test_data = {
        "truth": "```python\nvt_is_date_within_range(vt_get_last_analysis_date_from_report(vt_get_ip_address_report(ip='176.762.91.012', x_apikey='6A47Z90')), start='2022/01/01', end='2022/12/31')\n```",
        "result": "```python\nvt_is_date_within_range(timestamp=vt_get_last_analysis_date_from_report(report=vt_get_ip_address_report(ip='176.762.91.012', x_apikey='6A47Z90')), start='2022/01/01', end='2022/12/31')\n```"
    }
    
    # Run the test
    result = ll_run_tests(test_data)
    print(f"\nTest result: {'PASS' if result else 'FAIL'}")