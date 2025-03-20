class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    object_list = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        object_list.append(person_obj)

    for person in people:
        person_obj = Person.people[person["name"]]

        if "wife" in person and person["wife"] in Person.people:
            person_obj.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] in Person.people:
            person_obj.husband = Person.people[person["husband"]]

    return object_list
