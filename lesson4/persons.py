from lesson4.db import db
from package import models, config


if config.staging:

    persons = []

    for person in config.fake_db:
        persons.append(
            models.Person(person['username'], person['salary']).info()
        )

        print(persons)

else:

    while True:

        username = input('Username: ')
        salary = int(input('Salary: '))

        person = models.Person(username, salary)
        db.append(person)

        print(person.info())
