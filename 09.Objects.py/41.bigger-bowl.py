class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max = 3

    def __init__(self, *new):
        self.scoops = []

    def add_scoops(self, *new):
        for scoop in new:
            if len(self.scoops) < self.max:
                self.scoops.append(scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

class Super(Bowl):
    max = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
bb = Super()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
print(bb)