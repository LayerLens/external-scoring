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
inputs = [[[2, 4, 3, 5, 7], [3, 7]], [[2, 4, 3, 5, 7], [4, 3]], [[2, 4, 3, 5, 7], [1, 6]], [[], []], [[], [1]], [['r'], []], [['sfIngs', 'GYVu', 'r'], []], [['r', 'sfIngs', 'GYVu'], [False, 'klXTmRZyQ']], [[False, 99.97028427774339, 82, 'GYVu', False, 'Ok', None, [1, -71.80691717114227]], []], [['r', 'sfIngs', 'GYVu', 'GYVu'], ['r', 'sfIngs', 'GYVu', 'GYVu']], [['r', 'sgfIngs', 'GYVu', 'GYVu'], ['r', 'sgfIngs', 'GYVu', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYVu'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu']], [['r', 'sfIngs', 'GYVu'], ['r', 'sfIngs', 'GYVu']], [['sfIngs', 'GYVu'], ['sfIngs', 'GYVu']], [['sgfIngs', 'sfIngs', 'GYVu', 'r', 'r', 'sfIngs'], ['sgfIngs', 'sfIngs', 'GYVu', 'r', 'r', 'sfIngs']], [['r', 'GYVu', 'r'], []], [['r', 'GYVu', 'r'], ['r', 'GYVu', 'r']], [['sgfIngs', 'sfIngs', 'GYVu', 'sfIngsr', 'GYV', 'r', 'sfIngs'], ['sgfIngs', 'sfIngs', 'GYVu', 'sfIngsr', 'GYV', 'r', 'sfIngs']], [[1], [1]], [[None, False, {'sfIngsr': 42.34905566158099, 'FHvMaMnTCg': -74.03921201241215, 'hKRFjm': -74.21853866002988, 'rKQ': 40.63712034844792}, {'24.822944608944297': 'pfIhkuLtSg', '-22.735241874996206': 's', '-13.009939375362165': 'sfIngsr', '-71.80691717114227': 'VtqKcYvzg', '99.97028427774339': 'DBzU', '68.8678541991217': 'GYVu', '-83.5332401941628': 'PctAoxwD'}, [66, 1, -51, 1, -59, 1, False, -71], True, 'sfIngs', 1], []], [['GYVu', 'pfIhkuLtSg', 'O', 'Odpagl', 'Casb'], []], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'GYV'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'GYV']], [[-42, 8, -83.5332401941628, -82, 38.16772877208774, {'VtqKcYvzg': 47.40072133316414, 'sLmQQSONWn': -13.009939375362165, 'O': 36, 'rKQ': [48, -59]}, -40], []], [[8, None, False, {'sfIngsr': 42.34905566158099, 'FHvMaMnTCg': -74.03921201241215, 'hKRFjm': -74.21853866002988, 'rKQ': 40.63712034844792}, {'24.822944608944297': 'pfIhkuLtSg', '-22.735241874996206': 's', '-13.009939375362165': 'sfIngsr', '-71.80691717114227': 'VtqKcYvzg', '99.97028427774339': 'DBzU', '68.8678541991217': 'GYVu', '-83.5332401941628': 'PctAoxwD'}, [66, 1, -51, 1, -59, 1, False, -71], True, 'sfIngs', 1], []], [['r', 'sfIngs', 's'], [False, 'klXTmRZyQ']], [['r', 'sgfIngs', 'GYVu', 'pfIhkuLtSgr', 'GYVu'], ['r', 'sgfIngs', 'GYVu', 'pfIhkuLtSgr', 'GYVu']], [[[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 90.16807182684596, 'qyujtuO', 82, 75.22089802044161, 82], [[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 90.16807182684596, 'qyujtuO', 82, 75.22089802044161, 82]], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'r']], [['GYVur', 'sgfIngs', 'GYVu', 'GYVu'], ['GYVur', 'sgfIngs', 'GYVu', 'GYVu']], [['sfIngsGYVu', 'sfIngs', 'GYVu'], ['sfIngsGYVu', 'sfIngs', 'GYVu']], [['r', 'GYVu', 'r', 'r'], ['r', 'GYVu', 'r', 'r']], [['sfIngSFVGYVVgWCfDjsGYVu', 'sfIngSFVVgWCfDjsGYVu', 'sfIngs', 'GYVu'], ['sfIngSFVGYVVgWCfDjsGYVu', 'sfIngSFVVgWCfDjsGYVu', 'sfIngs', 'GYVu']], [['r', 'GYVu', 'r'], [True, True, True, False, True, False, False, True]], [['r'], ['r']], [['r', 'GSFVVgWCfDju', 'GYVu', 'r'], ['r', 'GSFVVgWCfDju', 'GYVu', 'r']], [['sgfIngs', 'sfIngs', 'GYVu', 'sfIngsr', 'GYV', 'r', 'GYV'], ['sgfIngs', 'sfIngs', 'GYVu', 'sfIngsr', 'GYV', 'r', 'GYV']], [[], [True, False, True]], [['r', 'GYVu', 'r'], [-49.293443668830214, 11.89338685730192, 38.68012886425632, 64.91527494125927, -74.03921201241215, 0.3374408817541621]], [['r', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu'], ['r', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu']], [[90.16807182684596, 'qyujtuO', 82, 75.22089802044161, 82], [90.16807182684596, 'qyujtuO', 82, 75.22089802044161, 82]], [['r', 'sfIngs', 'GYVu', 'r', 'r'], ['r', 'sfIngs', 'GYVu', 'r', 'r']], [[90.16807182684596, 'qyujtuO', 75.22089802044161, 'sfIngSFVGYVVgWCfDjsGYVu', 82], [90.16807182684596, 'qyujtuO', 75.22089802044161, 'sfIngSFVGYVVgWCfDjsGYVu', 82]], [['r', 'GYVu', 'r'], [-49.293443668830214, 11.89338685730192, 38.68012886425632, 64.91527494125927, -74.03921201241215, 0.3374408817541621, -74.03921201241215]], [['GYVur', 'sgfIngs', 'GYVu', 'GYVu', 'GYVu'], ['GYVur', 'sgfIngs', 'GYVu', 'GYVu', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYYVu', 'GYV', 'GYVu', 'GYV'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYYVu', 'GYV', 'GYVu', 'GYV']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVu', 'r']], [[-42, 9, -83.5332401941628, -82, 38.16772877208774, {'VtqKcYvzg': 47.40072133316414, 'sLmQQSONWn': -13.009939375362165, 'O': 36, 'rKQ': [48, -59]}, -40], [-42, 9, -83.5332401941628, -82, 38.16772877208774, {'VtqKcYvzg': 47.40072133316414, 'sLmQQSONWn': -13.009939375362165, 'O': 36, 'rKQ': [48, -59]}, -40]], [['r', 'sfIngs', 'GYVu'], [False]], [['GSFVVgWCfDju', 'r', 'sfIngs', 'GYVu', 'r', 'r', 'GSFVVgWCfDju', 'r'], ['GSFVVgWCfDju', 'r', 'sfIngs', 'GYVu', 'r', 'r', 'GSFVVgWCfDju', 'r']], [['sfIngs', 'PctAoxwD', 'GYVu'], ['sfIngs', 'PctAoxwD', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r']], [['sfIngs', 'PctAoxwD', 'GVYVu', 'GYVu', 'PctAoxwD'], ['sfIngs', 'PctAoxwD', 'GVYVu', 'GYVu', 'PctAoxwD']], [['r', 'sfIngs', 'u', 'GYV', 'GYVu'], ['r', 'sfIngs', 'u', 'GYV', 'GYVu']], [['r', 'VtqKcYvzg', 'r'], []], [['GYVur', 'GYYVur', 'sgfIngs', 'GYVu', 'GYVu'], ['GYVur', 'GYYVur', 'sgfIngs', 'GYVu', 'GYVu']], [[True, True, True, False, True, False, False, True, True], [True, True, True, False, True, False, False, True, True]], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'rGSFVVgWCfDju', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'rGSFVVgWCfDju', 'GYVu', 'r']], [['r', 'sfIngs', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'r']], [[-74.03921201241215, 75.22089802044161, -38.48806518576453], []], [[False], [True, False, True]], [['sfIngs', 'GYVu', 'r'], ['sfIngs', 'GYVu', 'r']], [['r', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu'], ['r', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu', 'GYVu']], [['sfIngsGYVu', 'sfIngs', 'GYVu', 'sfIngs', 'sfIngsGYVu'], ['sfIngsGYVu', 'sfIngs', 'GYVu', 'sfIngs', 'sfIngsGYVu']], [['r', 'GYVu', 'r'], [True, True, True, True, False, False, True]], [['r', 'sfInVtqKcYvzggs', 'GYVu'], ['r', 'sfInVtqKcYvzggs', 'GYVu']], [['r', 'GYVu', 'r', 'r'], [True, True, True, False, True, False, False, True]], [[[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 65.5370586539689, 'qyujtuO', 82, 75.22089802044161, 82, 82], [[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 65.5370586539689, 'qyujtuO', 82, 75.22089802044161, 82, 82]], [['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r'], ['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r']], [['r', 'sfIngs', 's'], ['klXTmRZyQ']], [['r', 'GYYVu', 'GYVu'], ['r', 'GYYVu', 'GYVu']], [[[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 90.16807182684596, 'qyujtuO', 82, 82], [[95.17158052544048, 'SFVVgWCfDj', -0.3414328935261324], 90.16807182684596, 'qyujtuO', 82, 82]], [[[95.17158052544048, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 65.5370586539689, [95.17158052544048, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 'qyujtuO', 82, 75.22089802044161, 82], [[95.17158052544048, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 65.5370586539689, [95.17158052544048, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 'qyujtuO', 82, 75.22089802044161, 82]], [['r', 'sfIngs', 'GYVu', 'GYVusfIngSFVGYVVgWCfDjsGYVu', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVusfIngSFVGYVVgWCfDjsGYVu', 'GYVu', 'r']], [['r', 'sfIngs', 's'], ['klXTmRZyQ', 'klXTmRZyQ']], [['sfIngsGYVu', 'sfIngs', 'GYVu', 'ssfIngs', 'sfIngsGYVu'], ['sfIngsGYVu', 'sfIngs', 'GYVu', 'ssfIngs', 'sfIngsGYVu']], [[-49.293443668830214, -0.4410790823334596, 11.89338685730192, 38.68012886425632, 64.91527494125927, 47.40072133316414, -74.03921201241215, 0.3374408817541621], [-49.293443668830214, -0.4410790823334596, 11.89338685730192, 38.68012886425632, 64.91527494125927, 47.40072133316414, -74.03921201241215, 0.3374408817541621]], [['r', 'GYVu', 'FHvMaMnTCg', 'rr'], ['r', 'GYVu', 'FHvMaMnTCg', 'rr']], [['klXTmRZyQr', 'sfIngs', 'GYVu', 'GYVu', 'sfIsngs', 'GYVu'], ['klXTmRZyQr', 'sfIngs', 'GYVu', 'GYVu', 'sfIsngs', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r', 'r']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'GYV', 'GYVu'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'GYV', 'GYVu']], [['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r', 'GYVu'], ['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYYVu', 'GYV', 'GYVVu', 'GYV'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYYVu', 'GYV', 'GYVVu', 'GYV']], [['r', 'GYVu', 'r', 'r'], [True, True, True, True, False, False, True]], [[90.16807182684596, 'qyujtuO', 75.22089802044161, 'sfIngSFVGYVVgWCfDjsGYVu', 'GYYVur', 82], [90.16807182684596, 'qyujtuO', 75.22089802044161, 'sfIngSFVGYVVgWCfDjsGYVu', 'GYYVur', 82]], [['r', 'snfInVtqKcYvzggs', 'sfInVtqKcYvzggs', 'GYVu'], ['r', 'snfInVtqKcYvzggs', 'sfInVtqKcYvzggs', 'GYVu']], [['rGYV', 'GYVu'], ['rGYV', 'GYVu']], [['r', 'rGYV', 'GYVu'], ['r', 'rGYV', 'GYVu']], [[False], [False]], [['sfIngsGYVu', 'GSFVVgWCfDjusfIngs', 'sfIngs', 'GYVu', 'sfIngsGYVu'], ['sfIngsGYVu', 'GSFVVgWCfDjusfIngs', 'sfIngs', 'GYVu', 'sfIngsGYVu']], [['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVVu', 'GYVu', 'r', 'r', 'GYVu', 'r']], [['r', 'GYVu'], ['r', 'GYVu']], [['r', 'sgfIngs', 's', 'GYVu', 'pfIhkuLtSgr', 'GYVu'], ['r', 'sgfIngs', 's', 'GYVu', 'pfIhkuLtSgr', 'GYVu']], [['GYVGu', 'r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r'], ['GYVGu', 'r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'GYVGu', 'r']], [['r', 'sfIngs', 'GYVu', 'GYVusfIngSFVGYVVgWCfDjsGYVu', 's', 'Casb', 'GYVu', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVusfIngSFVGYVVgWCfDjsGYVu', 's', 'Casb', 'GYVu', 'r']], [['sfIngs', 'GYVu', 'sfIngrrs', 'GYVu', 'GOkV', 'GYVGu', 'rr'], ['sfIngs', 'GYVu', 'sfIngrrs', 'GYVu', 'GOkV', 'GYVGu', 'rr']], [['YrGYV', 'GYVu', 'GOku'], ['YrGYV', 'GYVu', 'GOku']], [['GYVu', 'pfIhkuLtSg', 'O', 'Odpagl', 'Casb', 'GYVu'], [[87.8259025409381, 'GYVusfIngSFVGYVVgWCfDjsGYVu', [True, True], {'-51': -74.03921201241215, '60': 40.71791810053759, 'false': 5.735570485483905, '-10': 24.822944608944297, '8': 0.3374408817541621, '41': 64.91527494125927, '-82': -25.52239838327162, '-36': -41.74691632795968, '61': -74.21853866002988, '-83': 99.97028427774339}, False, [66, 68, -71, -71, -82, -65, -51], {'GSFVVgWCfDjusfIngs': 'ssfIngs', 'GYYVu': 'GOkV', 'uTw': 'GYVGu', 's': 'SFVVgWCfDj', 'klXTmRZyQr': 'FHvMaMnTCg', 'sfIngrrs': 'mXw', 'HGEtjdFe': 'sfIsngs', 'DBzU': 'EV', 'sfIngSFVGYVVgWCfDjsGYVu': 'WpVzXU', 'Xf': 'sfIngrrs'}], [], -10, -29, None]], [[True, True, True, False, True, False, False, True, True, False], [True, True, True, False, True, False, False, True, True, False]], [['r', 'sfIngs', 'r', 'GYVVu', 'GYVu', 'r', 'r'], ['r', 'sfIngs', 'r', 'GYVVu', 'GYVu', 'r', 'r']], [['r', 'sfInsfIngSFVGYVVgWCfDjsGYVugs', 'u', 'GYV', 'GYVu'], ['r', 'sfInsfIngSFVGYVVgWCfDjsGYVugs', 'u', 'GYV', 'GYVu']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'ssfIngs', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GYV', 'GYVu', 'ssfIngs', 'r']], [['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'WpVzXU', 'r', 'r'], ['r', 'sfIngs', 'GYVu', 'GYVu', 'GOkV', 'WpVzXU', 'r', 'r']], [[[94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 65.5370586539689, [94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 'qyujtuO', 82, [94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 75.22089802044161, 82], [[94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 65.5370586539689, [94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 'qyujtuO', 82, [94.17409950967779, 'SFVVgWCfDj', 'SFVVgWCfsgfIngsDj', -0.3414328935261324], 75.22089802044161, 82]], [['sgfIngs', 's', 'GYVu', 'pfIhkuLtSgr'], ['sgfIngs', 's', 'GYVu', 'pfIhkuLtSgr']]]
results = [False, True, False, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, False, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True]

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
        func_name = "is_sublist"
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
        for test_case in ['assert is_sublist([2,4,3,5,7],[3,7])==False', 'assert is_sublist([2,4,3,5,7],[4,3])==True', 'assert is_sublist([2,4,3,5,7],[1,6])==False']:
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
