import abstract

class Car(abstract.AbstractTransport):

    def __init__(self, title, model, color):
        super().__init__(title, model, color)

class Airplane(abstract.AbstractTransport):

    def __init__(self, title, model, color, speed):
        super().__init__(title, model, color)
        self.speed = speed
