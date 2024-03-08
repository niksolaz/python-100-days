from module_2 import Person

person = Person("John", 30)

def print_person(person) :
    print(person.get_name())
    print(person.get_age())
    print(person.__str__())

def set_person(person, name, age) :
    person.set_name(name)
    person.set_age(age)
    print_person(person)
