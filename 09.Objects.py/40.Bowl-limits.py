"""
 In this exercise, I want you to define a class attribute that will function like a constant, ensuring that we don’t need to hardcode any values in our class.
 What’s the task here? Well, you might have noticed a flaw in our Bowl class, one
that children undoubtedly love and their parents undoubtedly hate: you can put as
many Scoop objects in a bowl as you like.
"""

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():

    size = 1

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            if len(self.scoops) < Bowl.size:
                self.scoops.append(scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)