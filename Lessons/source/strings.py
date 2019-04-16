#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # Edge Cases
    if pattern == '':
        return True
    if text == '':
        return False
    
    if find_index_recursive(text, pattern) != None:
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == '':
        return 0
    if text == '':
        return None
    # check if the pattern is in the text
    # Get the first index of text and match it with the first index of pattern
    text_index = 0
    pattern_index = 0
    temp_index = 0

    while text_index < len(text):
        if text[temp_index] == pattern[pattern_index]:
            temp_index += 1
            pattern_index += 1
            if pattern_index == len(pattern):
                return text_index
        else:
            pattern_index = 0
            text_index += 1
            temp_index = text_index
    return None

    
def find_index_recursive(text, pattern, text_index=None, pattern_index=None, temp_index=None): 

    if text_index is None and pattern_index is None and temp_index is None:
        text_index = 0
        pattern_index = 0
        temp_index = 0
    
    if text_index < len(text):
        if text[temp_index] == pattern[pattern_index]:
            if pattern_index == (len(pattern) - 1):
                return text_index
            temp_index += 1
            pattern_index += 1
            return find_index_recursive(text, pattern, text_index, pattern_index, temp_index)
        else:
            pattern_index = 0
            text_index += 1
            temp_index = text_index
            return find_index_recursive(text, pattern, text_index, pattern_index, temp_index)
    return None
            

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if pattern == '':
        return [x for x in range(0, len(text))] 
    # an empty array to store indexes found
    indexes = []
    # call the find index recursive function
    # result = find_index_recursive(text, pattern)

    # while result != None:
    #     indexes.append(result)
        
    # return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
