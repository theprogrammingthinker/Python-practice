'''x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())'''

'''name = "This is a global name"


def greet():
    # Enclosing function
    name = 'Raihan'

    def hello():
        print("hello " + name)

    hello()


greet()

# Global
print(name)

# Built in
print(len(name))'''

'''
# Local Variables
x = 50
def func(x):
    print('x is ', x)
    x = 2
    print("changed local x to ", x)

func(x)
print('x is still ', x)
'''

x = 50
def func():
    global x
    print('this function is now using the global x!')
    print('because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to ', x)

print('Before calling func(), x is : ', x)
func()
print('value of x (outside of func()) is: ', x)