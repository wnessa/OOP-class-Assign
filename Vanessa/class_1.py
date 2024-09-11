# Class: Car
class Car:
    # Constructor method with attributes: make, model, year
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method: start_engine
    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine is now running."

    # Method: stop_engine
    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine is now off."
