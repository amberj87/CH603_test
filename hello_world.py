from dosomething import double

def addition(a,b):
    c=a+b
    return c

def multiply(a,b):
    c=a*b
    return c

def test(a,b):
    c=2*a+b*b+5
    return c

print("hello world")
a=1.0
b=2.0
c=addition(a,b)
print(c)
c=multiply(a,b)
print(c)
print("testing test",test(2,3))
print(c)
print(double(5.0))
