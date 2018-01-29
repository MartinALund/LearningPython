class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def print_person(self):
        print("Personen hedder {}, er {} år gammel og har en højde på {}".format(self.name, self.age, self.height))

