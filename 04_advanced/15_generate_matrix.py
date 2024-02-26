"""
Write a function that takes a `number` and returns a matrix of nested lists
equal to the number passed.
Each element in each sublist should be set to a value of `None`.


generate_matrix(1) # returns [[None]]

generate_matrix(2) # returns [[None, None], [None, None]]

generate_matrix(3) # returns [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

"""


def generate_matrix(number):
    # Your code here
    result = []
    for i in range(number):
        # init row 
        row = []
        for column in range(number):
            # adding ele into row
            row.append(None)
        # adding row to the list
        result.append(row)
    return result


def test_zero_generates_empty_list():
    assert generate_matrix(0) == []


def test_one():
    assert generate_matrix(1) == [[None]]


def test_two():
    assert generate_matrix(2) == [[None, None], [None, None]]


def test_three():
    assert generate_matrix(3) == [[None, None, None], [
        None, None, None], [None, None, None]]


def test_arbitrary():
    import random
    number = random.randint(4, 20)
    result = generate_matrix(number)
    assert len(result) == number
    for j in range(number):
        assert len(result[j]) == number
        for k in range(number):
            assert result[j][k] == None  # noqa
