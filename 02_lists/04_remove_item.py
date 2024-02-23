'''
Write a function, remove_item, that takes a list (items) and a number (n).
Return a new list without the item at position n. This should be a new list and
the item should still exist in the original list

remove_item([1, 2, 3], 1) # returns [1, 3]

remove_item([3], 0) # returns []
'''

from copy import deepcopy
def remove_item(items, n):
    # your code here
    print(items, n)
    result = [];
    # iterating through the indexes of items
    for index in range(len(items)):
        # checking position of the list in order to delete item at 'n' position
        if index == n:
            # creating a deep copy of the list, so that refence will not be shared. 
            result = deepcopy(items)
            del result[index]
    print(result, items)       
    return result;


def test_returns_a_list_without_the_specified_element():
    return_value = remove_item([1], 0)
    assert return_value == []


def test_returns_a_list_including_other_elements():
    return_value = remove_item([1, 2, 3, 4, 5], 2)
    assert return_value == [1, 2, 4, 5]


def test_only_removes_the_specified_element():
    return_value = remove_item([1, 2, 1, 2, 1], 2)
    assert return_value == [1, 2, 2, 1]


def test_returns_a_new_list():
    nums = [1, 2, 3]
    return_value = remove_item(nums, 2)
    assert return_value is not nums, "Returned list should not be the same one that was passed in"  # noqa


def test_element_is_still_included_in_original_list():
    nums = [1, 2, 3]
    remove_item(nums, 2)
    assert nums == [1, 2, 3], "Item should not be removed from original list"
