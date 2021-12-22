from classExample5 import Person, Student

std = Student(2, 'SID', 22, 2200)
print(std.show())

p = Person(5, 'Tahmid', 20)
print(p)
print(p.show()) # this done by __str__ func