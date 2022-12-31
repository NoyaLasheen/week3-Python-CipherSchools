a=5
print(isinstance(a,object))
print(type(a))
print(isinstance(a,int))

class A:
    pass
print(type(A))

def func():
    pass
print(type(func))
print(isinstance(func,object))

class A:
    name = 'Noya'
    marks = 50

print(type(A))

A=5
print(type(A))

print(type(int))
print(type(object))

class A:
    def __call__(self):
        print('You called me')
class A:
    pass
b = A.__call__()
b = A()

def func1():
    print("Hello")

for i in range(5):
    print(i)

n = {'name': 'Jatin'}
print(n)
n.__getitem__("name")


class Exponent:
    def __init__(self,n) :
        self.n = n
    def __getitem__(self,x):
        return x**self.n

x=3
e = Exponent(3)
print(e)

class A:
    name = 'jatin'
    def __init__(self,n) :
        self.n=n
print(A.name)

a=A(2)
print(a.n)

class Dogs:
    kind= 'canine '
    def __init__(self,name):
        self.name=name
a = Dogs('Maxx')
print(a.name)
print(a.kind)


class Dog:
    tricks = []

    def __init__(self,name):
        self.name=name
    def add_trick(self,trick):
        self.tricks.append(trick)

d1 = Dog('Maxx')
d1.add_trick('Fetch')
d1.add_trick("Talk")
d1.tricks

d2 = Dog('Bella')
print(d2.tricks)




    





