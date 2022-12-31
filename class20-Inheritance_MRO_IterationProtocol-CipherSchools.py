class A:
    def __init__(self) :
        print("A init executed")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init executed")

abc = B()
print(abc)
        
class A:
    pass
class B(A):
    x=5
class C(B):
    pass
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)

# DFS
# if there is a loop solve branches separately 

print(E.mro)

# Iteration protocol
'''
For any object to be an itrable, it should have 2 dunders
# __iter__
# __next__
'''

a = range(5)
it = a.__iter__()
print(it)
#ne = it.__next__()
it = iter(a)
print(next(it))
print(it.__next__())


class myrange:
    def __init__(self,n) :
        self.n = n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange) :
        self.myrange=myrange
        self.i = 0

    def __next__(self):
        ret = self.i
        self.i += 1

        if ret>= self.myrange.n:
            raise StopIteration
        return ret
    
a = myrange(5)
it = iter(a)
print(next(it))




a = 'python'
print(iter(a))