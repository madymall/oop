class Car:

    def __init__(self, title, model, color, max_speed, speed):
        
        self.title = title
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.speed = speed

    """поведение - Method (def)"""

    def start_engine(self):
        print(f"On {self.title} {self.model} engine started!")

    def gas(self):
        if self._currentSpeed >= self.max_speed:
            print('cvheck on!')
        else:
            self._currentSpeed += self.speed
            print(f'On {self.title} self.model} self._currentSpeed)


"""Instance"""

bmw = Car('BMW', 'e38', 'blue', 360, 20)
bmw.start_engine()

mercedes = Car('Mercedes', 'w220', 'black', 340, 10)
mercedes.start_engine()
# print(
#     f"Title: {bmw.title}\nModel: {bmw.model}\nColor: {bmw.color}"
# )