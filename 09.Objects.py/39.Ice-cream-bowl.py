"""
 In this exercise, we’re going to see a small-scale version of that. In the previous
exercise, we created a Scoop class that represents one scoop of ice cream. If we’re
really going to model the real world, though, we should have another object into
which we can put the scoops. I thus want you to create a Bowl class, representing a
bowl into which we can put our ice cream (figure 9.7); for example
"""

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
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