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
    def dance(self):
        print(f'{self.name}正在跳舞')
    def sing(self):
        print(f'{self.name}正在唱歌')
