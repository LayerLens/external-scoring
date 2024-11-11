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
inputs = [[2], [10], [56], [0], [100], [99], [True], [False], [98], [1], [3], [97], [96], [11], [12], [92], [95], [94], [14], [13], [55], [17], [15], [93], [16], [9], [91], [54], [25], [18], [4], [5], [6], [8], [90], [53], [7], [19], [64], [20], [21], [63], [52], [24], [57], [22], [62], [89], [51], [50], [88], [58], [49], [45], [65], [23], [87], [46], [59], [26], [44], [61], [48], [47], [60], [30], [27], [86], [28], [31], [29], [66], [67], [85], [70], [71], [43], [69], [82], [83], [72], [68], [81], [73], [32], [33], [42], [74], [84], [41], [80], [79], [75], [40], [76], [34], [35], [78], [77], [39], [38], [36]]
results = [2, 115975, 6775685320645824322581483068371419745979053216268760300, 1, 47585391276764833658790768841387207826363669686825611466616334637559114497892442622672724044217756306953557882560751, 1618706027446068305855680628161135741330684513088812399898409470089128730792407044351108134019449028191480663320741, 1, 1, 55494677927746340698788238667452126040563242441827634980157203368430358083090722409217101274455481270374885095618, 1, 5, 1917593350464112616752757157565032460248311804906650215954187246738986739924580790084847891233423398173059771233, 66790853422797408533421892496106177820862555650400879850993569405575404871887998514898872210341414631481213729, 678570, 4213597, 106611797892739782364113678801520610524431974731789913132104301942153476208366519192812848588253648356364, 2345129936856330144543337656630809098301482271000632150222900693128839447045930834163493232282141300734566042, 83012043550967281787120476720274991081436431402381752242504514629481800064636673934392827445150961387102019, 190899322, 27644437, 359334085968622831041960188598043661065388726959079837, 82864869804, 1382958545, 2962614388531218251190227244935749736828675583113926711461226180042633884248639975904464409686755210349399, 10480142147, 21147, 3868731362280702160655673912482765098905555785458740412264329844745080937342264610781770223818259614025, 19317287589145618265728950069285503257349832850302011, 4638590332229999353, 682076806159, 15, 52, 203, 4140, 141580318123392930464192819123202606981284563291786545804370223525364095085412667328027643050802912567, 1052928518014714166107781298021583534928402714242132, 877, 5832742205057, 172134143357358850934369963665272571125557575184049758045339873395, 51724158235372, 474869816156751, 8250771700405624889912456724304738028450190134337110943817172961, 58205338024195872785464627063218599149503972126463, 445958869294805289, 129482661947506964462616580633806000917491602609372517195, 4506715738447323, 400237304821454786230522819234667544935526963060240082269259738, 5225728505358477773256348249698509144957920836936865715700797250722975706153317517427783066539250012, 3263983870004111524856951830191582524419255819477, 185724268771078270438257767181908917499221852770, 194553897403965647871786295024290690576513032341195649821051001205884166153194143340809062985041067, 2507136358984296114560786627437574942253015623445622326263, 10726137154573358400342215518590002633917247281, 139258505266263669602347053993654079693415, 3633778785457899322415257682767737441410036994560435982365219287372, 44152005855084346, 7306720755827530589639480511232846731775215754200303890190355852772713202556415109429779445622537, 2265418219334494002928484444705392276158355, 49176743336309621659000944152624896853591018248919168867818, 49631246523618756274, 8701963427387055089023600531855797148876, 19652364471547941482114228389322789963345673460673370562378245, 628919796303118415420210454071849537746015761, 37450059502461511196505342096431510120174682, 976939307467007552986994066961675455550246347757474482558637, 846749014511809332450147, 545717047936059989389, 276844443054160876160126038812506987515878490163433019207947986484590126191194780416973565092618, 6160539404599934652455, 10293358946226376485095653, 71339801938860275191172, 77605907238843669482155930857960017792778059887519278038000759795263, 1676501284301523453367212880854005182365748317589888660477021013719409, 10583321873228234424552137744344434100391955309436425797852108559510434249855735357360593574749, 18075003898340511237556784424498369141305841234468097908227993035088029195, 408130093410464274259945600962134706689859323636922532443365594726056131962, 552950118797165484321714693280737767385, 809212768387947836336846277707066239391942323998649273771736744420003007, 624387454429479848302014120414448006907125370284776661891529899343806658375826740689137423, 15892292813296951899433594303207669496517041849871581501737510069308817348770226226653966474, 9314528182092653288251451483527341806516792394674496725578935706029134658745, 36628224206696135478834640618028539032699174847931909480671725803995436, 24761288718465863816962119279306788401954401906692653427329808967315171931611751006838915, 214834623568478894452765605511928333367140719361291003997161390043701285425833, 128064670049908713818925644, 1629595892846007606764728147, 35742549198872617291353508656626642567, 5006908024247925379707076470957722220463116781409659160159536981161298714301202, 408248141291805738980141314733701533991578374164094348787738475995651988600158415299211778933, 2351152507740617628200694077243788988, 991267988808424794443839434655920239360814764000951599022939879419136287216681744888844, 40064166844084356404509204005730815621427040237270563024820379702392240194729249115029, 117896026920858300966730642538212084059025603061199813571998059942386637656568797, 157450588391204931289324344702531067, 2804379077740744643020190973126488180455295657360401565474468309847623573788115607, 21195039388640360462388656799, 281600203019560266563340426570, 1635000770532737216633829256032779450518375544542935181844299348876855151241590189395, 67379449595254843852699636792665969652321946648374400833740986348378276368807261348, 10738823330774692832768857986425209, 746289892095625330523099540639146, 3819714729894818339975525681317]

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
        func_name = "bell_number"
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
        for test_case in ['assert bell_number(2)==2', 'assert bell_number(10)==115975', 'assert bell_number(56)==6775685320645824322581483068371419745979053216268760300']:
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
