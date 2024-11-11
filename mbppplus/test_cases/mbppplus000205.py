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
inputs = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[10, 20, 30]], [[12, 15]], [[]], [[-1, 0, 1, -2, 3, -4]], [[1, 2.5, 3, -4.7, 5, 6, 7, -8.9]], [[-5, -10, -15]], [[1000000]], [[1, 2.5, 3, -4.7, 5, 6, 7, -8.72172602966587]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686]], [[0, -5, -10, -15]], [[0, -5, -15]], [[0, 0, -5, -15]], [[1, 2.5, -4.7, 5, 7, 7, -8.9]], [[1000000, 1000000]], [[0, 0, -5, -15, 0]], [[1, 2.5, -4.7, 5, 7, 7, -8.9, -8.9]], [[0, 0, -5, -15, -15]], [[0, 0, -4, -15]], [[-6, 0, 0, -5, -15, 0]], [[1000000, 1000000, 1000000, 1000000]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9]], [[1, -5, 2.5, 3, -4.7, 5, 6, -4.584526506846036, 7, -8.72172602966587]], [[0, -4, -15]], [[0, -4, 0, -5, -15, -15]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686, 83.25955683011043]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -2.7576561022677204, -8.201037222609227, 24.753109546228686, -8.9, 24.753109546228686]], [[-6, 2.5, 3, -2.7576561022677204, 5, 6, 7, -8.72172602966587]], [[0, -4, 0, -10, -5, -15, -15]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9, -4.7]], [[7, -5, -10, -15, -10]], [[-1, -5, 1, 3, -4]], [[1, -4, 0, -10, -5, -15]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 24.753109546228686, -8.9, 24.753109546228686]], [[1, 2.5, -4.7, 7, 5, 7, 6, 2.6465487078850902, -8.9, -4.7]], [[1, 2.2169763918581937, -4.7, 7, 5, 7, 6, 2.836490197182278, -8.9, 6]], [[-5]], [[1, 2.5, 2.6465487078850902, 7, 5, 6, 2.6465487078850902, -8.9, -4.7]], [[-6, 0, 0, -5, -15, 0, -5]], [[0, 0, -4, -4, 0]], [[-5, -10]], [[-1, -5, -15, -15]], [[1, -4, 0, -10, -4, -15]], [[-5, -5]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9, 5]], [[-1, 0, -2, 3, -5]], [[1, -4, -9, 0, -10, -15]], [[1000000, 1000000, 1000000, 1000000, 1000000]], [[0, 0, -5, -15, -1]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 24.753109546228686, -8.9, -4.584526506846036, 24.753109546228686]], [[1, -5, 2.5, -2, -4.7, 5, 6, -4.584526506846036, 7, -8.72172602966587, 2.5]], [[0, -5, -15, -1]], [[-15, 1.8501344536549909, 3, -2.7576561022677204, 5, 6, 7, -8.72172602966587, 3]], [[-6, 0, -4]], [[0, -15, -1, -1, -1]], [[-6, 1000000, 0, 0, -5, -15, 0, -5]], [[-8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 24.753109546228686, -8.9, -4.584526506846036, 24.753109546228686]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 14.182649846232774, -8.9]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9, 5, -8.9]], [[-1, -5, -15, -2, -15, -5]], [[1, -5, 2.5, 3, -4.7, -2, -4, 6, -4.584526506846036, 7, -8.72172602966587]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686, 83.25955683011043, -8.9]], [[3, -5, -10]], [[7, 0, 0, -5, -15]], [[0, 0, -5, -1, -15, 0]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, 24.753109546228686, 83.25955683011043]], [[1, 2.5, -4.7, 5, 8, 7, 2.6465487078850902, -8.9, 5, -8.9]], [[7, 6, -5, -10, -15, -10]], [[1, -5, 2.5, -2, -4.7, 6, 6, -4.584526506846036, 7, 2.5, -4.584526506846036, -4.7]], [[1, 2.5, -4.7, 4, 7, 7, -8.9]], [[1, -5, 2.5, -2, 1.8501344536549909, -4, 6, 6, -4.584526506846036, 7, 2.5, -4.584526506846036, -4.7]], [[24.82021742307545, 47.032765210131785, -8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 24.753109546228686, -8.9, -4.584526506846036, 24.753109546228686, -4.584526506846036]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9, 4]], [[0, 0, -5, -15, 0, 0]], [[0, -1, -5, -15]], [[1, 2.5, -4.7, 5, 5, 7, 7, 2.6465487078850902, -8.9, 4]], [[-1, -5, 1, -15, 3, -4]], [[-6, 1000000, 0, 0, -15, 0, -5]], [[0, 0, -5, -15, 0, 0, 0, 0]], [[-8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, 24.753109546228686, -8.9, -4.409923735811289, 24.753109546228686, 83.70113458577298]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 58.017978656752504, 24.753109546228686, 83.25955683011043, -8.9]], [[0, -15, -5, -15, 0, 0, 0, 0]], [[-8.9, 47.032765210131785, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686, 83.25955683011043, 24.753109546228686]], [[1, 2.5, -4.7, 5, 7, 7, 2.6465487078850902, -8.9, -4.7, 2.6465487078850902]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686, -8.9, -8.9]], [[1, -5, 2.5, -2, -4.7, 5, 6, -4.584526506846036, 7, -8.72172602966587, 2.5, 2.5]], [[1000000, 1000000, 1000000]], [[-6, 1000000, 0, 0, 0, -5, 1000000]], [[-1, -5, 1, -15, 3, -4, -5]], [[0, -16, 0, -5, -15, -16]], [[-8.9, 60.14886561626176, 2.5, 83.25955683011043, -3.4333260030736827, 24.753109546228686, -8.9, 58.017978656752504, 24.753109546228686, 83.25955683011043, -8.9]], [[1, 2.5, -4.7, 7, 7, 2.6465487078850902, -8.9]], [[-4, 0, -10, -4, -15]], [[24.82021742307545, 24.753109546228686, 83.70113458577298, 2.5, -1.6259727483177557, -8.72172602966587, -8.201037222609227, 14.182649846232774, -8.9]], [[7, -5, 1000000, -10, -15, -10]], [[-40, -15]], [[0, 0, -5, -15, 0, -5, 0, 0]], [[0, 0, -5, -15, 0, -4, 0]], [[-6, 0, 0, -15, 0, -5]], [[-1, -5, 1, -15, 4, 1, -4]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -1.8071120625507624, -8.201037222609227, -8.9, 24.753109546228686]], [[24.82021742307545, -8.9, 83.70113458577298, 2.5, -8.201037222609227, -8.9, 24.753109546228686]], [[1, 0, -5, -15, -1]], [[0, -15, -1, -1]], [[-8.72115684988007, 60.14886561626176, 2.5, 83.45789457940089, -2.7576561022677204, 24.753109546228686, -8.9, 24.753109546228686]], [[-1, -5, -15, 3, -4, -5]], [[7, 0, -5, -15, 0]], [[1, -4, -8, 0, -10, 1]]]
results = [[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000], [1000, 8000, 27000], [1728, 3375], [], [-1, 0, 1, -8, 27, -64], [1, 15.625, 27, -103.82300000000001, 125, 216, 343, -704.969], [-125, -1000, -3375], [1000000000000000000], [1, 15.625, 27, -103.82300000000001, 125, 216, 343, -663.4486595428851], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068], [0, -125, -1000, -3375], [0, -125, -3375], [0, 0, -125, -3375], [1, 15.625, -103.82300000000001, 125, 343, 343, -704.969], [1000000000000000000, 1000000000000000000], [0, 0, -125, -3375, 0], [1, 15.625, -103.82300000000001, 125, 343, 343, -704.969, -704.969], [0, 0, -125, -3375, -3375], [0, 0, -64, -3375], [-216, 0, 0, -125, -3375, 0], [1000000000000000000, 1000000000000000000, 1000000000000000000, 1000000000000000000], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969], [1, -125, 15.625, 27, -103.82300000000001, 125, 216, -96.35704306985083, 343, -663.4486595428851], [0, -64, -3375], [0, -64, 0, -125, -3375, -3375], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068, 577168.0535614366], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -20.9710568501592, -551.5772550112853, 15166.636967209068, -704.969, 15166.636967209068], [-216, 15.625, 27, -20.9710568501592, 125, 216, 343, -663.4486595428851], [0, -64, 0, -1000, -125, -3375, -3375], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969, -103.82300000000001], [343, -125, -1000, -3375, -1000], [-1, -125, 1, 27, -64], [1, -64, 0, -1000, -125, -3375], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 15166.636967209068, -704.969, 15166.636967209068], [1, 15.625, -103.82300000000001, 343, 125, 343, 216, 18.537009558026593, -704.969, -103.82300000000001], [1, 10.896404208352577, -103.82300000000001, 343, 125, 343, 216, 22.82148291540266, -704.969, 216], [-125], [1, 15.625, 18.537009558026593, 343, 125, 216, 18.537009558026593, -704.969, -103.82300000000001], [-216, 0, 0, -125, -3375, 0, -125], [0, 0, -64, -64, 0], [-125, -1000], [-1, -125, -3375, -3375], [1, -64, 0, -1000, -64, -3375], [-125, -125], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969, 125], [-1, 0, -8, 27, -125], [1, -64, -729, 0, -1000, -3375], [1000000000000000000, 1000000000000000000, 1000000000000000000, 1000000000000000000, 1000000000000000000], [0, 0, -125, -3375, -1], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 15166.636967209068, -704.969, -96.35704306985083, 15166.636967209068], [1, -125, 15.625, -8, -103.82300000000001, 125, 216, -96.35704306985083, 343, -663.4486595428851, 15.625], [0, -125, -3375, -1], [-3375, 6.333005603236757, 27, -20.9710568501592, 125, 216, 343, -663.4486595428851, 27], [-216, 0, -64], [0, -3375, -1, -1, -1], [-216, 1000000000000000000, 0, 0, -125, -3375, 0, -125], [-704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 15166.636967209068, -704.969, -96.35704306985083, 15166.636967209068], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 2852.8053635460533, -704.969], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969, 125, -704.969], [-1, -125, -3375, -8, -3375, -125], [1, -125, 15.625, 27, -103.82300000000001, -8, -64, 216, -96.35704306985083, 343, -663.4486595428851], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068, 577168.0535614366, -704.969], [27, -125, -1000], [343, 0, 0, -125, -3375], [0, 0, -125, -1, -3375, 0], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, 15166.636967209068, 577168.0535614366], [1, 15.625, -103.82300000000001, 125, 512, 343, 18.537009558026593, -704.969, 125, -704.969], [343, 216, -125, -1000, -3375, -1000], [1, -125, 15.625, -8, -103.82300000000001, 216, 216, -96.35704306985083, 343, 15.625, -96.35704306985083, -103.82300000000001], [1, 15.625, -103.82300000000001, 64, 343, 343, -704.969], [1, -125, 15.625, -8, 6.333005603236757, -64, 216, 216, -96.35704306985083, 343, 15.625, -96.35704306985083, -103.82300000000001], [15290.3259904969, 104040.28645453702, -704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 15166.636967209068, -704.969, -96.35704306985083, 15166.636967209068, -96.35704306985083], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969, 64], [0, 0, -125, -3375, 0, 0], [0, -1, -125, -3375], [1, 15.625, -103.82300000000001, 125, 125, 343, 343, 18.537009558026593, -704.969, 64], [-1, -125, 1, -3375, 27, -64], [-216, 1000000000000000000, 0, 0, -3375, 0, -125], [0, 0, -125, -3375, 0, 0, 0, 0], [-704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, 15166.636967209068, -704.969, -85.76167149624284, 15166.636967209068, 586400.0989918504], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 195293.4968521427, 15166.636967209068, 577168.0535614366, -704.969], [0, -3375, -125, -3375, 0, 0, 0, 0], [-704.969, 104040.28645453702, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068, 577168.0535614366, 15166.636967209068], [1, 15.625, -103.82300000000001, 125, 343, 343, 18.537009558026593, -704.969, -103.82300000000001, 18.537009558026593], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068, -704.969, -704.969], [1, -125, 15.625, -8, -103.82300000000001, 125, 216, -96.35704306985083, 343, -663.4486595428851, 15.625, 15.625], [1000000000000000000, 1000000000000000000, 1000000000000000000], [-216, 1000000000000000000, 0, 0, 0, -125, 1000000000000000000], [-1, -125, 1, -3375, 27, -64, -125], [0, -4096, 0, -125, -3375, -4096], [-704.969, 217611.7409295406, 15.625, 577168.0535614366, -40.47111114850837, 15166.636967209068, -704.969, 195293.4968521427, 15166.636967209068, 577168.0535614366, -704.969], [1, 15.625, -103.82300000000001, 343, 343, 18.537009558026593, -704.969], [-64, 0, -1000, -64, -3375], [15290.3259904969, 15166.636967209068, 586400.0989918504, 15.625, -4.298726229416711, -663.4486595428851, -551.5772550112853, 2852.8053635460533, -704.969], [343, -125, 1000000000000000000, -1000, -3375, -1000], [-64000, -3375], [0, 0, -125, -3375, 0, -125, 0, 0], [0, 0, -125, -3375, 0, -64, 0], [-216, 0, 0, -3375, 0, -125], [-1, -125, 1, -3375, 64, 1, -64], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -5.901402747473851, -551.5772550112853, -704.969, 15166.636967209068], [15290.3259904969, -704.969, 586400.0989918504, 15.625, -551.5772550112853, -704.969, 15166.636967209068], [1, 0, -125, -3375, -1], [0, -3375, -1, -1], [-663.3187780532812, 217611.7409295406, 15.625, 581302.6104720804, -20.9710568501592, 15166.636967209068, -704.969, 15166.636967209068], [-1, -125, -3375, 27, -64, -125], [343, 0, -125, -3375, 0], [1, -64, -512, 0, -1000, 1]]

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
        func_name = "cube_nums"
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
        for test_case in ['assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]', 'assert cube_nums([10,20,30])==([1000, 8000, 27000])', 'assert cube_nums([12,15])==([1728, 3375])']:
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