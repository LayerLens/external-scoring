METADATA = {
    "subsets": ["algebra", "arithmetic", "geometry"],  # Add your actual subsets here
    "description": "Math expression equivalence testing"
}

def last_boxed_only_string(string):
    """Extract the last \boxed{...} or \fbox{...} element from a string."""
    idx = string.rfind("\\boxed")
    if idx < 0:
        idx = string.rfind("\\fbox")
        if idx < 0:
            return None
            
    i = idx
    right_brace_idx = None
    num_left_braces_open = 0
    while i < len(string):
        if string[i] == "{":
            num_left_braces_open += 1
        if string[i] == "}":
            num_left_braces_open -= 1
            if num_left_braces_open == 0:
                right_brace_idx = i
                break
        i += 1
    
    if right_brace_idx == None:
        return None
        
    return string[idx:right_brace_idx + 1]

def clean_numbers(string):
    """Clean numbers in the given string for consistent formatting."""
    num_prev_digits = 0
    new_string = ""
    for i, c in enumerate(string):
        if c in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            num_prev_digits += 1
        else:
            if num_prev_digits > 3:
                string_number = new_string[-num_prev_digits:]
                new_string = new_string[:-num_prev_digits] + "{0:,}".format(int(string_number))
            num_prev_digits = 0
        new_string += c
    if num_prev_digits > 3:
        string_number = new_string[-num_prev_digits:]
        new_string = new_string[:-num_prev_digits] + "{0:,}".format(int(string_number))
    return new_string

def _fix_fracs(string):
    substrs = string.split("\\frac")
    new_str = substrs[0]
    if len(substrs) > 1:
        substrs = substrs[1:]
        for substr in substrs:
            new_str += "\\frac"
            if substr[0] == "{":
                new_str += substr
            else:
                try:
                    assert len(substr) >= 2
                except:
                    return string
                a = substr[0]
                b = substr[1]
                if b != "{":
                    if len(substr) > 2:
                        post_substr = substr[2:]
                        new_str += "{" + a + "}{" + b + "}" + post_substr
                    else:
                        new_str += "{" + a + "}{" + b + "}"
                else:
                    if len(substr) > 2:
                        post_substr = substr[2:]
                        new_str += "{" + a + "}" + b + post_substr
                    else:
                        new_str += "{" + a + "}" + b
    string = new_str
    return string

def _fix_a_slash_b(string):
    if len(string.split("/")) != 2:
        return string
    a = string.split("/")[0]
    b = string.split("/")[1]
    try:
        a = int(a)
        b = int(b)
        assert string == "{}/{}".format(a, b)
        new_string = "\\frac{" + str(a) + "}{" + str(b) + "}"
        return new_string
    except:
        return string

def _remove_right_units(string):
    # "\\text{ " only ever occurs (at least in the val set) when describing units
    if "\\text{ " in string:
        splits = string.split("\\text{ ")
        assert len(splits) == 2
        return splits[0]
    else:
        return string

def _fix_sqrt(string):
    if "\\sqrt" not in string:
        return string
    splits = string.split("\\sqrt")
    new_string = splits[0] 
    for split in splits[1:]:
        if split[0] != "{":
            a = split[0]
            new_substr = "\\sqrt{" + a + "}" + split[1:]
        else:
            new_substr = "\\sqrt" + split
        new_string += new_substr
    return new_string

def _strip_string(string):
    # linebreaks  
    string = string.replace("\n", "")

    # remove inverse spaces
    string = string.replace("\\!", "")

    # replace \\ with \
    string = string.replace("\\\\", "\\")

    # replace tfrac and dfrac with frac
    string = string.replace("tfrac", "frac")
    string = string.replace("dfrac", "frac")

    # remove \left and \right
    string = string.replace("\\left", "")
    string = string.replace("\\right", "")
    
    # Remove circ (degrees)
    string = string.replace("^{\\circ}", "")
    string = string.replace("^\\circ", "")

    # remove dollar signs
    string = string.replace("\\$", "")
    
    # remove units (on the right)
    string = _remove_right_units(string)

    # remove percentage
    string = string.replace("\\%", "")
    string = string.replace("\%", "")

    # " 0." equivalent to " ." and "{0." equivalent to "{." Alternatively, add "0" if "." is the start of the string
    string = string.replace(" .", " 0.")
    string = string.replace("{.", "{0.")
    # if empty, return empty string
    if len(string) == 0:
        return string
    if string[0] == ".":
        string = "0" + string

    # to consider: get rid of e.g. "k = " or "q = " at beginning
    if len(string.split("=")) == 2:
        if len(string.split("=")[0]) <= 2:
            string = string.split("=")[1]

    # fix sqrt3 --> sqrt{3}
    string = _fix_sqrt(string)

    # remove spaces
    string = string.replace(" ", "")

    # \frac1b or \frac12 --> \frac{1}{b} and \frac{1}{2}, etc. Even works with \frac1{72} (but not \frac{72}1). Also does a/b --> \\frac{a}{b}
    string = _fix_fracs(string)

    # manually change 0.5 --> \frac{1}{2}
    if string == "0.5":
        string = "\\frac{1}{2}"

    # NOTE: X/Y changed to \frac{X}{Y} in dataset, but in simple cases fix in case the model output is X/Y
    string = _fix_a_slash_b(string)

    return string

def extract_and_normalize_answer(string):
    """Extract boxed answer and normalize it."""
    if string is None:
        return None
        
    # Extract boxed content
    boxed = last_boxed_only_string(string)
    if boxed is None:
        return string
        
    # Remove \boxed{} wrapper
    if boxed.startswith("\\boxed{") and boxed.endswith("}"):
        boxed = boxed[7:-1]  # Remove \boxed{ and }
    elif boxed.startswith("\\fbox{") and boxed.endswith("}"):
        boxed = boxed[6:-1]  # Remove \fbox{ and }
    
    # Clean and normalize
    boxed = clean_numbers(boxed)
    boxed = _strip_string(boxed)
    
    return boxed

def is_equiv(str1, str2, verbose=False):
    """Compare two mathematical expressions for equivalence."""
    if str1 is None and str2 is None:
        print("WARNING: Both None")
        return True
    if str1 is None or str2 is None:
        return False

    try:
        # Extract and normalize both answers
        ss1 = extract_and_normalize_answer(str1)
        ss2 = extract_and_normalize_answer(str2)
        
        if verbose:
            print(f"Normalized str1: {ss1}")
            print(f"Normalized str2: {ss2}")
            
        return ss1 == ss2
    except Exception as e:
        print(f"Equivalence check failed: {str(e)}")
        return str1 == str2

def run_tests(response_data):
    """
    Main test function called by the test runner.
    Args:
        response_data: Dict containing response and truth
    Returns:
        bool: True if answers are equivalent
    """
    try:
        # Extract response and truth
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        
        # Get subset for potential subset-specific handling
        subset = response_data['prompt'].get('subset', '')
        
        # Compare using our equivalence function
        return is_equiv(response, truth, verbose=METADATA.get('verbose', False))
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False
