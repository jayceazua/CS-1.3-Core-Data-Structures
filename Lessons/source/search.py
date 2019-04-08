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
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index > (len(array) - 1):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    array = sorted(array)
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    #  create a variable for the left and right boundaries
    left_bound = 0 # left being the start of the array
    right_bound = (len(array) -1) # right being the end of the array
    # add the left and right boundaries and divide them by half
    current_middle_index = (left_bound + right_bound) // 2
    # While the current index is between the boundaries continue
    while left_bound <= current_middle_index and right_bound >= current_middle_index:
        # if the current index value is equal to the item we are searching for
        if array[current_middle_index] == item:
            # return that current index
            return current_middle_index
        # if not then we move on to check if the value of that current index is greater than the item
        elif array[current_middle_index] > item:
            # if it is greater than that the item then we reassign the right boundary to the current index minus 1
            right_bound = current_middle_index - 1
        # Check is the current index value is less than
        elif array[current_middle_index] < item:
            # if it is less than that the item then we reassign the left boundary to the current index plus 1
            left_bound = current_middle_index + 1
        # then add the left anf right boundary and divide it by its half
        current_middle_index = (left_bound + right_bound) // 2
    # if the the item is not found return None
    return None

    
    

    


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    pass


def main():
    names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
    contain = 'Julia'
    not_contain = 'Jeremy'

    print(binary_search(names, contain))
    print(binary_search(names, not_contain))


if __name__ == '__main__':
    main()
