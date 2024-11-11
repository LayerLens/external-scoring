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
inputs = [[5], [2], [4], [13], [100], [1000], [True], [1001], [99], [98], [101], [97], [999], [96], [84], [998], [85], [1002], [83], [76], [77], [102], [1003], [78], [1004], [103], [95], [1005], [79], [82], [997], [48], [49], [996], [75], [35], [86], [81], [87], [36], [37], [80], [50], [88], [89], [34], [1006], [995], [104], [52], [53], [65], [94], [47], [33], [66], [74], [93], [105], [51], [91], [90], [46], [32], [92], [106], [18], [54], [994], [15], [1007], [21], [17], [107], [108], [19], [20], [44], [73], [22], [64], [38], [14], [45], [1008], [993], [23], [11], [24], [67], [12], [25], [68], [16], [72], [7], [39], [10], [43], [31], [40], [55], [56], [30], [69]]
results = [11, 1, 5, 2731, 422550200076076467165567735125, 3571695357287557736494750163533339368538016039018445358145834627901170170416453741643994596052319527091982243058510489417290484285641046811994859191566191601311522591608076995140358201687457047292651394051015491661193980422466255853055181315359020971523732159228847389220143277217541462279068556023125, 1, 7143390714575115472989500327066678737076032078036890716291669255802340340832907483287989192104639054183964486117020978834580968571282093623989718383132383202623045183216153990280716403374914094585302788102030983322387960844932511706110362630718041943047464318457694778440286554435082924558137112046251, 211275100038038233582783867563, 105637550019019116791391933781, 845100400152152934331135470251, 52818775009509558395695966891, 1785847678643778868247375081766669684269008019509222679072917313950585085208226870821997298026159763545991121529255244708645242142820523405997429595783095800655761295804038497570179100843728523646325697025507745830596990211233127926527590657679510485761866079614423694610071638608770731139534278011563, 26409387504754779197847983445, 6447604371278022265099605, 892923839321889434123687540883334842134504009754611339536458656975292542604113435410998649013079881772995560764627622354322621071410261702998714797891547900327880647902019248785089550421864261823162848512753872915298495105616563963263795328839755242880933039807211847305035819304385365569767139005781, 12895208742556044530199211, 14286781429150230945979000654133357474152064156073781432583338511604680681665814966575978384209278108367928972234041957669161937142564187247979436766264766405246090366432307980561432806749828189170605576204061966644775921689865023412220725261436083886094928636915389556880573108870165849116274224092501, 3223802185639011132549803, 25185954575304774473045, 50371909150609548946091, 1690200800304305868662270940501, 28573562858300461891958001308266714948304128312147562865166677023209361363331629933151956768418556216735857944468083915338323874285128374495958873532529532810492180732864615961122865613499656378341211152408123933289551843379730046824441450522872167772189857273830779113761146217740331698232548448185003, 100743818301219097892181, 57147125716600923783916002616533429896608256624295125730333354046418722726663259866303913536837112433471715888936167830676647748570256748991917747065059065620984361465729231922245731226999312756682422304816247866579103686759460093648882901045744335544379714547661558227522292435480663396465096896370005, 3380401600608611737324541881003, 13204693752377389598923991723, 114294251433201847567832005233066859793216513248590251460666708092837445453326519732607827073674224866943431777872335661353295497140513497983835494130118131241968722931458463844491462453998625513364844609632495733158207373518920187297765802091488671088759429095323116455044584870961326792930193792740011, 201487636602438195784363, 1611901092819505566274901, 446461919660944717061843770441667421067252004877305669768229328487646271302056717705499324506539940886497780382313811177161310535705130851499357398945773950163940323951009624392544775210932130911581424256376936457649247552808281981631897664419877621440466519903605923652517909652192682784883569502891, 93824992236885, 187649984473771, 223230959830472358530921885220833710533626002438652834884114664243823135651028358852749662253269970443248890191156905588580655267852565425749678699472886975081970161975504812196272387605466065455790712128188468228824623776404140990815948832209938810720233259951802961826258954826096341392441784751445, 12592977287652387236523, 11453246123, 25790417485112089060398421, 805950546409752783137451, 51580834970224178120796843, 22906492245, 45812984491, 402975273204876391568725, 375299968947541, 103161669940448356241593685, 206323339880896712483187371, 5726623061, 228588502866403695135664010466133719586433026497180502921333416185674890906653039465215654147348449733886863555744671322706590994281026995967670988260236262483937445862916927688982924907997251026729689219264991466316414747037840374595531604182977342177518858190646232910089169741922653585860387585480021, 111615479915236179265460942610416855266813001219326417442057332121911567825514179426374831126634985221624445095578452794290327633926282712874839349736443487540985080987752406098136193802733032727895356064094234114412311888202070495407974416104969405360116629975901480913129477413048170696220892375723, 6760803201217223474649083762005, 1501199875790165, 3002399751580331, 12297829382473034411, 6602346876188694799461995861, 46912496118443, 2863311531, 24595658764946068821, 6296488643826193618261, 3301173438094347399730997931, 13521606402434446949298167524011, 750599937895083, 825293359523586849932749483, 412646679761793424966374741, 23456248059221, 1431655765, 1650586719047173699865498965, 27043212804868893898596335048021, 87381, 6004799503160661, 55807739957618089632730471305208427633406500609663208721028666060955783912757089713187415563317492610812222547789226397145163816963141356437419674868221743770492540493876203049068096901366516363947678032047117057206155944101035247703987208052484702680058314987950740456564738706524085348110446187861, 10923, 457177005732807390271328020932267439172866052994361005842666832371349781813306078930431308294696899467773727111489342645413181988562053991935341976520472524967874891725833855377965849815994502053459378438529982932632829494075680749191063208365954684355037716381292465820178339483845307171720775170960043, 699051, 43691, 54086425609737787797192670096043, 108172851219475575594385340192085, 174763, 349525, 5864062014805, 3148244321913096809131, 1398101, 6148914691236517205, 91625968981, 5461, 11728124029611, 914354011465614780542656041864534878345732105988722011685333664742699563626612157860862616589393798935547454222978685290826363977124107983870683953040945049935749783451667710755931699631989004106918756877059965865265658988151361498382126416731909368710075432762584931640356678967690614343441550341920085, 27903869978809044816365235652604213816703250304831604360514333030477891956378544856593707781658746305406111273894613198572581908481570678218709837434110871885246270246938101524534048450683258181973839016023558528603077972050517623851993604026242351340029157493975370228282369353262042674055223093931, 2796203, 683, 5592405, 49191317529892137643, 1365, 11184811, 98382635059784275285, 21845, 1574122160956548404565, 43, 183251937963, 341, 2932031007403, 715827883, 366503875925, 12009599006321323, 24019198012642645, 357913941, 196765270119568550571]

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
        func_name = "jacobsthal_num"
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
        for test_case in ['assert jacobsthal_num(5) == 11', 'assert jacobsthal_num(2) == 1', 'assert jacobsthal_num(4) == 5', 'assert jacobsthal_num(13) == 2731']:
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