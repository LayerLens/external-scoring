import numpy as np
[]

def is_floats(x) -> bool:
    """Helper function to check float values for comparison"""
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    """Custom assertion function that handles float comparisons"""
    # Special handling for booleans
    if isinstance(out, bool) or isinstance(exp, bool):
        assert out == exp, f"out: {out}, exp: {exp}"
        return
        
    # Float comparison setup
    if atol == 0 and is_floats(exp):
        atol = 1e-6
    
    # Handle set conversion for sequences
    if isinstance(out, (list, tuple)) and isinstance(exp, (list, tuple)):
        out = set(out)
        exp = set(exp)
    
    # Do the actual comparison
    if out != exp and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert out == exp, f"out: {out}, exp: {exp}"

# Test data
inputs = [['clearly!! we can see the sky'], ['seriously!! there are many roses'], ['unfortunately!! sita is going to home'], ['heavily and quickly we ran down the steep hill'], ['they swiftly and silently tiptoed through the dark room'], ['quickly and quietly, the bird flew away'], ['flew'], ['they swiftly and silentlywe tiptoed through the dark room'], ['swiftly'], ['dhillrk'], ['quicklthey flew away'], ['they swiftly and silentlywe tiptoede through the dark room'], ['and'], ['they'], ['dark'], ['awaquicklyy'], ['ran'], ['andran'], ['they swiftly and silently tiptoed thr ough the dark room'], ['ttiptoed'], ['they swiftly and silentlywe tiptoede through the dark om'], ['ann'], ['ythey'], ['dhilllrk'], ['they swiftly and silentlywe dtiptoede through the dark om'], ['darkran'], ['yththey swiftly and silently tiptoed through the dark roomey'], ['they swiftly and silently tiptoedd through the dark room'], ['dhillhrdtiptoedek'], ['aran'], ['awaquickalyy'], ['silentlywe'], ['tsilentyhey'], ['annthey'], ['quietly,'], ['awfayfle'], ['tthey swiftly and silently tiptoed through the dark roomheey'], ['fswiftlylew'], ['dathey swiftly and silentlywe tiptoede through the dark roomrk'], ['they swiftly and silentlywe tiptoed th rough the dark room'], ['roomey'], ['they sdhilllrkwiftly and silentlywe tiptoede through the dark room'], ['awfsilentlyayfle'], ['yt'], ['they roomswiftly and silentlywe dtiptoede through the dark om'], ['hj'], ['dathey swiftly and silentlywe tiptoede thandranrk'], ['awefsilentlyayfle'], ['they swiftly and sittiptoedlentlywe tiptoed th rough the dark room'], ['room'], ['awilentlyayfle'], ['ough'], ['bird'], ['they swiftly and sittiptoedlentlywe h rough the dark r'], ['they swiftly and sittiptoedlentlywe tiptoed th rthroughough the dark room'], ['roomrk'], ['dtiptoede'], ['away'], ['heavily'], ['awfsilentlyale'], ['dhillhrdtiptoed'], ['quroom flew away'], ['dathey swiftly and silentlywe tndranrk'], ['thesdhilllrkwiftlyy swiftly and silentlywe tiptoede through the dark om'], ['dathey swiftly and silentlywe tiyt'], ['quickly and quietldtiptoedey, the bird flew away'], ['quickly anrand quietly, the bird flew away'], ['dhililrk'], ['darak'], ['thesdhilllrkwiftlyy'], ['rdathey swiftly and silentlywe tndranrkugh'], ['quickly anhe bird flew away'], ['fswiftlysilentlywellew'], ['theyfswiftlysilentlywellewy and silentlywe dtiptoede through the dark om'], ['quietheavilyly,'], ['htthey swiftly and silently tiptoed through the dark roomheeyj'], ['they swiftly and silentlywe tiptoed th rough ethe dsdhilllrkwiftlyark room'], ['quicklydehillhrdtiptoed'], ['oroweomrk'], ['dhk'], ['tiptoedthandranrkd'], ['sOlS'], ['dand silentlywfe tndranrk'], ['they swiftly and sittiptoedlentlywe tiptoed th rough tdhde dark room'], ['quickly and quietldtiptoedey, the bird flroomheeyew away'], ['they swiftly and silroomentlywe tiptoede through the dark room'], ['thesdquroom flew awayitlyy'], ['thesdhtlyy'], ['they swiftly and silroomentlywe tiptoede through the dark rooom'], ['awfafle'], ['tiptoed'], ['dathey swiftly and silentlywesilesntly tndranrk'], ['BesPtviFH'], ['awaquiyckalyy'], ['anhe'], ['fswiftlysilentlywe'], ['tsdhilllrkwiftlytiptoed'], ['thr'], ['theyfswiftlysilentlywellewy and silentlywe dtiptoede throrugh the dark om'], ['fleww'], [''], ['they swiftly and silentlyy tiptoed through the dark room'], ['arran'], ['othey swiftly and silroomentlywe tiptoede through the dark roomughh'], ['t'], ['BeFsPtviFFH']]
results = [(0, 7, 'clearly'), (0, 9, 'seriously'), (0, 13, 'unfortunately'), (0, 7, 'heavily'), (5, 12, 'swiftly'), (0, 7, 'quickly'), None, (5, 12, 'swiftly'), (0, 7, 'swiftly'), None, None, (5, 12, 'swiftly'), None, None, None, (0, 10, 'awaquickly'), None, None, (5, 12, 'swiftly'), None, (5, 12, 'swiftly'), None, None, None, (5, 12, 'swiftly'), None, (8, 15, 'swiftly'), (5, 12, 'swiftly'), None, None, (0, 11, 'awaquickaly'), (0, 8, 'silently'), None, None, (0, 7, 'quietly'), None, (6, 13, 'swiftly'), (0, 8, 'fswiftly'), (7, 14, 'swiftly'), (5, 12, 'swiftly'), None, (5, 20, 'sdhilllrkwiftly'), (0, 11, 'awfsilently'), None, (5, 16, 'roomswiftly'), None, (7, 14, 'swiftly'), (0, 12, 'awefsilently'), (5, 12, 'swiftly'), None, (0, 9, 'awilently'), None, None, (5, 12, 'swiftly'), (5, 12, 'swiftly'), None, None, None, (0, 7, 'heavily'), (0, 11, 'awfsilently'), None, None, (7, 14, 'swiftly'), (0, 18, 'thesdhilllrkwiftly'), (7, 14, 'swiftly'), (0, 7, 'quickly'), (0, 7, 'quickly'), None, None, (0, 18, 'thesdhilllrkwiftly'), (8, 15, 'swiftly'), (0, 7, 'quickly'), (0, 16, 'fswiftlysilently'), (0, 20, 'theyfswiftlysilently'), (0, 14, 'quietheavilyly'), (7, 14, 'swiftly'), (5, 12, 'swiftly'), (0, 7, 'quickly'), None, None, None, None, (5, 13, 'silently'), (5, 12, 'swiftly'), (0, 7, 'quickly'), (5, 12, 'swiftly'), (17, 25, 'awayitly'), (0, 9, 'thesdhtly'), (5, 12, 'swiftly'), None, None, (7, 14, 'swiftly'), None, (0, 12, 'awaquiyckaly'), None, (0, 16, 'fswiftlysilently'), (0, 16, 'tsdhilllrkwiftly'), None, (0, 20, 'theyfswiftlysilently'), None, None, (5, 12, 'swiftly'), None, (6, 13, 'swiftly'), None, None]

