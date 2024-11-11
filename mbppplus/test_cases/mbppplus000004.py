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
inputs = [['Please move back to stream'], ['Jing Eco and Tech'], ['Jhingai wulu road Zone 3'], [''], ['This is a very long string with no words that are at least 4 characters long.'], ['words'], ['with'], ['4'], ['ve'], ['This is a very long string with no arewords that are along.t least 4 charatacters long.is'], ['arewords'], ['This is a very long string with no words that are at llongeast 4 characters long.'], ['arrewords'], ['This is a very long strigng with no words that are at least 4 characters long.'], ['least'], ['arerwordsThis'], ['stralong.t'], ['stralonwith.t'], ['vate'], ['Thicharatactercss'], ['wosrds'], ['vwosrds'], ['llongeast'], ['along.t'], ['vcharacterse'], ['This is a very long string with no arords that are along.t least 4 charatacters long.is'], ['Thicharatactercsvcharacterse'], ['ThicharatacterThis is a very long strigng with no words that are at least 4 characters long.csvcharacterse'], ['ThicharatacterT4his is a very long strigng with no words that are at least 4 characters long.csvcharacterse'], ['arords'], ['This is a very long string with no arewords that are along.t least 4 charatacters lonThis vwosrdsis a very long string with no words that are at least 4 characters long.g.is'], ['long.with'], ['Thicharattactercss'], ['This is a very long string with no alrords that are along.t least 4 charatacters long.is'], ['Thicharataercss'], ['arewds'], ['This is a very long string with no arords that are along.t least 4 charatacters long.isarords'], ['thatvcharacterse'], ['is'], ['tat'], ['stralong..t'], ['s'], ['string'], ['long.g.is'], ['This is a very long gstrigng with no words that are at least 4 characters long.'], ['This is a very long string with no words that are at llongeast 4 charactThis is a very long string with no arewords that are along.t least 4 charatacters lonThis vwosrdsis a very long string with no words that are at least 4 characters long.g.iss long.'], ['vwords'], ['that'], ['characters'], ['woords'], ['vworrds'], ['ThicharatacterThis is a very long strigng  least 4 characters long.csvcharacterse'], ['srtring'], ['This is a very long sarrewordstring with no words that are at llongeast 4 characters long.'], ['long.alrordsg.is'], ['wossrds'], ['This is a very long strigng with no words that are at least 4 characters longcharactThis.'], ['arerwordsThis is a voery long gstrigng with no words that are at least 4 characters long.This'], ['vwdorrdwossrdss'], ['This is a very long string with no words that are at llongeast Thicharatactercssters long.'], ['longlong.This.gwith'], ['vworrrds'], ['charactThis'], ['Tchicharatactercsvcharacterse'], ['stralon'], ['alrords'], ['tast'], ['44'], ['avworrds'], ['srtring44'], ['leaet'], ['ThicharatacterThis'], ['ThicharacterscharattractercssarerwordsThis'], ['vcherse'], ['alrordlonThiss'], ['This is a very long string with no words that are at llongeast Thcharactersicharatactercssters long.'], ['ttat'], ['witth'], ['along.longcharactThis.t'], ['a'], ['at'], ['alrordlonThisllongeasts'], ['tlong.This'], ['ThicharatacterT4his is a very long strigng with no words that arevery at least 4 charactiers long.csvcharacterse'], ['srtrinrg'], ['tlong.TgstrignThcharactersicharatactercsstersghis'], ['wwith'], ['stringtast'], ['wilong.alrordsg.is'], ['long.This'], ['osrds'], ['stringtaststralong.t'], ['srtnoring'], ['vee'], ['ThicharatacterThis is a very long strigng with no words that are at least t4 characters long.csvcharacterse'], ['averyrewords'], ['thavworrdsat'], ['This is a very long string with no words that are at lllongeastcharacters long.'], ['stralong..ts'], ['thatvcharaccharactiersterthavworrdsatse'], ['loleaetg'], ['wwitThish'], ['aa'], ['atare'], ['avaeryrewords']]
results = [['Please', 'move', 'back', 'stream'], ['Jing', 'Tech'], ['Jhingai', 'wulu', 'road', 'Zone'], [], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'least', 'characters', 'long'], ['words'], ['with'], [], [], ['This', 'very', 'long', 'string', 'with', 'arewords', 'that', 'along', 'least', 'charatacters', 'long'], ['arewords'], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'llongeast', 'characters', 'long'], ['arrewords'], ['This', 'very', 'long', 'strigng', 'with', 'words', 'that', 'least', 'characters', 'long'], ['least'], ['arerwordsThis'], ['stralong'], ['stralonwith'], ['vate'], ['Thicharatactercss'], ['wosrds'], ['vwosrds'], ['llongeast'], ['along'], ['vcharacterse'], ['This', 'very', 'long', 'string', 'with', 'arords', 'that', 'along', 'least', 'charatacters', 'long'], ['Thicharatactercsvcharacterse'], ['ThicharatacterThis', 'very', 'long', 'strigng', 'with', 'words', 'that', 'least', 'characters', 'long', 'csvcharacterse'], ['ThicharatacterT4his', 'very', 'long', 'strigng', 'with', 'words', 'that', 'least', 'characters', 'long', 'csvcharacterse'], ['arords'], ['This', 'very', 'long', 'string', 'with', 'arewords', 'that', 'along', 'least', 'charatacters', 'lonThis', 'vwosrdsis', 'very', 'long', 'string', 'with', 'words', 'that', 'least', 'characters', 'long'], ['long', 'with'], ['Thicharattactercss'], ['This', 'very', 'long', 'string', 'with', 'alrords', 'that', 'along', 'least', 'charatacters', 'long'], ['Thicharataercss'], ['arewds'], ['This', 'very', 'long', 'string', 'with', 'arords', 'that', 'along', 'least', 'charatacters', 'long', 'isarords'], ['thatvcharacterse'], [], [], ['stralong'], [], ['string'], ['long'], ['This', 'very', 'long', 'gstrigng', 'with', 'words', 'that', 'least', 'characters', 'long'], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'llongeast', 'charactThis', 'very', 'long', 'string', 'with', 'arewords', 'that', 'along', 'least', 'charatacters', 'lonThis', 'vwosrdsis', 'very', 'long', 'string', 'with', 'words', 'that', 'least', 'characters', 'long', 'long'], ['vwords'], ['that'], ['characters'], ['woords'], ['vworrds'], ['ThicharatacterThis', 'very', 'long', 'strigng', 'least', 'characters', 'long', 'csvcharacterse'], ['srtring'], ['This', 'very', 'long', 'sarrewordstring', 'with', 'words', 'that', 'llongeast', 'characters', 'long'], ['long', 'alrordsg'], ['wossrds'], ['This', 'very', 'long', 'strigng', 'with', 'words', 'that', 'least', 'characters', 'longcharactThis'], ['arerwordsThis', 'voery', 'long', 'gstrigng', 'with', 'words', 'that', 'least', 'characters', 'long', 'This'], ['vwdorrdwossrdss'], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'llongeast', 'Thicharatactercssters', 'long'], ['longlong', 'This', 'gwith'], ['vworrrds'], ['charactThis'], ['Tchicharatactercsvcharacterse'], ['stralon'], ['alrords'], ['tast'], [], ['avworrds'], ['srtring44'], ['leaet'], ['ThicharatacterThis'], ['ThicharacterscharattractercssarerwordsThis'], ['vcherse'], ['alrordlonThiss'], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'llongeast', 'Thcharactersicharatactercssters', 'long'], ['ttat'], ['witth'], ['along', 'longcharactThis'], [], [], ['alrordlonThisllongeasts'], ['tlong', 'This'], ['ThicharatacterT4his', 'very', 'long', 'strigng', 'with', 'words', 'that', 'arevery', 'least', 'charactiers', 'long', 'csvcharacterse'], ['srtrinrg'], ['tlong', 'TgstrignThcharactersicharatactercsstersghis'], ['wwith'], ['stringtast'], ['wilong', 'alrordsg'], ['long', 'This'], ['osrds'], ['stringtaststralong'], ['srtnoring'], [], ['ThicharatacterThis', 'very', 'long', 'strigng', 'with', 'words', 'that', 'least', 'characters', 'long', 'csvcharacterse'], ['averyrewords'], ['thavworrdsat'], ['This', 'very', 'long', 'string', 'with', 'words', 'that', 'lllongeastcharacters', 'long'], ['stralong'], ['thatvcharaccharactiersterthavworrdsatse'], ['loleaetg'], ['wwitThish'], [], ['atare'], ['avaeryrewords']]

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
        func_name = "find_char_long"
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
        for test_case in ["assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])", "assert set(find_char_long('Jing Eco and Tech')) == set(['Jing', 'Tech'])", "assert set(find_char_long('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])"]:
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
