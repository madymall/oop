class Animal:

    def __init__(self, name, type, color, voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)

class Dog(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)

class Cat(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)


rex = Dog('Rex', 'Domestic', 'Blue', 'gaf gaf!')
rex.voice()

barsik = Cat('Barsic', 'Domastic', 'White-Black', 'Meow-Meow')
barsik.voice()

#polimorfism

class Horse(Animal):

    def __init__(self, name, type, color, voiceText, speed, weight):
        super().__init__(name, type, color, voiceText)
        self.speed = speed
        self.weight = weight

    def voice(self):
        print(f'{self.name}: {self.voiceText}')

mustang = Horse('Mustang', 'Domestic', 'brown', 'kukareku', 30, 250)
mustang.voice()

"""Incapsulation"""

