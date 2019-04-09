#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index 
    return None  


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index > (len(array) - 1): # check is the index is out of range
        return None 
    if array[index] == item: # check if the current index value is equal to the item
        return index
    else:
        # if it is not the same continue onto the next iteration
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    array = sorted(array)
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    #  create a variable for the left and right boundaries
    left_bound = 0 # left is the zero index of the array
    right_bound = (len(array) -1) # right is the full length of the array
    #
    while left_bound <= right_bound:
        #
        current_middle_index = ((left_bound + right_bound) // 2) 
        middle_value = array[current_middle_index]
        #
        if middle_value == item: 
            return current_middle_index
        #
        elif middle_value > item:
            right_bound = current_middle_index - 1
        #
        elif middle_value < item:
            left_bound = current_middle_index + 1
    # never found item - python and ruby we don't need a return
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    #
    if left == None and right == None:
        left = 0
        right = (len(array) - 1)
    #
    middle_index = (left + right) // 2
    middle_value = array[middle_index]
    # 
    if left > right:
        return None
    #
    if middle_value == item:
        return middle_index
    #
    if middle_value > item:
        right = middle_index - 1
        return binary_search_recursive(array, item, left, right)
    #
    left = middle_index + 1
    return binary_search_recursive(array, item, left, right)


    


def main():
    names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
    contain = 'Julia'
    not_contain = 'Jeremy'

    print(binary_search(names, contain))
    print(binary_search(names, not_contain))


if __name__ == '__main__':
    main()
