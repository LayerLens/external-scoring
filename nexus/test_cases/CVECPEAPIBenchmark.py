import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "CVECPEAPIBenchmark",
    "description": "Test cases for CVECPEAPIBenchmark API calls"
}

# Initialize correctness tracking
correctness = []

# API Function Definitions
def count_cvecpe_items(
    cvecpeList: List[Dict]
) -> int:
    """
    This function counts the total number of CVE and CPE items provided in the arg.

    Args:
    - cvecpeList: This arg takes in a list of CVE or CPE items.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"count_cvecpe_items": locals()})

def summarize_cvecpes(
    cvecpeList: List[Dict]
) -> Dict:
    """
    This function can summarize the contents of provided CVE or CPE items.

    Args:
    - cvecpeList: This arg takes in a list of CVE or CPE items.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"summarize_cvecpes": locals()})

def verify_and_process_data_range_start(
    startdate: str,
    enddate: str
) -> str:
    """
    This function can verify whether the range of dates being searched is within 3 months. If true, it returns the original startdate. If not, it will automatically truncate and return an appropriate startdate resulting in a 3-month time span. Note that searchCVE or searchCPE cannot handle time span longer than 3 months.

    Args:
    - startdate: The start date of the searched time span.
    - enddate: The end date of the searched time span.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"verify_and_process_data_range_start": locals()})

def verify_and_process_data_range_end(
    startdate: str,
    enddate: str
) -> str:
    """
    This function can verify whether the range of dates being searched is within 3 months. If true, it returns the original enddate. If not, it will automatically truncate and return an appropriate enddate resulting in a 3-month time span. Note that searchCVE or searchCPE cannot handle time span longer than 3 months.

    Args:
    - startdate: The start date of the searched time span.
    - enddate: The end date of the searched time span.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"verify_and_process_data_range_end": locals()})

def compare_cvecpes(
    cvecpeList1: List[Dict],
    cvecpeList2: List[Dict]
) -> Dict:
    """
    This function can compare the contents of two lists of provided CVE or CPE items, summarizing the common parts and differences between the two lists.

    Args:
    - cvecpeList1: This arg takes in a list of CVE or CPE items to compare with another list.
    - cvecpeList2: This arg takes in a list of CVE or CPE items to compare with another list.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"compare_cvecpes": locals()})

def search_backup_keywords(
    cvecpeList: List[Dict],
    backup_keyword: str
) -> List[Dict]:
    """
    This function takes in a backup keyword and a list of CVE or CPE items found by an initial searchCVE or searchCPE. If the list is empty, the function will search again using the backup keyword instead of the original keyword. If it is not empty, the function returns the original searched results.

    Args:
    - cvecpeList: This arg takes in a list of CVE or CPE items.
    - backup_keyword: The backup keyword to search if the original keyword doesn't lead to corresponding results.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"search_backup_keywords": locals()})

def getCPEName(
    cpeObject: Dict
) -> str:
    """
    This function takes a CPE object and extracts the CPE name.

    Args:
    - cpeObject: A CPE object from which the CPE name is to be extracted. The object should have a 'cpeName' field.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"getCPEName": locals()})

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

def countCVEsBySeverity(
    cve_list: List[Dict]
) -> Dict[str, int]:
    """
    Analyze a list of CVE objects, and return a dictionary with counts of CVEs according to their 'cvssV3Severity' (LOW, MEDIUM, HIGH, CRITICAL).

    Args:
    - cve_list: A list of dictionary objects each representing a CVE. Each dictionary should include a 'cvssV3Severity' key.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"countCVEsBySeverity": locals()})

