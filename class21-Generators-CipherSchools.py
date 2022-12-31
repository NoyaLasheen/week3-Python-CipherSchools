# Generators

def generate_squares(n):
    return [i**2 for i in range(1,n)]

for x in generate_squares(100):
    print(x)

    '''a = []
    for i in range(1,100):
        a.append(i**2)

    for x in a:
        print(x)'''

# Lazy loading
def generate_squares(n):
    for i in range(1,n):
        yield(i**2)

for i in generate_squares(1):
    print(i)


print('Hello')
for i in range(10000000):
    pass
print("World")

from time import sleep
def func():
    print('Started')
    yield
    sleep(5)
    print("Ended")

func()

print('Hello')
it = iter(func())
next(it)
print("World")
next(it)