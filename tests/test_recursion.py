from modules.recursion import flatten_people, my_list


def test_flatten_people():
    names = flatten_people(my_list, [])
    for name in names:
        assert type(name) == str