def ll_run_tests(response_data):
    """
    Main test function for code evaluation.
    Args:
        response_data: Dict containing response code
    Returns:
        bool: True if all test cases pass
    """
    try:
        # Initialize test environment
        global_namespace = {
            'np': np,
            'assertion': assertion,
            'is_floats': is_floats,
            'inputs': inputs,
            'results': results
        }
        
        # Execute solution code
        response_code = response_data.get('parsed_result', response_data.get('result', ''))
        exec(response_code, global_namespace)
        
        # Verify function exists
        func_name = "find_adverb_position"
        if func_name not in global_namespace:
            print(f"Function '{func_name}' not found in response")
            return False
        
        # Execute tests
        solution_func = global_namespace[func_name]
        
        # Run input/output tests
        for i, (test_input, expected) in enumerate(zip(inputs, results)):
            try:
                result = solution_func(*test_input)
                assertion(result, expected, 0)
            except AssertionError as e:
                print(f"Test case {i} failed: {str(e)}")
                print(f"Input: {test_input}")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                return False
        
        # Run assertion-based tests if any
        for test_case in ['assert find_adverb_position("clearly!! we can see the sky")==(0, 7, \'clearly\')', 'assert find_adverb_position("seriously!! there are many roses")==(0, 9, \'seriously\')', 'assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, \'unfortunately\')']:
            try:
                exec(test_case, global_namespace)
            except AssertionError as e:
                print(f"Assertion test failed: {str(e)}")
                print(f"Test case: {test_case}")
                return False
            
        return True
            
    except Exception as e:
        print(f"Error during test execution: {str(e)}")
        return False
