import re
import json
import copy
from typing import List, Dict, Tuple, Any, Union

METADATA = {
    "subset": "CVECPEAPIBenchmark",
    "description": "Test cases for CVECPEAPIBenchmark API calls"
}

# Initialize correctness tracking
correctness = []

def pre_initialization():
    """Reset the correctness list before each test run"""
    global correctness
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
    correctness.append({"count_cvecpe_items": locals()})
    return len(cvecpeList) if cvecpeList else 0

def summarize_cvecpes(
    cvecpeList: List[Dict]
) -> Dict:
    """
    This function can summarize the contents of provided CVE or CPE items.

    Args:
    - cvecpeList: This arg takes in a list of CVE or CPE items.
    """
    correctness.append({"summarize_cvecpes": locals()})
    return {"total": len(cvecpeList), "types": ["CVE", "CPE"]} if cvecpeList else {}

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
    correctness.append({"verify_and_process_data_range_start": locals()})
    return startdate  # Mock implementation returns the original startdate

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
    correctness.append({"verify_and_process_data_range_end": locals()})
    return enddate  # Mock implementation returns the original enddate

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
    correctness.append({"compare_cvecpes": locals()})
    return {"common": 1, "differences": 2}  # Mock result

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
    correctness.append({"search_backup_keywords": locals()})
    if cvecpeList:
        return cvecpeList
    else:
        # Mock implementation, return sample data
        return [{"id": "CVE-2023-1234", "keyword": backup_keyword}]

def getCPEName(
    cpeObject: Dict
) -> str:
    """
    This function takes a CPE object and extracts the CPE name.

    Args:
    - cpeObject: A CPE object from which the CPE name is to be extracted. The object should have a 'cpeName' field.
    """
    correctness.append({"getCPEName": locals()})
    return cpeObject.get('cpeName', 'cpe:/a:example:product:1.0')

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

def countCVEsBySeverity(
    cve_list: List[Dict]
) -> Dict[str, int]:
    """
    Analyze a list of CVE objects, and return a dictionary with counts of CVEs according to their 'cvssV3Severity' (LOW, MEDIUM, HIGH, CRITICAL).

    Args:
    - cve_list: A list of dictionary objects each representing a CVE. Each dictionary should include a 'cvssV3Severity' key.
    """
    correctness.append({"countCVEsBySeverity": locals()})
    return {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}

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
    correctness.append({"sortCVEsByCVSSv3Score": locals()})
    return cve_list  # Mock implementation returns the original list

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
    correctness.append({"sortCVEsByCVSSv2Score": locals()})
    return cve_list  # Mock implementation returns the original list

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
    correctness.append({"sortCVEsByModDate": locals()})
    return cve_list  # Mock implementation returns the original list

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
    correctness.append({"filterCVEByLanguage": locals()})
    return [cve for cve in cve_list if cve.get('language') == language] if cve_list else []

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
    correctness.append({"filterCVEsBySeverity": locals()})
    filtered_list = []
    if cveList and severityLevel:
        for cve in cveList:
            if cve.get('cvssV3Severity') == severityLevel or cve.get('cvssV2Severity') == severityLevel:
                filtered_list.append(cve)
    return filtered_list

def filterDeprecatedCPEs(
    cpeList: List[Dict]
) -> List[Dict]:
    """
    Loop through the CPE objects in the list and return the ones that are not deprecated.

    Args:
    - cpeList: A list of CPE objects. Each CPE object in the list has a 'deprecated' key. If the value of this key is False, it means the CPE object is not deprecated.
    """
    correctness.append({"filterDeprecatedCPEs": locals()})
    return [cpe for cpe in cpeList if not cpe.get('deprecated', False)] if cpeList else []

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
    correctness.append({"sortCPEsByLastMod": locals()})
    return cpeList  # Mock implementation returns the original list

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
    correctness.append({"mergeCVEs": locals()})
    return (list1 or []) + (list2 or [])

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
    correctness.append({"mergeCPEs": locals()})
    return (list1 or []) + (list2 or [])

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
    correctness.append({"searchCVE": locals()})
    # Mock implementation
    return [
        {"id": "CVE-2023-1234", "description": "Sample CVE for testing", "cvssV3Severity": "HIGH"}
    ]

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
    correctness.append({"searchCPE": locals()})
    # Mock implementation
    return [
        {"cpeName": "cpe:/a:example:product:1.0", "title": "Example Product", "deprecated": False}
    ]

def ll_run_tests(response_data):
    """
    Test function that simply executes the provided code.
    This version focuses on execution rather than comparison.
    """
    try:
        # Initialize test environment
        global correctness
        correctness = []
        
        # Extract code from response
        response_code = response_data.get("result", "") or ""
        
        # First try with standard pattern
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
        
        # Skip execution if code is empty
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
            
            # Always return True if execution was successful
            return True
            
        except Exception as e:
            print(f"Response execution failed: {str(e)}")
            return False
        
    except Exception as e:
        print(f"Test execution failed: {str(e)}")
        return False