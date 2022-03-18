class Dog:
    
    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.animal}: {self.voiceText}')

dog = Dog('Dog', 'Bow-Vow')
dog.voice()


class Cat:

    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.animal}: {self.voiceText}')

cat = Cat('Cat', 'Meow')
cat.voice()
    

class Cow:

    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.animal}: {self.voiceText}')

cow = Cow('Cow', 'Moo-Moo')
cow.voice()
    

class Bear:

    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.animal}: {self.voiceText}')

bear = Bear('Bear', 'Gr-Gr')
bear.voice()