def sortCVEsByCVSSv3Score(
    cve_list: List[Dict],
    descending: bool = True
) -> List[Dict]:
    """
    Accepts a list of CVE objects and sorts them by their CVSS Version 3.x base scores. If a CVE object does not contain a CVSS v3 score, it is assumed to have the lowest possible score (i.e., 0).

    Args:
    - cve_list: List of CVE objects, where each object contains details such as CVE identifier, CVSS v2 and v3 scores, etc.
    - descending: If set to True, the list will be sorted in descending order (highest CVSSv3Score first).
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"sortCVEsByCVSSv3Score": locals()})

def sortCVEsByCVSSv2Score(
    cve_list: List[Dict],
    descending: bool = True
) -> List[Dict]:
    """
    Accepts a list of CVE objects and sorts them by their CVSS Version 2.0 base scores. If a CVE object does not contain a CVSS v2 score, it is assumed to have the lowest possible score (i.e., 0).

    Args:
    - cve_list: List of CVE objects, where each object contains details such as CVE identifier, CVSS v2 and v3 scores, etc.
    - descending: If set to True, the list will be sorted in descending order (highest CVSSv2Score first). Defaults to True.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"sortCVEsByCVSSv2Score": locals()})

def sortCVEsByModDate(
    cve_list: List[Dict],
    descending: bool = True
) -> List[Dict]:
    """
    This function sorts a list of CVE objects by their last modification date.

    Args:
    - cve_list: A list of CVE objects. Each object should at least have a property for last modification date.
    - descending: If set to True, the list will be sorted in descending order (most recently modified first).
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"sortCVEsByModDate": locals()})

def filterCVEByLanguage(
    cve_list: List[Dict],
    language: str
) -> List[Dict]:
    """
    Filters a collection of CVE (Common Vulnerabilities and Exposures) objects and returns a list of the ones that have descriptions for a specific language.

    Args:
    - cve_list: A list of CVE objects. Each object should contain information about a particular CVE, including its description available in various languages.
    - language: Language code for which the function will check in the description field of the CVE objects. This must follow the ISO 639-1 language codes, such as 'en' for English, 'es' for Spanish, and 'de' for German, etc.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"filterCVEByLanguage": locals()})

def filterCVEsBySeverity(
    cveList: List[Dict],
    severityLevel: str
) -> List[Dict]:
    """
    Returns a list of CVE objects from the given collection that have the provided severity level.

    Args:
    - cveList: List of objects containing a collection of CVEs. Each CVE object is expected to have 'cvssV2Severity' and/or 'cvssV3Severity' properties reflecting the severity level of the vulnerability.
    - severityLevel: The severity level with which to filter the CVEs. Accepts 'LOW', 'MEDIUM', 'HIGH' for both 'cvssV2Severity' and 'cvssV3Severity', and 'CRITICAL' for 'cvssV3Severity' only.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"filterCVEsBySeverity": locals()})

def filterDeprecatedCPEs(
    cpeList: List[Dict]
) -> List[Dict]:
    """
    Loop through the CPE objects in the list and return the ones that are not deprecated.

    Args:
    - cpeList: A list of CPE objects. Each CPE object in the list has a 'deprecated' key. If the value of this key is False, it means the CPE object is not deprecated.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"filterDeprecatedCPEs": locals()})

def sortCPEsByLastMod(
    cpeList: List[Dict],
    descending: bool = True
) -> List[Dict]:
    """
    Sorts a list of object collections of CPEs by their last modification time.

    Args:
    - cpeList: The list of object collections of CPEs that need to be sorted. Each object collection has a lastModified field.
    - descending: Determines the order of sort. If True, CPEs will be sorted in descending order of 'last modification time'. If False, the sorting will be in descending order.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"sortCPEsByLastMod": locals()})

def mergeCVEs(
    list1: List[Dict],
    list2: List[Dict]
) -> List[Dict]:
    """
    This function takes two lists of objects each containing a collection of CVEs, and combines them into a single list.

    Args:
    - list1: First list of objects each holding details of a CVE. Defined by NVD format.
    - list2: Second list of objects each holding details of a CVE. Defined by NVD format.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"mergeCVEs": locals()})

def mergeCPEs(
    list1: List[Dict],
    list2: List[Dict]
) -> List[Dict]:
    """
    Combines two lists of CPEs into one.

    Args:
    - list1: List of CPEs. Each object in the list should contain a collection of CPEs.
    - list2: Another list of CPEs. Each object in this list should also contain a collection of CPEs.
    """
    args_dict = locals()
    args_dict.pop("kwargs", None)  # Remove kwargs if it exists
    return_dict = {}
    for key, value in args_dict.items():
        if value:
          return_dict[key] = value
    correctness.append({"mergeCPEs": locals()})

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
