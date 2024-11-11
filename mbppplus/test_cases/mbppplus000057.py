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
inputs = [[[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]], [[[' red ', 'green'], ['blue ', ' black'], [' orange', 'brown']]], [[['zilver', 'gold'], ['magnesium', 'aluminium'], ['steel', 'bronze']]], [[]], [[['apple', 'banana', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'banana']]], [[['orange', 'green', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'orange', 'green']]], [[['apple', 'banana', 'cherry'], [], ['cherry', 'apple', 'banana']]], [[['apple', 'banana', 'banana'], ['pear', 'pear'], ['orange', 'orange', 'orange']]], [[['apple', 'banana', 'cherry'], [], ['orange', 'plum', 'peach']]], [[['cat', 'dog', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger'], ['monkey']]], [[['pear', 'banana', 'banana'], ['apple', 'orange'], ['kiwi'], ['grape', 'mango', 'apple']]], [[['red', 'green', 'blue'], ['yellow', 'orange'], ['purple', 'pink', 'teal', 'brown']]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x'], ['y', 'z']]], [[[], [], []]], [[['apple', 'banana', 'cherry'], ['orange', 'plum', 'peach']]], [[['cherry', 'apple', 'banana'], ['orange', 'peach', 'plum'], ['banana', 'cherry', 'apple']]], [[['blue', 'red', 'green'], ['brown', 'purple', 'pink', 'teal'], ['orange', 'yellow']]], [[['orange', 'green'], ['white', 'black'], ['black', 'white', 'orange']]], [[['apple', 'zebra', 'cat'], ['dog', 'elephant'], ['giraffe', 'lion', 'banana']]], [[['red', 'green', 'blue'], [], ['orange', 'purple', 'brown']]], [[['cat', 'dog', 'elephant'], ['giraffe', 'tiger', 'zebra'], ['monkey', 'lion', 'tiger'], ['banana']]], [[['cherry', 'banana', 'apple'], ['peach', 'orange', 'plum'], ['cherry', 'banana', 'apple']]], [[['elephant', 'ant', 'bee'], ['dog', 'camel', 'cat'], ['zebra', 'giraffe', 'lion']]], [[['red', 'green', 'blue'], [], ['orange', 'purple', 'brown'], ['yellow', 'pink', 'teal']]], [[['red', 'green', 'bpinklue', 'blue'], ['yellow', 'orange']]], [[['blue', 'red', 'green'], ['brown', 'purple', 'pink', 'teal'], ['brown', 'purple', 'pink', 'teal']]], [[['pear', 'banana', 'banana'], ['apple', 'orange'], ['kiwi'], ['grape', 'mango', 'apple'], ['grape', 'mango', 'apple']]], [[['apple', 'banana', 'cherry'], ['cherry', 'appl', 'banana'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']]], [[['apple', 'orange'], ['kiwi'], ['grape', 'mango', 'apple']]], [[['apple', 'orange'], ['kiwi'], ['grape', 'mango', 'apple'], ['grape', 'mango', 'apple']]], [[['cat', 'dog', 'elephant'], [], ['zebra', 'lion', 'tiger'], ['monkey']]], [[['orange', 'green', 'green'], ['white', 'orange', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'green']]], [[['red', 'green', 'blue'], ['yellow', 'pink'], [], ['orange', 'purple', 'brown'], ['yellow', 'pink'], ['red', 'green', 'blue']]], [[[], ['cat', 'dog', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger'], []]], [[['banaa', 'cherry', 'banana', 'apple'], ['peach', 'orange', 'plum'], ['cherry', 'banana', 'apple']]], [[['cherry', 'apple', 'bsanana', 'banana'], ['apple', 'banana', 'cherry', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'bsanana', 'banana']]], [[['orange', 'green', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'bsanana', 'orange', 'green'], ['black', 'white', 'black', 'white']]], [[['elephant', 'ant', 'bee'], ['zebra', 'giraffe', 'lion']]], [[['white', 'black'], ['black', 'white', 'orange']]], [[['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['peach', 'orange', 'plum'], ['cherry', 'banana', 'apple']]], [[['banana', 'cherry'], ['cherry', 'apple'], ['cherry', 'apple', 'banana']]], [[['elephant', 'ant', 'bee']]], [[['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a'], ['cat', 'dog', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger']]], [[['red', 'green', 'blue'], ['yellow', 'orange']]], [[['apple', 'banana', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'banana'], ['banana', 'cherry', 'apple']]], [[['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['peach', 'orange', 'plum'], ['cherry', 'banana', 'apple', 'apple'], ['cherry', 'banana', 'apple', 'apple']]], [[['elephant', 'ant', 'bee'], ['elephant', 'ant', 'bee']]], [[['cherry', 'apple', 'banana', 'apple'], ['banana', 'cherry'], ['cherry', 'apple'], ['cherry', 'apple', 'banana', 'apple']]], [[[]]], [[['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['cherry', 'banana', 'p'], ['cherry', 'banana', 'apple', 'apple'], ['cherry', 'banana', 'apple', 'apple']]], [[['cherry', 'apple', 'bsanana', 'banana'], ['apple', 'banana', 'cherry', 'cherry']]], [[['dog', 'elephant', 'elephant'], ['dog', 'elephant', 'elephant'], ['giraffe', 'lion', 'banana']]], [[['cherry', 'apple', 'banana'], ['orange', 'peach', 'plum'], ['banana', 'cherry', 'apple'], ['banana', 'cherry', 'apple'], ['banana', 'cherry', 'apple'], ['orange', 'peach', 'plum']]], [[['cherry', 'apple', 'banana', 'apple'], ['cherry', 'apple'], ['cherry', 'apple', 'banana', 'apple']]], [[['apple', 'banana', 'cherry'], ['cherry', 'appl', 'banana', 'banana'], ['apple', 'banana', 'cherry'], ['cherry', 'appl', 'banana', 'banana'], ['apple', 'banana', 'cherry']]], [[['cherry', 'banana', 'apple'], ['peach', 'orange', 'plum'], ['cherry', 'banana', 'apple'], ['peach', 'orange', 'plum']]], [[[], ['cat', 'dog', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger'], [], [], [], []]], [[['orange', 'green', 'green'], ['white', 'orange', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'green'], ['black', 'white', 'black', 'white']]], [[['red', 'green'], ['red', 'green'], ['yellow', 'orange']]], [[['red', 'green', 'blue', 'green'], ['yellow'], ['red', 'green', 'blue', 'green'], ['yellow']]], [[['apple', 'banana', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'banana'], ['cherry', 'apple', 'banana']]], [[['black', 'orange', 'green'], ['white', 'black'], ['black', 'orange', 'green'], ['black', 'white', 'orange']]], [[['cbpinklueherry', 'cherry', 'apple', 'bsanana', 'banana'], ['banana', 'cherry', 'apple'], ['cbpinklueherry', 'cherry', 'apple', 'bsanana', 'banana']]], [[['orange', 'green']]], [[['cherry', 'apple', 'bsanana', 'banana'], ['orange', 'peach', 'plum'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'bsanana', 'banana'], ['banana', 'cherry', 'apple'], ['banana', 'cherry', 'apple'], ['orange', 'peach', 'plum']]], [[['apple', 'orange'], ['grape', 'mango', 'apple', 'grape'], ['grape', 'mango', 'apple', 'grape'], ['grape', 'mango', 'apple', 'grape']]], [[['zebra', 'lion', 'tiger', 'zebra'], ['cat', 'dog', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger', 'zebra'], ['monkey']]], [[['cherry', 'banana', 'apple'], ['peach', 'orage', 'plum'], ['peach', 'orage', 'plum'], ['cherry', 'banana', 'apple']]], [[['red', 'green'], ['red', 'green'], ['yellow', 'orange'], ['red', 'green']]], [[['red', 'green', 'blue', 'green'], ['yellow', 'yellow'], ['red', 'green', 'blue', 'green'], ['yellow', 'yellow'], ['yellow', 'yellow']]], [[['ngeant', 'nge']]], [[['red', 'green', 'blue'], ['yellow', 'orange'], ['purple', 'pink', 'teal', 'brown'], ['red', 'green', 'blue']]], [[['apple', 'banana', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple'], ['cherry', 'apple'], ['cherry', 'apple']]], [[['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a'], ['cat', 'dog', 'helephant', 'elephant'], ['cat', 'dog', 'helephant', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger']]], [[['red', 'green', 'blue', 'red'], ['yellow', 'orange']]], [[['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a', 'e'], ['cat', 'dog', 'elephant'], ['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a', 'e'], [], [], ['zebra', 'lion', 'tiger']]], [[[], ['cat', 'dog', 'elephant'], ['zebra', 'lion'], ['giraffe'], ['zebra', 'lion'], []]], [[['banana', 'cherry', 'apple'], ['cherry', 'apple', 'banana'], ['cherry', 'apple', 'banana']]], [[['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'orange', 'green'], ['white', 'orange', 'orange', 'green']]], [[['cat', 'dog', 'elephant'], [], ['zebra', 'lion', 'tiger'], ['monkey'], []]], [[['apple', 'banana', 'banana'], ['ant', 'pear', 'pear', 'pear'], ['ant', 'pear', 'pear', 'pear'], ['orange', 'orange', 'orange', 'orange'], ['orange', 'orange', 'orange', 'orange']]], [[['cherry', 'apple', 'banana', 'apple'], ['banana', 'cherry', 'banana'], ['banana', 'cherry', 'banana'], ['cherry', 'apple'], ['cherry', 'apple', 'banana', 'apple']]], [[['cat', 'dog', 'elephant'], ['giraffe', 'tiger', 'zebra'], ['monkey', 'lion', 'tiger']]], [[['cherry', 'apple', 'apple'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple']]], [[[], ['orange', 'purple', 'brown'], ['yellow', 'teai', 'pink', 'teal']]], [[['appletiger', 'banana', 'cherry', 'cherry'], ['cherry', 'apple', 'bsanana', 'banana'], ['appletiger', 'banana', 'cherry', 'cherry'], ['banana', 'cherry', 'apple'], ['cherry', 'apple', 'bsanana', 'banana']]], [[['apple', 'banana', 'mango'], ['apple', 'banana', 'mango'], ['cherry', 'appl', 'banana'], ['apple', 'banana', 'mango'], ['apple', 'banana', 'mango']]], [[['orange', 'orabluenge', 'e'], ['apple', 'banana', 'banana'], ['orange', 'orabluenge', 'e'], ['pear', 'pear'], ['orange', 'orabluenge', 'e'], ['apple', 'banana', 'banana']]], [[['apple', 'banana', 'banana'], ['pear', 'pear'], ['orange', 'orange']]], [[['red', 'green', 'orange', 'blue'], [], ['orange', 'purple', 'brown'], ['yellow', 'pink', 'teal']]], [[['banana', 'cherry', 'apple'], ['cdherry', 'apple', 'banana'], ['cdherry', 'apple', 'banana']]], [[['black', 'orange', 'green'], ['white', 'black'], ['black', 'orange', 'green'], ['black', 'white', 'orange'], ['black', 'white', 'orange']]], [[['orange', 'green', 'green', 'orange'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'bsanana', 'orange', 'green'], ['black', 'white', 'black', 'white']]], [[['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'orange', 'green'], ['white', 'orange', 'orange', 'green'], ['apple', 'green'], ['apple', 'green']]], [[['blue', 'red', 'green'], ['orange', 'yellow', 'orange'], ['brown', 'purple', 'pink', 'teal'], ['orange', 'yellow', 'orange']]], [[['elephant', 'ant', 'bee'], ['dog', 'camel', 'cat'], ['zebra', 'giraffe', 'lion'], ['dog', 'camel', 'cat']]], [[['cherry', 'apple', 'bsanana', 'banana'], ['orange', 'kiwi', 'plum', 'plum'], ['banana', 'cherry', 'apple', 'cherry'], ['cherry', 'apple', 'bsanana', 'banana'], ['orange', 'kiwi', 'plum', 'plum'], ['banana', 'cherry', 'apple', 'cherry'], ['banana', 'cherry', 'apple', 'cherry'], ['orange', 'kiwi', 'plum', 'plum']]], [[['banana', 'cherry'], ['cherry', 'apple'], ['cherry', 'apple', 'banana'], ['banana', 'cherry']]], [[['red'], ['red'], ['red'], ['yellow', 'orange'], ['red']]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x'], ['y', 'z']]], [[['red', 'green', 'blue', 'green', 'green'], ['red', 'green', 'blue', 'green', 'green'], ['red', 'green', 'blue', 'green', 'green'], ['yellow', 'yellow'], ['yellow', 'yellow'], ['red', 'green', 'blue', 'green', 'green']]], [[['pear', 'bakna', 'banana'], ['apple', 'orange'], ['kiwi'], ['grape', 'mango', 'apple'], ['grape', 'mango', 'apple']]], [[['pear', 'banana', 'banana'], ['apple', 'orange'], ['kiwi'], ['grape', 'pgrape', 'mango', 'apple']]], [[['a', 'orabluenge', 'e'], ['pear', 'pear', 'pear'], ['apple', 'banana', 'banana'], ['a', 'orabluenge', 'e'], ['pear', 'pear', 'pear'], ['a', 'orabluenge', 'e'], ['a', 'orabluenge', 'e'], ['apple', 'banana', 'banana']]], [[['cherry', 'apple', 'apple'], ['banana', 'chlrry', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple']]], [[['cat', 'banana', 'apple'], ['cherry', 'banana', 'apple'], ['peach', 'orange', 'plum'], ['cat', 'banana', 'apple']]], [[['orange', 'yellow', 'orange', 'orange'], ['blue', 'red', 'green'], ['orange', 'yellow', 'orange', 'orange'], ['brown', 'purple', 'pink', 'teal'], ['orange', 'yellow', 'orange', 'orange']]], [[['banana', 'cherry'], ['cherry', 'apple']]], [[['red', 'green', 'p', 'green'], ['yellow'], ['red', 'green', 'p', 'green'], ['yellow'], ['red', 'green', 'p', 'green']]], [[['cherry', 'apple', 'banana', 'apple'], ['banana', 'cherry', 'banana'], ['banana', 'cherry', 'banana'], ['cherry', 'apple', 'banana', 'apple']]], [[['pear', 'banana', 'banana'], ['apple', 'orange'], ['kiwi'], ['grape', 'apple'], ['grape', 'apple'], ['grape', 'apple']]], [[['red', 'green', 'orange', 'blue'], [], ['orange', 'purple'], ['orange', 'purple'], ['yellow', 'pink', 'teal']]], [[['cat', 'dog', 'elephant'], ['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a', 'e'], [], [], ['zebra', 'lion', 'tiger'], ['zebra', 'lion', 'tiger'], ['zebra', 'lion', 'tiger']]], [[['cherry', 'apple', 'apple'], ['banana', 'chlrry', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple'], ['cherry', 'apple', 'apple']]], [[['cherry', 'apple', 'banana'], ['orange', 'peach', 'plum'], ['banana', 'cherry', 'apple'], ['banana', 'cherry', 'apple'], ['orange', 'peach', 'plum']]], [[['apple', 'banana'], ['orange', 'orabluenge', 'e'], ['apple', 'banana'], ['orange', 'orabluenge', 'e'], ['pear', 'pear'], ['orange', 'orabluenge', 'e'], ['apple', 'banana']]], [[['cherry', 'apple', 'bsanana', 'banana'], ['orange', 'kiwi', 'plum', 'plum'], ['banana', 'cherry', 'apple', 'abanana', 'cherry'], ['cherry', 'apple', 'bsanana', 'banana'], ['orange', 'kiwi', 'plum', 'plum'], ['banana', 'cherry', 'apple', 'abanana', 'cherry'], ['orange', 'kiwi', 'plum', 'plum']]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x']]], [[['red', 'green', 'blue', 'green', 'green'], ['red', 'green', 'blue', 'green', 'green'], ['red', 'green', 'blue', 'green', 'green'], ['yellow', 'yellow'], ['yellow', 'yellow'], ['red', 'green', 'blue', 'green', 'green'], ['yellow', 'yellow']]], [[['cat', 'banana', 'apple'], ['cherry', 'banana', 'apple'], ['peach', 'orange', 'plum', 'plum'], ['peach', 'orange', 'plum', 'plum']]], [[['IODiWvh', 'e', 'f', 'dog', 'r', 'cat', 'a'], ['cat', 'dog', 'helephant', 'elephant'], ['cat', 'dog', 'helephant', 'elephant'], ['giraffe'], ['zebra', 'lion', 'tiger'], ['cat', 'dog', 'helephant', 'elephant']]], [[['apple', 'orange'], ['grape', 'mango', 'n', 'grape'], ['grape', 'mango', 'n', 'grape'], ['grape', 'mango', 'n', 'grape']]], [[['dog', 'camel', 'cat'], ['zebra', 'giraffe', 'lion']]], [[['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'white', 'black', 'white'], ['white', 'orange', 'green'], ['white', 'orange', 'green']]]]
results = [[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']], [[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']], [['gold', 'zilver'], ['aluminium', 'magnesium'], ['bronze', 'steel']], [], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['green', 'green', 'orange'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'orange', 'white']], [['apple', 'banana', 'cherry'], [], ['apple', 'banana', 'cherry']], [['apple', 'banana', 'banana'], ['pear', 'pear'], ['orange', 'orange', 'orange']], [['apple', 'banana', 'cherry'], [], ['orange', 'peach', 'plum']], [['cat', 'dog', 'elephant'], ['giraffe'], ['lion', 'tiger', 'zebra'], ['monkey']], [['banana', 'banana', 'pear'], ['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango']], [['blue', 'green', 'red'], ['orange', 'yellow'], ['brown', 'pink', 'purple', 'teal']], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x'], ['y', 'z']], [[], [], []], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum']], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry']], [['blue', 'green', 'red'], ['brown', 'pink', 'purple', 'teal'], ['orange', 'yellow']], [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']], [['apple', 'cat', 'zebra'], ['dog', 'elephant'], ['banana', 'giraffe', 'lion']], [['blue', 'green', 'red'], [], ['brown', 'orange', 'purple']], [['cat', 'dog', 'elephant'], ['giraffe', 'tiger', 'zebra'], ['lion', 'monkey', 'tiger'], ['banana']], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry']], [['ant', 'bee', 'elephant'], ['camel', 'cat', 'dog'], ['giraffe', 'lion', 'zebra']], [['blue', 'green', 'red'], [], ['brown', 'orange', 'purple'], ['pink', 'teal', 'yellow']], [['blue', 'bpinklue', 'green', 'red'], ['orange', 'yellow']], [['blue', 'green', 'red'], ['brown', 'pink', 'purple', 'teal'], ['brown', 'pink', 'purple', 'teal']], [['banana', 'banana', 'pear'], ['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango'], ['apple', 'grape', 'mango']], [['apple', 'banana', 'cherry'], ['appl', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango']], [['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango'], ['apple', 'grape', 'mango']], [['cat', 'dog', 'elephant'], [], ['lion', 'tiger', 'zebra'], ['monkey']], [['green', 'green', 'orange'], ['green', 'orange', 'white'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'white']], [['blue', 'green', 'red'], ['pink', 'yellow'], [], ['brown', 'orange', 'purple'], ['pink', 'yellow'], ['blue', 'green', 'red']], [[], ['cat', 'dog', 'elephant'], ['giraffe'], ['lion', 'tiger', 'zebra'], []], [['apple', 'banaa', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry']], [['apple', 'banana', 'bsanana', 'cherry'], ['apple', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry']], [['green', 'green', 'orange'], ['black', 'black', 'white', 'white'], ['bsanana', 'green', 'orange', 'orange', 'white'], ['black', 'black', 'white', 'white']], [['ant', 'bee', 'elephant'], ['giraffe', 'lion', 'zebra']], [['black', 'white'], ['black', 'orange', 'white']], [['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry']], [['banana', 'cherry'], ['apple', 'cherry'], ['apple', 'banana', 'cherry']], [['ant', 'bee', 'elephant']], [['IODiWvh', 'a', 'cat', 'dog', 'e', 'f', 'r'], ['cat', 'dog', 'elephant'], ['giraffe'], ['lion', 'tiger', 'zebra']], [['blue', 'green', 'red'], ['orange', 'yellow']], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['orange', 'peach', 'plum'], ['apple', 'apple', 'banana', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [['ant', 'bee', 'elephant'], ['ant', 'bee', 'elephant']], [['apple', 'apple', 'banana', 'cherry'], ['banana', 'cherry'], ['apple', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [[]], [['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['banana', 'cherry', 'p'], ['apple', 'apple', 'banana', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [['apple', 'banana', 'bsanana', 'cherry'], ['apple', 'banana', 'cherry', 'cherry']], [['dog', 'elephant', 'elephant'], ['dog', 'elephant', 'elephant'], ['banana', 'giraffe', 'lion']], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum']], [['apple', 'apple', 'banana', 'cherry'], ['apple', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [['apple', 'banana', 'cherry'], ['appl', 'banana', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['appl', 'banana', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum']], [[], ['cat', 'dog', 'elephant'], ['giraffe'], ['lion', 'tiger', 'zebra'], [], [], [], []], [['green', 'green', 'orange'], ['green', 'orange', 'white'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'white'], ['black', 'black', 'white', 'white']], [['green', 'red'], ['green', 'red'], ['orange', 'yellow']], [['blue', 'green', 'green', 'red'], ['yellow'], ['blue', 'green', 'green', 'red'], ['yellow']], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['black', 'green', 'orange'], ['black', 'white'], ['black', 'green', 'orange'], ['black', 'orange', 'white']], [['apple', 'banana', 'bsanana', 'cbpinklueherry', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'bsanana', 'cbpinklueherry', 'cherry']], [['green', 'orange']], [['apple', 'banana', 'bsanana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum']], [['apple', 'orange'], ['apple', 'grape', 'grape', 'mango'], ['apple', 'grape', 'grape', 'mango'], ['apple', 'grape', 'grape', 'mango']], [['lion', 'tiger', 'zebra', 'zebra'], ['cat', 'dog', 'elephant'], ['giraffe'], ['lion', 'tiger', 'zebra', 'zebra'], ['monkey']], [['apple', 'banana', 'cherry'], ['orage', 'peach', 'plum'], ['orage', 'peach', 'plum'], ['apple', 'banana', 'cherry']], [['green', 'red'], ['green', 'red'], ['orange', 'yellow'], ['green', 'red']], [['blue', 'green', 'green', 'red'], ['yellow', 'yellow'], ['blue', 'green', 'green', 'red'], ['yellow', 'yellow'], ['yellow', 'yellow']], [['nge', 'ngeant']], [['blue', 'green', 'red'], ['orange', 'yellow'], ['brown', 'pink', 'purple', 'teal'], ['blue', 'green', 'red']], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'cherry'], ['apple', 'cherry'], ['apple', 'cherry']], [['IODiWvh', 'a', 'cat', 'dog', 'e', 'f', 'r'], ['cat', 'dog', 'elephant', 'helephant'], ['cat', 'dog', 'elephant', 'helephant'], ['giraffe'], ['lion', 'tiger', 'zebra']], [['blue', 'green', 'red', 'red'], ['orange', 'yellow']], [['IODiWvh', 'a', 'cat', 'dog', 'e', 'e', 'f', 'r'], ['cat', 'dog', 'elephant'], ['IODiWvh', 'a', 'cat', 'dog', 'e', 'e', 'f', 'r'], [], [], ['lion', 'tiger', 'zebra']], [[], ['cat', 'dog', 'elephant'], ['lion', 'zebra'], ['giraffe'], ['lion', 'zebra'], []], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']], [['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'orange', 'white'], ['green', 'orange', 'orange', 'white']], [['cat', 'dog', 'elephant'], [], ['lion', 'tiger', 'zebra'], ['monkey'], []], [['apple', 'banana', 'banana'], ['ant', 'pear', 'pear', 'pear'], ['ant', 'pear', 'pear', 'pear'], ['orange', 'orange', 'orange', 'orange'], ['orange', 'orange', 'orange', 'orange']], [['apple', 'apple', 'banana', 'cherry'], ['banana', 'banana', 'cherry'], ['banana', 'banana', 'cherry'], ['apple', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [['cat', 'dog', 'elephant'], ['giraffe', 'tiger', 'zebra'], ['lion', 'monkey', 'tiger']], [['apple', 'apple', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry']], [[], ['brown', 'orange', 'purple'], ['pink', 'teai', 'teal', 'yellow']], [['appletiger', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry'], ['appletiger', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry']], [['apple', 'banana', 'mango'], ['apple', 'banana', 'mango'], ['appl', 'banana', 'cherry'], ['apple', 'banana', 'mango'], ['apple', 'banana', 'mango']], [['e', 'orabluenge', 'orange'], ['apple', 'banana', 'banana'], ['e', 'orabluenge', 'orange'], ['pear', 'pear'], ['e', 'orabluenge', 'orange'], ['apple', 'banana', 'banana']], [['apple', 'banana', 'banana'], ['pear', 'pear'], ['orange', 'orange']], [['blue', 'green', 'orange', 'red'], [], ['brown', 'orange', 'purple'], ['pink', 'teal', 'yellow']], [['apple', 'banana', 'cherry'], ['apple', 'banana', 'cdherry'], ['apple', 'banana', 'cdherry']], [['black', 'green', 'orange'], ['black', 'white'], ['black', 'green', 'orange'], ['black', 'orange', 'white'], ['black', 'orange', 'white']], [['green', 'green', 'orange', 'orange'], ['black', 'black', 'white', 'white'], ['bsanana', 'green', 'orange', 'orange', 'white'], ['black', 'black', 'white', 'white']], [['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'orange', 'white'], ['green', 'orange', 'orange', 'white'], ['apple', 'green'], ['apple', 'green']], [['blue', 'green', 'red'], ['orange', 'orange', 'yellow'], ['brown', 'pink', 'purple', 'teal'], ['orange', 'orange', 'yellow']], [['ant', 'bee', 'elephant'], ['camel', 'cat', 'dog'], ['giraffe', 'lion', 'zebra'], ['camel', 'cat', 'dog']], [['apple', 'banana', 'bsanana', 'cherry'], ['kiwi', 'orange', 'plum', 'plum'], ['apple', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry'], ['kiwi', 'orange', 'plum', 'plum'], ['apple', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'cherry', 'cherry'], ['kiwi', 'orange', 'plum', 'plum']], [['banana', 'cherry'], ['apple', 'cherry'], ['apple', 'banana', 'cherry'], ['banana', 'cherry']], [['red'], ['red'], ['red'], ['orange', 'yellow'], ['red']], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x'], ['y', 'z']], [['blue', 'green', 'green', 'green', 'red'], ['blue', 'green', 'green', 'green', 'red'], ['blue', 'green', 'green', 'green', 'red'], ['yellow', 'yellow'], ['yellow', 'yellow'], ['blue', 'green', 'green', 'green', 'red']], [['bakna', 'banana', 'pear'], ['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango'], ['apple', 'grape', 'mango']], [['banana', 'banana', 'pear'], ['apple', 'orange'], ['kiwi'], ['apple', 'grape', 'mango', 'pgrape']], [['a', 'e', 'orabluenge'], ['pear', 'pear', 'pear'], ['apple', 'banana', 'banana'], ['a', 'e', 'orabluenge'], ['pear', 'pear', 'pear'], ['a', 'e', 'orabluenge'], ['a', 'e', 'orabluenge'], ['apple', 'banana', 'banana']], [['apple', 'apple', 'cherry'], ['apple', 'banana', 'chlrry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry']], [['apple', 'banana', 'cat'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cat']], [['orange', 'orange', 'orange', 'yellow'], ['blue', 'green', 'red'], ['orange', 'orange', 'orange', 'yellow'], ['brown', 'pink', 'purple', 'teal'], ['orange', 'orange', 'orange', 'yellow']], [['banana', 'cherry'], ['apple', 'cherry']], [['green', 'green', 'p', 'red'], ['yellow'], ['green', 'green', 'p', 'red'], ['yellow'], ['green', 'green', 'p', 'red']], [['apple', 'apple', 'banana', 'cherry'], ['banana', 'banana', 'cherry'], ['banana', 'banana', 'cherry'], ['apple', 'apple', 'banana', 'cherry']], [['banana', 'banana', 'pear'], ['apple', 'orange'], ['kiwi'], ['apple', 'grape'], ['apple', 'grape'], ['apple', 'grape']], [['blue', 'green', 'orange', 'red'], [], ['orange', 'purple'], ['orange', 'purple'], ['pink', 'teal', 'yellow']], [['cat', 'dog', 'elephant'], ['IODiWvh', 'a', 'cat', 'dog', 'e', 'e', 'f', 'r'], [], [], ['lion', 'tiger', 'zebra'], ['lion', 'tiger', 'zebra'], ['lion', 'tiger', 'zebra']], [['apple', 'apple', 'cherry'], ['apple', 'banana', 'chlrry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry'], ['apple', 'apple', 'cherry']], [['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum'], ['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum']], [['apple', 'banana'], ['e', 'orabluenge', 'orange'], ['apple', 'banana'], ['e', 'orabluenge', 'orange'], ['pear', 'pear'], ['e', 'orabluenge', 'orange'], ['apple', 'banana']], [['apple', 'banana', 'bsanana', 'cherry'], ['kiwi', 'orange', 'plum', 'plum'], ['abanana', 'apple', 'banana', 'cherry', 'cherry'], ['apple', 'banana', 'bsanana', 'cherry'], ['kiwi', 'orange', 'plum', 'plum'], ['abanana', 'apple', 'banana', 'cherry', 'cherry'], ['kiwi', 'orange', 'plum', 'plum']], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'], ['i', 'j', 'j'], ['k', 'l'], ['m', 'n'], ['o', 'p'], ['q', 'r'], ['s', 't'], ['u', 'v'], ['w', 'x']], [['blue', 'green', 'green', 'green', 'red'], ['blue', 'green', 'green', 'green', 'red'], ['blue', 'green', 'green', 'green', 'red'], ['yellow', 'yellow'], ['yellow', 'yellow'], ['blue', 'green', 'green', 'green', 'red'], ['yellow', 'yellow']], [['apple', 'banana', 'cat'], ['apple', 'banana', 'cherry'], ['orange', 'peach', 'plum', 'plum'], ['orange', 'peach', 'plum', 'plum']], [['IODiWvh', 'a', 'cat', 'dog', 'e', 'f', 'r'], ['cat', 'dog', 'elephant', 'helephant'], ['cat', 'dog', 'elephant', 'helephant'], ['giraffe'], ['lion', 'tiger', 'zebra'], ['cat', 'dog', 'elephant', 'helephant']], [['apple', 'orange'], ['grape', 'grape', 'mango', 'n'], ['grape', 'grape', 'mango', 'n'], ['grape', 'grape', 'mango', 'n']], [['camel', 'cat', 'dog'], ['giraffe', 'lion', 'zebra']], [['apple', 'green'], ['apple', 'green'], ['apple', 'green'], ['black', 'black', 'white', 'white'], ['green', 'orange', 'white'], ['green', 'orange', 'white']]]

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
        func_name = "sort_sublists"
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
        for test_case in ['assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[[\'green\', \'orange\'], [\'black\', \'white\'], [\'black\', \'orange\', \'white\']]', 'assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[\' red \', \'green\'], [\' black\', \'blue \'], [\' orange\', \'brown\']]', 'assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[[\'gold\', \'zilver\'],[\'aluminium\', \'magnesium\'], [\'bronze\', \'steel\']]']:
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
