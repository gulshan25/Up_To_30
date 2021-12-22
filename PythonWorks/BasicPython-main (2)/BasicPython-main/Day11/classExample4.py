"""
class baseClass:
    pass

class derivedClass(baseClass):
    pass
"""

# Parent class
class Bird:
    def __init__(self) -> None:
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')

    def swim(self):
        print('Swim faster')

class Penguin(Bird):
    def __init__(self) -> None:
        super().__init__()
        print('Penguine is ready')

    def whoisThis(self):
        print('Penguin')
    
    def run(self):
        print('Run faster')

p = Penguin()
p.whoisThis()
p.swim()
p.run()