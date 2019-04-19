#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # Base Case
    if pattern == '':
        return True
    # Edge Case
    if text == '':
        return False
    # return true if there was an index found
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
    # preset indexes to zero
    text_index = 0 # index position to return that stays when a pattern is detected
    pattern_index = 0 # iterator of the pattern to check if the pattern is being met
    ghost_index = 0 # iterator of the text to match the pattern
    # make sure we are within range
    while text_index < (len(text)):
        # if there is a match move on to the next index of the pattern
        if text[ghost_index] == pattern[pattern_index]:
            ghost_index += 1
            pattern_index += 1
            # return the start of the index pattern only if the pattern is fully met
            if pattern_index == len(pattern):
                return text_index
        else: # move on to the next and restart from zero but with the start indexes plus one
            pattern_index = 0
            text_index += 1
            ghost_index = text_index
    return None

    
def find_index_recursive(text, pattern, text_index=None, pattern_index=None, ghost_index=None):
    #
    if text_index is None and pattern_index is None and ghost_index is None:
        text_index = 0
        pattern_index = 0
        ghost_index = 0
    # make sure the indexes are within range
    if text_index < len(text) and ghost_index <= (len(text) -1):
        # check that there is pattern starting
        if text[ghost_index] == pattern[pattern_index]:
            # return the index once we found the entire pattern
            if pattern_index == (len(pattern) - 1):
                return text_index
            # check the following indexes of the pattern
            ghost_index += 1
            pattern_index += 1
            return find_index_recursive(text, pattern, text_index, pattern_index, ghost_index)
        else:
            #  move the text index from its current index plus one and start the pattern from 0
            pattern_index = 0
            text_index += 1
            ghost_index = text_index
            return find_index_recursive(text, pattern, text_index, pattern_index, ghost_index)
    return None
            

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # Base Case returns a value without making any subsequent recursive calls. 
    # It does this for one or more special input values for which the function can be evaluated without recursion.
    if pattern == '':
        return [x for x in range(0, len(text))] 
    # an empty array to store indexes found
    indexes = []
    # get the initial index of the pattern
    result = find_index_recursive(text, pattern)
    while result != None:
        indexes.append(result)
        # move the indexes over by one to make sure we are not starting from its previous index
        start_index = result + 1
        result = find_index_recursive(text, pattern, start_index, 0, start_index)
    return indexes


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
