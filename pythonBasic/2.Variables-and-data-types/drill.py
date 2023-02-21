name = "Alan Turing"
age = 42
person = [name,age,"mathematician"]
""" text = f"Hello , my name is {name} "
print(text) """
text = "Hello, my name is {}, I am {} years old and I am a {}.".format(name, age, person[2])
print(text)
age_type = type(age)
print(age_type)

import unittest


class TestNotebook(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name, "Alan Turing")

    def test_age(self):
        self.assertEqual(age, 42)

    def test_person(self):
        self.assertEqual(person, ["Alan Turing", 42, "mathematician"])

    def test_text(self):
        self.assertEqual(
            text,
            "Hello, my name is Alan Turing, I am 42 years old and I am a mathematician.",
        )

    def test_type(self):
        self.assertEqual(age_type, int)


unittest.main(argv=[""], verbosity=2, exit=False)
     