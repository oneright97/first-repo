class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name) # 클래스 변수로 접근할 순 없다.

p2.ssafy = 11
print(p2.ssafy)