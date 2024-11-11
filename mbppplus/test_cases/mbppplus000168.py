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
inputs = [[['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [85, 98, 89, 92]], [['abc', 'def', 'ghi', 'jkl'], ['python', 'program', 'language', 'programs'], [100, 200, 300, 400]], [['A1', 'A2', 'A3', 'A4'], ['java', 'C', 'C++', 'DBMS'], [10, 20, 30, 40]], [['abc', 'def', 'ghi', 'jkl'], ['python', 'program', 'language', 'programs'], [{'1': 'a', '2': 'b'}, {'3': 'c'}, 4, ['x', 'y', 'z']]], [['A1', 'A2', 'A3', 'A4'], [10, 20, 30, 40], [['a', 'b'], ['c', 'd', 'e'], [1, 2, 3, 4], {'x': 1, 'y': 2}]], [['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [[], [], []], [[], [], ['qePIokPMx', -88.68963858646266, False, 92.17031809189785, 20]], [[], [False, True, False, True, True, False, False], []], [['python', 'program', 'lMarshanguage', 'programs'], ['python', 'program', 'lMarshanguage', 'programs'], ['python', 'program', 'lMarshanguage', 'programs']], [[], [92.17031809189785], []], [[10, 20, 30, 40, 20], [10, 20, 30, 40, 20], [['a', 'b'], [1, 2, 3, 4], {'x': 1, 'y': 2}]], [[False, True, False, True, True, False, False], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266], [False, True, False, True, True, False, False]], [[False, True, False, True, True, True], [False, True, False, True, True, True], [False, True, False, True, True, True]], [[92.17031809189785], ['Adina', 'Boyle'], []], [[81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266], [True, False, True, False, False], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266]], [[True, True, False, False, True], [], []], [['python', 'lMarshanguage', 'programs'], ['python', 'lMarshanguage', 'programs'], ['python', 'lMarshanguage', 'programs']], [[20, 4, -85, -8, 20, 5, 73, 13, 2], [], [20, 4, -85, -8, 20, 5, 73, 13, 2]], [['S001', 'S002', 'S003', 'S00', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [[], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20]], [['qePIokPMx', -88.68963858646266, 92.17031809189785, 20], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20], []], [[False, True, False, True, False], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20]], [[], [92.17031809189785, 92.17031809189785], [True, True, False, False, False]], [[], [], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20]], [[10, 20, 30, 40, 20], [10, 20, 30, 40, 20], [['a', 'b'], [1, 3, 3, 4], [1, 3, 3, 4], {'x': 1, 'y': 2}]], [['qePIokPMx', 92.17031809189785, 20], ['qePIokPMx', 92.17031809189785, 20], ['qePIokPMx', 92.17031809189785, 20]], [['S001', 'S002', 'S003', 'S00', 'S004', 'S003'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [[92.17031809189785], [], [92.17031809189785]], [['d', 'A3', 'RaU', 'Park', 'A3', 'ffyPs', 'Duncan', 'Leyton'], [False, True, False, True, True, False, False], []], [['A1', 'A2', 'A3', 'A4'], [10, 20, 30, 40], [['a', 'b'], ['c', 'd', 'e'], {'x': 1, 'y': 2}]], [[81.68418398262912, -91.09614035628569, 57.03263542097301, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266], [81.68418398262912, -91.09614035628569, 57.03263542097301, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266], [81.68418398262912, -91.09614035628569, 57.03263542097301, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266]], [[False, True, False, True, True, False, True], [81.68418398262912, -29.92530843974366, 91.9700693495451, 3.8439202491777706, -2.811244688688049, -91.09614035628569, 92.17031809189785, 37.75918765306639, 37.75918765306639, -44.15533537486549], []], [['S001', 'S002', 'S003', 'S00', 'S004'], ['x', 'Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [['python', 'programs'], ['python', 'programs'], ['python', 'programs']], [['abc', 'def', 'ghi', 'jkl'], ['python', 'program', 'lganguage', 'language', 'programs'], [{'1': 'a', '2': 'b'}, {'3': 'c'}, 4, ['x', 'y', 'z']]], [['qePIokPMx', 92.17031809189785, 20, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785]], [[False, True, False, True, True, True, False], [False, True, False, True, True, True, False], [False, True, False, True, True, True, False]], [['qePIokPMx', 20, 92.17031809189785], ['qePIokPMx', 20, 92.17031809189785], ['qePIokPMx', 20, 92.17031809189785]], [[False, True, False, True, True, True, True], [False, True, False, True, True, True, True], [False, True, False, True, True, True, True]], [['Duncan Boyle', -88.68963858646266, 92.17031809189785, 20], ['Duncan Boyle', -88.68963858646266, 92.17031809189785, 20], ['Duncan Boyle', -88.68963858646266, 92.17031809189785, 20]], [['S001', 'S002', 'S003', 'S00', 'S004'], ['x', 'Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['x', 'Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']], [['def', 'Duncan Boyle', 'ghi', 'jkl'], ['def', 'Duncan Boyle', 'ghi', 'jkl'], ['python', 'Saim Richards', 'lganguage', 'language', 'programs']], [['Duncan Boyle', -88.68963858646266, -91.09614035628569, 19], ['Duncan Boyle', -88.68963858646266, -91.09614035628569, 19], ['Duncan Boyle', -88.68963858646266, -91.09614035628569, 19]], [[False, True, False, True, True, False, True], [81.68418398262912, 3.8439202491777706, -29.92530843974366, 91.9700693495451, 3.8439202491777706, -2.811244688688049, -91.09614035628569, 92.17031809189785, 37.75918765306639, 37.75918765306639, -44.15533537486549], []], [[92.39137694572081, 92.17031809189785], [], [92.39137694572081, 92.17031809189785]], [['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 'qePIokPMx', 'qePIokPMx'], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 'qePIokPMx', 'qePIokPMx'], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 'qePIokPMx', 'qePIokPMx']], [['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}, [1, 2, 3]]], [['x', 'Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Leyton Marsh', 'x'], ['x', 'Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Leyton Marsh', 'x'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [['S001', 'S00Leyton2', 'S003', 'S00', 'S004'], ['S001', 'S00Leyton2', 'S003', 'S00', 'S004'], ['x', 'def', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']], [['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}, {'a': 'x', 'b': 'y', 'c': 'z'}]], [['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785]], [['qePIokPMx', 92.17031809189785, 20], ['qePIokPMx', 92.17031809189785, 20], []], [['Leyton Marsh', 'def', 'Duncan Boyle', 'Saim Richards'], ['Leyton Marsh', 'def', 'Duncan Boyle', 'Saim Richards'], ['S001', 'S00Leyton2', 'S003', 'S00', 'S004']], [[81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, 57.03263542097301, -2.5121677165315077, -88.68963858646266], [True, False, True, False, False], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, 37.75918765306639, 57.03263542097301, 57.03263542097301, -2.5121677165315077, -88.68963858646266]], [[92.17031809189785], ['Adina', 'Boyle'], [-17, 3, 10]], [[], [92.17031809189785, 92.17031809189785], [True, True, False, False, False, False]], [[True, False, True, False, True, True, False, True], [-105.42260580914375, 81.68418398262912, 3.8439202491777706, -29.92530843974366, 91.9700693495451, 3.8439202491777706, -2.811244688688049, -91.09614035628569, 92.17031809189785, 37.75918765306639, 37.75918765306639, -44.15533537486549], []], [['Adina Park', 'Leyton Marsh', 'Duncan Boyle'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [['qePIokPMx', 92.17031809189785, 1, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 1, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 1, 92.17031809189785, 92.17031809189785]], [['qePIokPMx', 56.8935355233056, 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 56.8935355233056, 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 92.17031809189785], ['qePIokPMx', 56.8935355233056, 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 92.17031809189785]], [['Duncan Boyle', 92.17031809189785, 2], ['Duncan Boyle', 92.17031809189785, 2], ['Duncan Boyle', 92.17031809189785, 2]], [[], [False, True, False, True, True, False, True, False], []], [['Adina Park', 'ghi', 'a', 'S004', 'oVDxoixzW', 'IjKiPHTZYR'], [74.62440942155206, -24.89013707770465, 10, 13, -105.42260580914375, 'program'], []], [['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}]], [[-99.76860339291179, 39.84690584810048, 62.189883068165244, 48.27284080844191, -76.69894057820215, -0.5834249281476502, 12.15338911271509, 8.777721336176342, -78.25134314005295, 92.39137694572081, 12.15338911271509], [], []], [['qePIokPMx', 92.17031809189785, 20, 20], ['qePIokPMx', 92.17031809189785, 20, 20], ['qePIokPMx', 92.17031809189785, 20, 20]], [['def', 'Duncan Boyle', 'ghi', 'jkl'], ['def', 'Duncan Boyle', 'ghi', 'jkl'], ['def', 'Duncan Boyle', 'ghi', 'jkl']], [[-91.09614035628569, 92.17031809189785], [-91.09614035628569, 92.17031809189785], []], [[], [92.17031809189785], [92.17031809189785]], [['Duncan Boyle', 2], ['Duncan Boyle', 2], ['Duncan Boyle', 2]], [[-88.68963858646266, 92.17031809189785, 20, 20], [-88.68963858646266, 92.17031809189785, 20, 20], [-88.68963858646266, 92.17031809189785, 20, 20]], [[81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266]], [['python', 'programs', 'python'], ['python', 'programs', 'python'], ['python', 'programs', 'python']], [[], [92.17031809189785, 92.17031809189785], [92.17031809189785, 92.17031809189785]], [[], [-13.280024492899287, -2.811244688688049, 92.39137694572081, 75.06000739007223, -2.811244688688049, 62.189883068165244, -2.811244688688049, -67.07829122649602, 37.75918765306639, -0.5834249281476502], ['qePIokPMx', -88.68963858646266, False, 92.17031809189785, 20]], [['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Duncan Boyle'], ['Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Duncan Boyle']], [[81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266, -88.68963858646266, -29.92530843974366], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266, -88.68963858646266, -29.92530843974366], [81.68418398262912, -91.09614035628569, -99.76860339291179, -88.68963858646266, -88.68963858646266, -29.92530843974366, 37.75918765306639, 57.03263542097301, -2.5121677165315077, -88.68963858646266, -88.68963858646266, -88.68963858646266, -29.92530843974366]], [['qePIokPMx', -88.68963858646266, 'S00Leyton2', 92.17031809189785, 20], [], ['qePIokPMx', -88.68963858646266, 'S00Leyton2', 92.17031809189785, 20]], [['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 'qePIokPMx'], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 'qePIokPMx'], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785, 92.17031809189785, 'qePIokPMx']], [['S001', 'S002', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [[1, 2, 3], [4, 5, 6], {'a': 'x', 'b': 'y', 'c': 'z'}, [1, 2, 3]]], [['S001', 'S002', 'S004'], ['S002', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['S002', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']], [['A1', 'A2', 'A3', 'A4'], [10, 20, 30, 40], [['a', 'b'], ['c', 'd', 'e'], {'y': 2}]], [[10, 20, 30, 40, 20], [10, 20, 30, 40, 20], [10, 20, 30, 40, 20]], [['S002', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['S002', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['S002', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']], [['programs', 'python'], ['programs', 'python'], ['programs', 'python']], [['qePIokPMx', -88.68963858646266, 'c', 'S00Leyton2', 92.17031809189785, 20], [], ['qePIokPMx', -88.68963858646266, 'c', 'S00Leyton2', 92.17031809189785, 20]], [[-99.76860339291179, 39.84690584810048, 62.189883068165244, 48.27284080844191, -76.69894057820215, -0.5834249281476502, 12.15338911271509, 8.777721336176342, -78.25134314005295, 92.39137694572081, 12.15338911271509], [], ['IjKiPHTZYR', '', 'BMI', 'bBRSnEOt']], [['S002', 'A4', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['S002', 'A4', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], ['S002', 'A4', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']], [['qePIokPMx', 20, 119.11950781083245, 92.17031809189785, 20], ['qePIokPMx', 20, 119.11950781083245, 92.17031809189785, 20], ['qePIokPMx', 20, 119.11950781083245, 92.17031809189785, 20]], [['BMI', 'Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Duncan Boyle', 'qePIokPMx'], ['BMI', 'Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Duncan Boyle', 'qePIokPMx'], ['BMI', 'Adina Park', 'qePIokPMx', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'Duncan Boyle', 'qePIokPMx']], [['qePIokPMx', 20], ['qePIokPMx', 20], ['qePIokPMx', 20]], [[11, 20, 30, 13, 20, 13], [11, 20, 30, 13, 20, 13], [11, 20, 30, 13, 20, 13]], [['def', 'Duncan Boyle', 'ghi', 'jkl'], ['def', 'Duncan Boyle', 'ghi', 'jkl'], ['python', 'Saim Richards', 'lganguage', 'programs']], [[False, False, True, True, True, False, False], [False, False, True, True, True, False, False], [False, False, True, True, True, False, False]], [['qePIokPMx', 92.17031809189785, 20, 92.17031809189785], ['qePIokPMx', 92.17031809189785, 20, 92.17031809189785], []], [['qePIokPMx', -88.68963858646266, 92.17031809189785, 20, 20], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20, 20], ['qePIokPMx', -88.68963858646266, 92.17031809189785, 20, 20]], [[], [-13.280024492899287, 92.39137694572081, 75.06000739007223, -2.811244688688049, 62.189883068165244, -2.811244688688049, 37.75918765306639, -0.5834249281476502], [-13.280024492899287, 92.39137694572081, 75.06000739007223, -2.811244688688049, 62.189883068165244, -2.811244688688049, 37.75918765306639, -0.5834249281476502]], [[-76.69894057820215, 12.15338911271509, 81.68418398262912, -44.15533537486549, -29.92530843974366, -29.92530843974366, -99.76860339291179, -105.42260580914375, -99.2192956011222, 8.777721336176342], [], ['qePIokPMx', -88.68963858646266, False, 92.17031809189785, 20, False]], [[92.17031809189785], ['Adina'], [-17, 3, 10]], [[20, 4, -85, -8, 20, 5, 73, 13, 2, 5], [True, True, False, False, True, True, True, True, False, False], [20, 4, -85, -8, 20, 5, 73, 13, 2, 5]], [[92.17031809189785], ['Adina', 'Boyle'], [-62, 73]], [['Adina'], [4, -17, 40, 3, 10], [92.17031809189785]], [[False, True, False, True, True, False, True], [81.68418398262912, -29.92530843974366, 91.9700693495451, 3.8439202491777706, -2.811244688688049, -91.09614035628569, 92.17031809189785, 37.75918765306639, 37.75918765306639, -44.15533537486549], [81.68418398262912, -29.92530843974366, 91.9700693495451, 3.8439202491777706, -2.811244688688049, -91.09614035628569, 92.17031809189785, 37.75918765306639, 37.75918765306639, -44.15533537486549]], [[-76.69894057820215, 12.15338911271509, 81.68418398262912, -44.15533537486549, -29.92530843974366, -29.92530843974366, -99.76860339291179, -105.42260580914375, -99.2192956011222, 10.903113434010868], [-88, 'qiMdF'], [-76.69894057820215, 12.15338911271509, 81.68418398262912, -44.15533537486549, -29.92530843974366, -29.92530843974366, -99.76860339291179, -105.42260580914375, -99.2192956011222, 10.903113434010868]], [['x', 'def', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'x'], ['S001', 'S00Leyton2', 'S003', 'S002', 'S004'], ['x', 'def', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards', 'x']], [[10, 30, 13, 20, 13], [10, 30, 13, 20, 13], [10, 30, 13, 20, 13]]]
results = [[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}], [{'abc': {'python': 100}}, {'def': {'program': 200}}, {'ghi': {'language': 300}}, {'jkl': {'programs': 400}}], [{'A1': {'java': 10}}, {'A2': {'C': 20}}, {'A3': {'C++': 30}}, {'A4': {'DBMS': 40}}], [{'abc': {'python': {'1': 'a', '2': 'b'}}}, {'def': {'program': {'3': 'c'}}}, {'ghi': {'language': 4}}, {'jkl': {'programs': ['x', 'y', 'z']}}], [{'A1': {10: ['a', 'b']}}, {'A2': {20: ['c', 'd', 'e']}}, {'A3': {30: [1, 2, 3, 4]}}, {'A4': {40: {'x': 1, 'y': 2}}}], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'Leyton Marsh': [4, 5, 6]}}, {'S003': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [], [], [], [{'python': {'python': 'python'}}, {'program': {'program': 'program'}}, {'lMarshanguage': {'lMarshanguage': 'lMarshanguage'}}, {'programs': {'programs': 'programs'}}], [], [{10: {10: ['a', 'b']}}, {20: {20: [1, 2, 3, 4]}}, {30: {30: {'x': 1, 'y': 2}}}], [{False: {81.68418398262912: False}}, {True: {-91.09614035628569: True}}, {False: {-99.76860339291179: False}}, {True: {-88.68963858646266: True}}, {True: {-88.68963858646266: True}}, {False: {37.75918765306639: False}}, {False: {57.03263542097301: False}}], [{False: {False: False}}, {True: {True: True}}, {False: {False: False}}, {True: {True: True}}, {True: {True: True}}, {True: {True: True}}], [], [{81.68418398262912: {True: 81.68418398262912}}, {-91.09614035628569: {False: -91.09614035628569}}, {-99.76860339291179: {True: -99.76860339291179}}, {-88.68963858646266: {False: -88.68963858646266}}, {-88.68963858646266: {False: -88.68963858646266}}], [], [{'python': {'python': 'python'}}, {'lMarshanguage': {'lMarshanguage': 'lMarshanguage'}}, {'programs': {'programs': 'programs'}}], [], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'Leyton Marsh': [4, 5, 6]}}, {'S003': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [], [], [{False: {'qePIokPMx': 'qePIokPMx'}}, {True: {-88.68963858646266: -88.68963858646266}}, {False: {92.17031809189785: 92.17031809189785}}, {True: {20: 20}}], [], [], [{10: {10: ['a', 'b']}}, {20: {20: [1, 3, 3, 4]}}, {30: {30: [1, 3, 3, 4]}}, {40: {40: {'x': 1, 'y': 2}}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'Leyton Marsh': [4, 5, 6]}}, {'S003': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [], [], [{'A1': {10: ['a', 'b']}}, {'A2': {20: ['c', 'd', 'e']}}, {'A3': {30: {'x': 1, 'y': 2}}}], [{81.68418398262912: {81.68418398262912: 81.68418398262912}}, {-91.09614035628569: {-91.09614035628569: -91.09614035628569}}, {57.03263542097301: {57.03263542097301: 57.03263542097301}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {37.75918765306639: {37.75918765306639: 37.75918765306639}}, {57.03263542097301: {57.03263542097301: 57.03263542097301}}, {-2.5121677165315077: {-2.5121677165315077: -2.5121677165315077}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}], [], [{'S001': {'x': [1, 2, 3]}}, {'S002': {'Adina Park': [4, 5, 6]}}, {'S003': {'Leyton Marsh': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [{'python': {'python': 'python'}}, {'programs': {'programs': 'programs'}}], [{'abc': {'python': {'1': 'a', '2': 'b'}}}, {'def': {'program': {'3': 'c'}}}, {'ghi': {'lganguage': 4}}, {'jkl': {'language': ['x', 'y', 'z']}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}], [{False: {False: False}}, {True: {True: True}}, {False: {False: False}}, {True: {True: True}}, {True: {True: True}}, {True: {True: True}}, {False: {False: False}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}], [{False: {False: False}}, {True: {True: True}}, {False: {False: False}}, {True: {True: True}}, {True: {True: True}}, {True: {True: True}}, {True: {True: True}}], [{'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}], [{'S001': {'x': 'x'}}, {'S002': {'Adina Park': 'Adina Park'}}, {'S003': {'Leyton Marsh': 'Leyton Marsh'}}, {'S00': {'Duncan Boyle': 'Duncan Boyle'}}, {'S004': {'Saim Richards': 'Saim Richards'}}], [{'def': {'def': 'python'}}, {'Duncan Boyle': {'Duncan Boyle': 'Saim Richards'}}, {'ghi': {'ghi': 'lganguage'}}, {'jkl': {'jkl': 'language'}}], [{'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-91.09614035628569: {-91.09614035628569: -91.09614035628569}}, {19: {19: 19}}], [], [], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'Leyton Marsh': [4, 5, 6]}}, {'S003': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}, {'S004': {'Saim Richards': [1, 2, 3]}}], [{'x': {'x': [1, 2, 3]}}, {'Adina Park': {'Adina Park': [4, 5, 6]}}, {'Leyton Marsh': {'Leyton Marsh': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [{'S001': {'S001': 'x'}}, {'S00Leyton2': {'S00Leyton2': 'def'}}, {'S003': {'S003': 'Leyton Marsh'}}, {'S00': {'S00': 'Duncan Boyle'}}, {'S004': {'S004': 'Saim Richards'}}], [{'Adina Park': {'Adina Park': [1, 2, 3]}}, {'Leyton Marsh': {'Leyton Marsh': [4, 5, 6]}}, {'Duncan Boyle': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}, {'Saim Richards': {'Saim Richards': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}], [], [{'Leyton Marsh': {'Leyton Marsh': 'S001'}}, {'def': {'def': 'S00Leyton2'}}, {'Duncan Boyle': {'Duncan Boyle': 'S003'}}, {'Saim Richards': {'Saim Richards': 'S00'}}], [{81.68418398262912: {True: 81.68418398262912}}, {-91.09614035628569: {False: -91.09614035628569}}, {-99.76860339291179: {True: -99.76860339291179}}, {-88.68963858646266: {False: -88.68963858646266}}, {-88.68963858646266: {False: -88.68963858646266}}], [{92.17031809189785: {'Adina': -17}}], [], [], [{'Adina Park': {'Adina Park': [1, 2, 3]}}, {'Leyton Marsh': {'Leyton Marsh': [4, 5, 6]}}, {'Duncan Boyle': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {1: {1: 1}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {56.8935355233056: {56.8935355233056: 56.8935355233056}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}], [{'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {2: {2: 2}}], [], [], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'qePIokPMx': [4, 5, 6]}}, {'S003': {'Leyton Marsh': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {20: {20: 20}}], [{'def': {'def': 'def'}}, {'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {'ghi': {'ghi': 'ghi'}}, {'jkl': {'jkl': 'jkl'}}], [], [], [{'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {2: {2: 2}}], [{-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {20: {20: 20}}], [{81.68418398262912: {81.68418398262912: 81.68418398262912}}, {-91.09614035628569: {-91.09614035628569: -91.09614035628569}}, {-99.76860339291179: {-99.76860339291179: -99.76860339291179}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-29.92530843974366: {-29.92530843974366: -29.92530843974366}}, {37.75918765306639: {37.75918765306639: 37.75918765306639}}, {57.03263542097301: {57.03263542097301: 57.03263542097301}}, {-2.5121677165315077: {-2.5121677165315077: -2.5121677165315077}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}], [{'python': {'python': 'python'}}, {'programs': {'programs': 'programs'}}, {'python': {'python': 'python'}}], [], [], [{'S001': {'Adina Park': 'Adina Park'}}, {'S002': {'qePIokPMx': 'qePIokPMx'}}, {'S003': {'Leyton Marsh': 'Leyton Marsh'}}, {'S004': {'Duncan Boyle': 'Duncan Boyle'}}], [{81.68418398262912: {81.68418398262912: 81.68418398262912}}, {-91.09614035628569: {-91.09614035628569: -91.09614035628569}}, {-99.76860339291179: {-99.76860339291179: -99.76860339291179}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-29.92530843974366: {-29.92530843974366: -29.92530843974366}}, {37.75918765306639: {37.75918765306639: 37.75918765306639}}, {57.03263542097301: {57.03263542097301: 57.03263542097301}}, {-2.5121677165315077: {-2.5121677165315077: -2.5121677165315077}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {-29.92530843974366: {-29.92530843974366: -29.92530843974366}}], [], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}], [{'S001': {'Adina Park': [1, 2, 3]}}, {'S002': {'Leyton Marsh': [4, 5, 6]}}, {'S004': {'Duncan Boyle': {'a': 'x', 'b': 'y', 'c': 'z'}}}], [{'S001': {'S002': 'S002'}}, {'S002': {'Leyton Marsh': 'Leyton Marsh'}}, {'S004': {'Duncan Boyle': 'Duncan Boyle'}}], [{'A1': {10: ['a', 'b']}}, {'A2': {20: ['c', 'd', 'e']}}, {'A3': {30: {'y': 2}}}], [{10: {10: 10}}, {20: {20: 20}}, {30: {30: 30}}, {40: {40: 40}}, {20: {20: 20}}], [{'S002': {'S002': 'S002'}}, {'Leyton Marsh': {'Leyton Marsh': 'Leyton Marsh'}}, {'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {'Saim Richards': {'Saim Richards': 'Saim Richards'}}], [{'programs': {'programs': 'programs'}}, {'python': {'python': 'python'}}], [], [], [{'S002': {'S002': 'S002'}}, {'A4': {'A4': 'A4'}}, {'Leyton Marsh': {'Leyton Marsh': 'Leyton Marsh'}}, {'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {'Saim Richards': {'Saim Richards': 'Saim Richards'}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {20: {20: 20}}, {119.11950781083245: {119.11950781083245: 119.11950781083245}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}], [{'BMI': {'BMI': 'BMI'}}, {'Adina Park': {'Adina Park': 'Adina Park'}}, {'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {'Leyton Marsh': {'Leyton Marsh': 'Leyton Marsh'}}, {'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {'Saim Richards': {'Saim Richards': 'Saim Richards'}}, {'Duncan Boyle': {'Duncan Boyle': 'Duncan Boyle'}}, {'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {20: {20: 20}}], [{11: {11: 11}}, {20: {20: 20}}, {30: {30: 30}}, {13: {13: 13}}, {20: {20: 20}}, {13: {13: 13}}], [{'def': {'def': 'python'}}, {'Duncan Boyle': {'Duncan Boyle': 'Saim Richards'}}, {'ghi': {'ghi': 'lganguage'}}, {'jkl': {'jkl': 'programs'}}], [{False: {False: False}}, {False: {False: False}}, {True: {True: True}}, {True: {True: True}}, {True: {True: True}}, {False: {False: False}}, {False: {False: False}}], [], [{'qePIokPMx': {'qePIokPMx': 'qePIokPMx'}}, {-88.68963858646266: {-88.68963858646266: -88.68963858646266}}, {92.17031809189785: {92.17031809189785: 92.17031809189785}}, {20: {20: 20}}, {20: {20: 20}}], [], [], [{92.17031809189785: {'Adina': -17}}], [{20: {True: 20}}, {4: {True: 4}}, {-85: {False: -85}}, {-8: {False: -8}}, {20: {True: 20}}, {5: {True: 5}}, {73: {True: 73}}, {13: {True: 13}}, {2: {False: 2}}, {5: {False: 5}}], [{92.17031809189785: {'Adina': -62}}], [{'Adina': {4: 92.17031809189785}}], [{False: {81.68418398262912: 81.68418398262912}}, {True: {-29.92530843974366: -29.92530843974366}}, {False: {91.9700693495451: 91.9700693495451}}, {True: {3.8439202491777706: 3.8439202491777706}}, {True: {-2.811244688688049: -2.811244688688049}}, {False: {-91.09614035628569: -91.09614035628569}}, {True: {92.17031809189785: 92.17031809189785}}], [{-76.69894057820215: {-88: -76.69894057820215}}, {12.15338911271509: {'qiMdF': 12.15338911271509}}], [{'x': {'S001': 'x'}}, {'def': {'S00Leyton2': 'def'}}, {'Leyton Marsh': {'S003': 'Leyton Marsh'}}, {'Duncan Boyle': {'S002': 'Duncan Boyle'}}, {'Saim Richards': {'S004': 'Saim Richards'}}], [{10: {10: 10}}, {30: {30: 30}}, {13: {13: 13}}, {20: {20: 20}}, {13: {13: 13}}]]

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
        func_name = "convert_list_dictionary"
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
        for test_case in ['assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{\'S001\': {\'Adina Park\': 85}}, {\'S002\': {\'Leyton Marsh\': 98}}, {\'S003\': {\'Duncan Boyle\': 89}}, {\'S004\': {\'Saim Richards\': 92}}]', 'assert convert_list_dictionary(["abc","def","ghi","jkl"],["python","program","language","programs"],[100,200,300,400])==[{\'abc\':{\'python\':100}},{\'def\':{\'program\':200}},{\'ghi\':{\'language\':300}},{\'jkl\':{\'programs\':400}}]', 'assert convert_list_dictionary(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{\'A1\':{\'java\':10}},{\'A2\':{\'C\':20}},{\'A3\':{\'C++\':30}},{\'A4\':{\'DBMS\':40}}]']:
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