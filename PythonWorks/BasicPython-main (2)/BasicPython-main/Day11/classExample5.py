class Person:
    """
    A simple model of Person class
    """
    def __init__(self, id, name, age) -> None:
        self.id = id
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.age}'

    def walk(self):
        print(self.name, 'is now running')

    def show(self):
        s = f'ID = {self.id}\nName = {self.name}\nAge = {self.age}'
        return s

class Student(Person):
    def __init__(self, id, name, age, fees) -> None:
        super().__init__(id, name, age)
        self.fees = fees

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.age} {self.fees}'

    def show(self):
        s = f'ID = {self.id}\nName = {self.name}\nAge = {self.age}\nFees ={self.fees}'
        return s


# p = Person(1, 'Aziz Uddin', 30)
# print(p)
# p.walk()
# print(p.show())
