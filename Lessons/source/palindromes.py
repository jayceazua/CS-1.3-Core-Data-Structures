#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


LETTERS = frozenset(string.ascii_letters)  # CS1.3 in class code review - Sam's code
def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    left_index = 0
    right_index = (len(text) - 1)
    # check if right and left are equal to exit out
    while left_index <= right_index:  # use while instead for time complex - Faith
        # get the character from the left and make sure that it is a letter
        while text[left_index] not in LETTERS:
            left_index += 1
            # increment the left
        # right "as above as below"
        while text[right_index] not in LETTERS:
            right_index -= 1
            # decrement the right until a letter is found
        # compare the two return false if it is not thr same <- lowercase the letter
        if text[left_index].lower() != text[right_index].lower():
            return False
        # else perform the increment and decrement
        left_index += 1
        right_index -= 1
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    # prevent case sensitive errors


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # Set the left and right variables to their initial values if they are found to both be None
    if left == None and right == None:
        left = 0
        right = (len(text) - 1)
    # only continue if the left index does not pass the right
    if left <= right:
        # if the charcter on the left is not a letter restart the recusiveness with an increased left index
        if text[left] not in LETTERS:
            left += 1
            return is_palindrome_recursive(text, left, right)
        # Same as above but checks for right and substract down on the right
        if text[right] not in LETTERS:
            right -= 1
            return is_palindrome_recursive(text, left, right)
        # if they are not equal return False
        if text[left].lower() != text[right].lower():
            return False
        # continue through the recursiveness 
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)
    # it is a palindrome
    return True
    
    
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
