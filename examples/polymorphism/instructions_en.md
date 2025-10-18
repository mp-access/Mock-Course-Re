Remember the `Pet` and `Dog` implementation from the previous example:

```python
class Pet:
    def __init__(self, name):
        self.name = name

    def sleep(self,hours):
        return (f"{self.name} will sleep for {hours} hours.")


class Dog(Pet):
    
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return "wuf"
```

In this exercise we want to use **polymorphism** instead of having specific `bark` function. Each pet should therefore have a `make_sound` method that can be overwritten by **subclasses**. The default implementation of `make_sound` in `Pet` is already implemented.

You should:
- Overwrite the class `make_sound` in the `Dog` class which should return `f"{name} says: wuf!"`
- Add a `Cat` class that inherits from Pet and overwrites `make_sound` to return `f"{name} says: miau!"`