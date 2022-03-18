class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance, number):
        super().__init__(first_name, last_name, phone_number, balance)
        self.number = number 

    def transaction(self):
        print(f"Jack's balance: {jack.balance - self.number}\nVito's balance: {vito.balance + self.number}")

jack = Jack('Jack', 'White','1234567', 2000)
vito = Vito('Vito', 'Smith', '7654321', 1500, 500)
vito.transaction()
