from typing import List


my_list = [
    {
        "name": "Bob",
        "children": [
            {
                "name": "bob child",
                "children": [
                    {"name": "bob child's child", "children": []},
                ],
            },
            {"name": "bob child2", "children": []},
        ],
    },
    {
        "name": "Tobias",
        "children": [
            {"name": "Tobias child", "children": []},
            {"name": "Tobias child2", "children": []},
        ],
    },
]

#################################################################################
# Print all the peoples names


def print_people(people):
    if len(people) == 0:
        return
    for person in people:
        print(person.get("name"))
        print_people(person.get("children"))


#################################################################################
# Flatten people returning only their names in a list


def flatten_people(people, flattened_people: List[str]):
    result = []

    for person in people:
        flattened_people.append(person.get("name"))
        result = [*result, *get_children(person.get("children"), flattened_people)]

    return result


def get_children(people, flattened_people):
    if len(people) == 0:
        return flattened_people

    for child in people:
        flattened_people.append(child.get("name"))
        return get_children(child.get("children"), flattened_people)


if __name__ == "__main__":
    print_people(my_list)
    print(flatten_people(my_list, []))
