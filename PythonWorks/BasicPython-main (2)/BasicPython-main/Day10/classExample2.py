"""
Polymorphism- is an ability
to use common interface for
multiple form.
Example - There are multiple
shape option (Rectangle, Squar, Circle)

"""
class Parrot:
    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print('Parrot can\'t swim')

class Penguin:
    def fly(self):
        print('Penguin can\'t fly')

    def swim(self):
        print('Penguin can swim')

def fly_test(obj):
    obj.fly()

def swim_test(obj):
    obj.swim()

tiya = Parrot()
peddy = Penguin()

fly_test(tiya)
fly_test(peddy)


