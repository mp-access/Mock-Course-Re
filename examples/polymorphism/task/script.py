class Pet:
    def __init__(self, name):
        self.name = name

    def sleep(self,hours):
        return f"{self.name} will sleep for {hours} hours."

    def make_sound(self):
        return f"{self.name} says: animal_sound."

class Dog(Pet):
    
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        ...


class Cat(Pet):
    
    def __init__(self, name):
        ...