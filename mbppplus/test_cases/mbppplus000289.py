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
inputs = [[-1], [0], [2], [-0.5], [0.5], [1], [1000000000], [-1000000000], [0.2072611874375927], [False], [True], [0.16809162682757048], [0.6844411299243851], [0.35683551430663585], [0.33946897052245506], [0.6521612813427807], [999999999], [0.17112184563336552], [19], [-65.63179010691987], [-0.01895300889853002], [-0.2255496597911223], [0.25992055122366875], [-1000000001], [-0.2386542836217336], [0.0886668365313565], [-0.6124370845097739], [1.554047854781877], [-65.03547673997947], [2.3994387471541216], [-35.74281783110325], [0.09528268647223326], [0.3232568533333865], [0.2242711558968573], [-0.9709905734457034], [-0.6546455374650706], [-0.06234286415868906], [1.3977482675936928], [0.29784236090387306], [0.33836539173549723], [-31.610835992989255], [-0.27669689852371004], [84], [-1000000002], [0.6223298065417987], [-999999999], [8], [0.6754515039898535], [1.071880421647353], [0.7544257017505951], [-26.27081423640981], [-999999998], [86], [-13.889508087517811], [2.600031963946284], [3.0652858255362965], [0.8998367814282604], [0.8309457774079265], [0.44818675801257646], [-0.30367725300317], [1.2411900876071214], [18], [0.2729798323779066], [0.3285339976213698], [-36.146603050653454], [-27], [-26], [-0.9874223750138421], [1.5476233443397687], [-86.6551056172488], [1.6060546715294721], [2.1601728022044884], [2.285060680697282], [2.8260615578768196], [0.14266165000955092], [-0.017934287764720593], [-84.95845096222169], [1.0974614491570875], [1.898333123797264], [-0.23800544092412548], [0.8789431902277999], [0.4102883538841385], [-0.2581929508402424], [4.5143460754522735], [1.1277670988949333], [-19.946636688004762], [-999999997], [-0.011164351123219007], [-87.64997072807174], [-0.6132302083082929], [-0.23140740618272113], [0.20870583419763342], [0.21493934798744777], [999999998], [-0.15646745414267438], [-0.37347281880381433], [-0.17536906835796195], [-0.12875962601096258], [0.7562408647560114], [-88.39828615224197], [0.4785284183694467], [0.29728651261782624], [1.0367180826599893], [-0.3475613031240767], [-0.38928230557291527], [1.3746888786897695]]
results = [None, 0, 4, None, 0.25, 1, 1000000000000000000, None, 0.042957199818040935, 0, 1, 0.028254795009539212, 0.468459660332169, 0.12733158427048133, 0.11523918194757546, 0.4253143368826576, 999999998000000001, 0.029282686052969378, 361, None, None, None, 0.06755869294841581, None, None, 0.007861807900478296, None, 2.415064734952154, None, 5.757306301344541, None, 0.009078790341365902, 0.10449499322700255, 0.050297551367312475, None, None, None, 1.9537002195611692, 0.08871007194879298, 0.1144911383243165, None, None, 7056, None, 0.3872943881103526, None, 64, 0.45623473424215516, 1.1489276383109073, 0.5691581394618779, None, None, 7396, None, 6.760166213542371, 9.395977192233735, 0.8097062332111709, 0.6904708849920633, 0.20087137005782377, None, 1.5405528335741736, 324, 0.07451798888506997, 0.10793458759307822, None, None, None, None, 2.39513801594541, None, 2.5794116079416405, 4.666346535383991, 5.221502314468727, 7.9866239289091565, 0.0203523463834476, None, None, 1.2044216323859747, 3.6036686489058787, None, 0.7725411316478223, 0.16833653333295606, None, 20.379320488951343, 1.2718586293498944, None, None, None, None, None, None, 0.04355812522813005, 0.04619892331326916, 999999996000000004, None, None, None, None, 0.5719002455269199, None, 0.2289894471871642, 0.08837927058446896, 1.0747843829142045, None, None, 1.8897695131933359]

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
        func_name = "triangle_area"
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
        for test_case in ['assert triangle_area(-1) == None', 'assert triangle_area(0) == 0', 'assert triangle_area(2) == 4']:
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
