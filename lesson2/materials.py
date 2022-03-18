class Material:

    def__init__(self, type, strength, flammability)
    self.type = type
    self.strength = strength
    self.flammability = flammability

    def information(self):
        print(f'Material: {self.type}, strength: {self.strength}, flammability: {self.flammability}')

class Wood(Material):
    def __init__(self, type, strength, flammability, color):
        super.__init__(type, strength, flammability)
        self.color = color

wood = Wood('wood', 'medium', 'high', 'brown')


def information(self):
    print(f'Material: {self.type}, strength: {self.strength}, flammability: {self.flammability}, ')


class Glass(Material):
    def __init__(self, type, strength, flammability, color):
        super.__init__(type, strength, flammability)
        self.color = color
class Plastic(Material):
    def __init__(self, type, strength, flammability, color):
        super.__init__(type, strength, flammability)
        self.color = color

class Metal(Material):
    def __init__(self, type, strength, flammability, color):
        super.__init__(type, strength, flammability)
        self.color = color

class Stone(Material):
    def __init__(self, type, strength, flammability, color):
        super.__init__(type, strength, flammability)
        self.color = color

class Table(Wood):
    def __init__(self, type, strength, flammability, color, cost ):
        super.__init__(type, strength, flammability, color)
        self.color = color
        self.cost = cost

class Cup(Glass):
    def __init__(self, type, strength, flammability, color, cost ):
        super.__init__(type, strength, flammability, color)
        self.color = color
        self.cost = cost

class Bottle(Plastic):
    def __init__(self, type, strength, flammability, color, cost ):
        super.__init__(type, strength, flammability, color)
        self.color = color
        self.cost = cost

class Pipe(Metal):
    def __init__(self, type, strength, flammability, color, cost ):
        super.__init__(type, strength, flammability, color)
        self.color = color
        self.cost = cost

class Statue(Stone):
    def __init__(self, type, strength, flammability, color, cost ):
        super.__init__(type, strength, flammability, color)
        self.color = color
        self.cost = cost