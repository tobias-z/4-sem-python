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


def print_people(people):
    if len(people) == 0:
        return
    for person in people:
        print(person.get("name"))
        print_people(person.get("children"))


if __name__ == "__main__":
    print_people(my_list)
