"""
Northcoders is expanding to France!

Unfortunately for us, our team on the ground in Paris are patriotically
Francophone and have been providing us with student data partly in French.

Write a function that will take a dictionary representing a student's data, a
key that needs changing, and its English translation.

The function should return a new dictionary with the relevant key name changed
to its English translation.

If the key to change does not exist in the student then no changes should be
made.

student = {
    'prénom': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

translate_key(student, 'prénom', 'first_name') # should return the following:

{
    'first_name': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

"""

from copy import deepcopy
def translate_key(student, key_to_change, translation):
    # Your code here
    result = deepcopy(student)
    print(student, key_to_change, translation)
    if len(student.keys()) == 0:
        return {}
    elif key_to_change not in result.keys():
        return result
    else:
        result[translation] = result[key_to_change]
        del result[key_to_change]
        return result


def test_return_copy_of_empty_data_unchanged():
    student = {}
    assert translate_key(student, 'prénom', 'first_name') == {}
    assert translate_key(student, 'prénom', 'first_name') is not student


def test_return_unchanged_if_key_not_present():
    student = {
        'first_name': 'Carla',
        'surname': 'Bruni',
        'job': 'Artist'
    }
    assert translate_key(student, 'prénom', 'first_name') == student
    assert translate_key(student, 'prénom', 'first_name') is not student


def test_translate_key_if_required():
    student1 = {
        'prénom': 'Carla',
        'surname': 'Bruni',
        'job': 'Artist'
    }
    expected1 = {
        'first_name': 'Carla',
        'surname': 'Bruni',
        'job': 'Artist'
    }
    result1 = translate_key(student1, 'prénom', 'first_name')

    assert result1 == expected1
    assert result1 is not student1

    student2 = {
        'first_name': 'Jean',
        'surname': 'Reno',
        'emploi': 'Actor'
    }
    expected2 = {
        'first_name': 'Jean',
        'surname': 'Reno',
        'job': 'Actor'
    }
    result2 = translate_key(student2, 'emploi', 'job')

    assert result2 == expected2
    assert result2 is not student2
