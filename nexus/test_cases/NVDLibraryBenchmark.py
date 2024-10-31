import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "NVDLibraryBenchmark",
    "description": "Test cases for NVDLibraryBenchmark API calls"
}

# Initialize correctness tracking
correctness = []

# API Function Definitions
def searchCVE(
    cpeName: str = None,
    cveId: str = None,
    cvssV2Metrics: str = None,
    cvssV2Severity: str = None,
    cvssV3Metrics: str = None,
    cvssV3Severity: str = None,
    cweId: str = None,
    hasCertAlerts: bool = None,
    hasCertNotes: bool = None,
    hasKev: bool = None,
    hasOval: bool = None,
    isVulnerable: bool = None,
    keywordExactMatch: bool = None,
    keywordSearch: str = None,
    lastModStartDate: str = None,
    lastModEndDate: str = None,
    noRejected: bool = None,
    pubStartDate: str = None,
    pubEndDate: str = None,
    sourceIdentifier: str = None,
    versionEnd: str = None,
    versionEndType: str = None,
    versionStart: str = None,
    versionStartType: str = None,
    virtualMatchString: str = None,
    limit: int = None,
    delay: int = None,
    key: str = None,
    verbose: bool = None
) -> List[Dict]:
    """
    NVDLib is a Python API wrapper utilizing the REST API provided by NIST for the National Vulnerability Database (NVD). NVDLib CVESearch can search specific CVEs according to the uses requests.

    Args:
    - cpeName: This value will be compared against the CPE Match Criteria within a CVE applicability statement. Partial match strings are allowed.
    - cveId: Returns a single CVE that already exists in the NVD.
    - cvssV2Metrics: This parameter returns only the CVEs that match the provided CVSSv2 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV3Metrics.
    - cvssV2Severity: Find vulnerabilities having a 'LOW', 'MEDIUM', or 'HIGH' version 2 severity.
    - cvssV3Metrics: This parameter returns only the CVEs that match the provided CVSSv3 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV2Metrics.                                                                                                                                                          - cvssV3Severity: Find vulnerabilities having a 'LOW', 'MEDIUM', 'HIGH', or 'CRITICAL' version 3 severity.
    - cweId: Filter collection by CWE (Common Weakness Enumeration) ID. A CVE can have multiple CWE IDs assigned to it.
    - hasCertAlerts: Returns CVE that contain a Technical Alert from US-CERT.
    - hasCertNotes: Returns CVE that contain a Vulnerability Note from CERT/CC.
    - hasOval: Returns CVE that contain information from MITRE's Open Vulnerability and Assessment Language (OVAL) before this transitioned to the Center for Internet Security (CIS).
    - isVulnerable: Returns CVE associated with a specific CPE, where the CPE is also considered vulnerable. REQUIRES cpeName parameter. isVulnerable is not compatible with virtualMatchString parameter.
    - keywordExactMatch: When keywordSearch is used along with keywordExactmatch, it will search the NVD for CVEs containing exactly what was passed to keywordSearch. REQUIRES keywordSearch.
    - keywordSearch: Searches CVEs where a word or phrase is found in the current description. If passing multiple keywords with a space character in between then each word must exist somewhere in the description, not necessarily together unless keywordExactMatch=True is passed to searchCVE.
    - lastModStartDate: This argument has a str with datetime format. These parameters return only the CVEs that were last modified during the specified period. If a CVE has been modified more recently than the specified period, it will not be included in the response. If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days.
    - lastModEndDate: This argument has a str with datetime format. Required if using lastModStartDate.
    - noRejected: Filters out all CVEs that are in a reject or rejected status. Searches without this parameter include rejected CVEs.
    - pubStartDate: This argument has a str with datetime format. These parameters return only the CVEs that were added to the NVD during the specified period. If filtering by the published date, both pubStartDate and pubEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days.
    - pubEndDate: This argument has a str with datetime format. Required if using pubStartDate.
    - sourceIdentifier: Returns CVE where the data source of the CVE is the value that is passed to sourceIdentifier.
    - versionEnd: Must be combined with versionEndType and virtualMatchString. Returns only the CVEs associated with CPEs in specific version ranges.
    - versionEndType: Must be combined with versionEnd and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionEnd, or exclude it.
    - versionStart: Must be combined with versionStartType and virtualMatchString. Returns only CVEs with specific versions. Requests that include versionStart cannot include a version component in the virtualMatchString.
    - versionStartType: Must be combined with versionStart and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionStart, or exclude it.
    - virtualMatchString: A more broad filter compared to cpeName. The cpe match string that is passed to virtualMatchString is compared against the CPE Match Criteria present on CVE applicability statements.
    - limit: Custom argument to limit the number of results of the search. Allowed any number between 1 and 2000.
    - delay: Can only be used if an API key is provided. This allows the user to define a delay. The delay must be greater than 0.6 seconds. The NVD API recommends scripts sleep for at last 6 seconds in between requests.
    - key: NVD API Key. Allows for the user to define a delay. NVD recommends scripts sleep 6 seconds in between requests. If no valid API key is provided, requests are sent with a 6 second delay.
    - verbose: Prints the full NVD API URL for each request.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"searchCVE": locals()})

def searchCPE(
    cpeNameId: str = None,
    cpeMatchString: str = None,
    keywordExactMatch: bool = None,
    keywordSearch: str = None,
    lastModStartDate: str = None,
    lastModEndDate: str = None,
    matchCriteriaId: str = None,
    limit: int = None,
    key: str = None,
    delay: int = 6,
    verbose: bool = None
) -> List[Dict]:
    """
    NVDLib is a Python API wrapper utilizing the REST API provided by NIST for the National Vulnerability Database (NVD). Searching for CPEs is similar to searching for CVEs albeit less parameters. CPE match strings are allowed, meaning if partial strings are known, you can search for all possible CPE names. Like searching CVEs, the parameters are not positional.

    Args:
    - cpeNameId: Returns a specific CPE record using its UUID. If a correctly formatted UUID is passed but it does not exist, it will return empty results. The UUID is the cpeNameId value when searching CPE.
    - cpeMatchString: Use a partial CPE name to search for other CPE names.
    - keywordExactMatch: Searches metadata within CPE title and reference links for an exact match of the phrase or word passed to it. Must be included with keywordSearch.
    - keywordSearch: Returns CPE records where a word or phrase is found in the metadata title or reference links. Space characters act as an AND statement.
    - lastModStartDate: CPE last modification start date. Maximum 120 day range. A start and end date is required. All times are in UTC 00:00. A datetime object or string can be passed as a date. NVDLib will automatically parse the datetime object into the correct format. String Example: "2020-06-28 00:00"
    - lastModEndDate: CPE last modification end date. Maximum 120 day range. Must be included with lastModStartDate. Example: "2020-06-28 00:00"
    - limit: Limits the number of results of the search.
    - key: NVD API Key. Allows for a request every 0.6 seconds instead of 6 seconds.
    - delay: Can only be used if an API key is provided. The amount of time to sleep in between requests. Must be a value above 0.6 seconds if an API key is present. delay is set to 6 seconds if no API key is passed.
    - verbose: Prints the URL request for debugging purposes.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"searchCPE": locals()})


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
