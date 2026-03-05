class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print(f'{self.name}正在睡觉')
    def eat(self):
        print(f'{self.name}正在吃饭')
class uukong(Person):
       def song(self):
           print(f'{self.name}正在唱歌')

class hxy(Person):
    def __init__(self,name,age,love):
        super().__init__(name,age)
        self.love = love
    def dance(self):
        super().eat()
    def sing(self):
        super().sleep()
        print(f'{self.name}爱{self.love}')


u=uukong('uukong',20)
u.song()

h=hxy('hxy',20,'uukong')
h.dance()
h.sing()

