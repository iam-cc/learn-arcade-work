class Dog():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("My name is" + self.name)

d1 = dog()
d1.name = "LEO"
d1.color = "Brown"
d1.weight = 30

d2 = dog()
d2.name = "Cookie"
d2.color = "Black"
d2.weight = 40

d1.introduce_self()
d2.introduce_sefl()


