#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
from io import StringIO
try:
    from universal.harness import *
except:
    sys.path.append("../../universal/")
    from harness import *

# Grading test suite starts here

script = grading_import("task", "script")

class GradingTests(AccessTestCase):

    def safe_function_call(self, obj, method_name, *args, **kwargs):
        try:
            return getattr(obj, method_name)(*args, **kwargs)
        except NameError:
            self.hint(f"It seems like you forgot to use the 'self.' keyword in your {obj.__class__.__name__}.{method_name}() method.")
            self.fail()
        except Exception as e:
            self.hint(f"Tried to call {obj.__class__.__name__}.{method_name}(), but your implementation crashed: {type(e).__name__} - {e}")
            self.fail()

    def safe_instantiation(self, cls_name, *args):
        try:
            cls = getattr(script, cls_name)
            return cls(*args)
        except AttributeError:
            self.hint(f"Could not find a class named '{cls_name}' in your code.")
            self.fail()
        except TypeError:
            self.hint(f"Make sure your {cls_name} class __init__ method accepts the 'name' parameter and matches the superclass signature.")
            self.fail()
        except Exception as e:
            self.hint(f"Check that your {cls_name} class is defined correctly and that __init__ is implemented properly.")
            self.fail()

    @weight(0) 
    def test_make_sound_print_instead_of_return_check(self):
        capture = StringIO()
        sys.stdout = capture

        objects = [self.safe_instantiation("Cat", "Garfield"), self.safe_instantiation("Dog", "Charlie")]

        for object in objects:
            return_val = self.safe_function_call(object, "make_sound")
            sys.stdout = sys.__stdout__
            output = capture.getvalue().strip()

            self.hint(f"Your {object.__class__.__name__}'s make_sound function should return a string, not print it.")
            self.assertFalse(return_val is None and output != "")

        

    def test_cat_correct_init(self):
        called = {"super_called": False}
        original_init = script.Pet.__init__

        # in order to trace if students call super()__init__
        def patched_init(self, name): 
            called["super_called"] = True
            original_init(self, name)

        script.Pet.__init__ = patched_init

        d = self.safe_instantiation("Cat", "Garfield")

        self.hint("Your Cat.__init__ method should call super().__init__(name) to properly initialize the parent class 'Pet'.")
        self.assertTrue(called["super_called"])

        self.hint("A Cat('Garfield') instance should have an attribute 'name' equal to 'Garfield'")
        self.assertEqual(d.name, "Garfield")

        script.Pet.__init__ = original_init

    def test_pet_make_sound_default_not_changed(self):
        p = self.safe_instantiation("Pet", "Speedy")
        actual = self.safe_function_call(p, "make_sound")
        self.hint("Seems like you changed the default value of the 'make_sound' method in the Pet class. Make sure you don't change the default value in the Pet class.")
        self.assertIn("something.", actual)

    def test_dog_make_sound_polymorphism(self):
        d = self.safe_instantiation("Dog", "Charlie")
        actual = self.safe_function_call(d, "make_sound")
        self.hint(f"The return value of {d.__class__.__name__}.make_sound() should not be None")
        self.assertIsNotNone(actual)

        self.hint(f"The return value of {d.__class__.__name__}.make_sound() should contain 'wuf', but returned '{actual}' instead.")
        self.assertIn("wuf", actual)

    def test_cat_make_sound_polymorphism(self):
        c = self.safe_instantiation("Cat", "Garfield")
        actual = self.safe_function_call(c, "make_sound")
        self.hint(f"The return value of {c.__class__.__name__}.make_sound() should contain 'miau', but returned '{actual}' instead.")
        self.assertIn("miau", actual)


TestRunner().run(AccessTestSuite(1, [GradingTests]))
