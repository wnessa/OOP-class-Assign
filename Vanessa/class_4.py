# Class: Dog
class Dog:
    # Constructor method with attributes: name, breed, age
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # Method: bark
    def bark(self):
        return f"{self.name} is barking."

    # Method: fetch
    def fetch(self, item):
        return f"{self.name} fetched the {item}