class Balance:

    amount = None

balance_1 = Balance()
balance_1.amount = 5000

class Person(Balance):
    frst_name = None
    last_name = None
    number = None

jack = Person()
jack.frst_name = "Jack"
jack.last_name = "Barbaro"
jack.number = '23456'
jack.amount = 5000

jack.amount = jack.amount + 40
print(jack.frst_name, jack.last_name, jack.number, jack.amount)


