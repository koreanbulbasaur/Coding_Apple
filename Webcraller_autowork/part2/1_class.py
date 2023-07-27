class Hero:
    def __init__(self):
        self.q = 'eat'
        self.w = 'snow'

class Hero_another:
    def __init__(self, hole):
        self.q = 'eat'
        self.w = 'snow'
        self.e = hole

    def hello(self):
        self.r = 'Oh! Hi!'
        print(self.r)

nunnun = Hero()
garden = Hero()
print(nunnun.q)
print(garden.w)

tery = Hero_another('soul')
print(tery.e)

ruru = Hero_another('cat')
ruru.hello()