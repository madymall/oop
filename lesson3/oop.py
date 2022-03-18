class Builder:

    def can_build(self):
        print("I can build")

class Doctor:

    def can_help(self):
        print("I can help!")

class Programmer:

    def can_write_code(self):
        print("I can write code on Python!")

    def can_build(self):
        print('I am programmer but I can build!')

class Person(Builder, Doctor, Programmer):
    pass

jack = Person()
# jack.can_write_code()
print(Person.__mro__)
jack.can_build()