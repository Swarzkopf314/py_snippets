import sys



def define_class():
    x = 5

    class A(object):

        def ala(this):
            def bubson():
                print("lal")

            print(this)
            print(x)

        ala("nic")

    return A

A = define_class()

a = A()

a.ala()

A.ala("nic")

# a.

sys.exit()

class X(object):
    zuza = 314
    def __getattribute__(self, attr):
        print "Zuzia"
        return 12
        return object.__getattribute__(self, attr)

    print('lala')

    # pass
    # ala = ala

x = X()#.lala
x.lala
x.buba = 14
print x.buba
print x.zuza

def log(msg):
    print(msg)

def gen():
    yield 1
    yield 2

gen = gen()

print iter(gen) is gen.__iter__()
print iter(gen) is gen


def print_dict():
    for k in{"x": 1, "y": 2}:
        print(k)

for _ in range(1):
    print_dict()


sys.exit()

def gen_setter(cls, *names):

    def gen_f(name):
      def f(self, val):
        log(name)
        self.__dict__[name] = val
      return f

    for name in names:
        setattr(cls, 'set_' + name, gen_f(name))

class A(object):
    pass

# setattr(A, "buba", 3)
class B:
    gen_setter(A, "zuza", "arbuza")

a = A()
a.set_zuza("czy odpowie?")
a.set_arbuza(3)
print a.zuza
print a.arbuza

sys.exit()

class X(object):
    zuza = 314
    def __getattribute__(self, attr):
        print "Zuzia"
        return 12
        return object.__getattribute__(self, attr)

    # pass
    # ala = ala

x = X()#.lala
x.lala
x.buba = 14
print x.buba
print x.zuza

sys.exit()

class X:
    # @classmethod
    def ala(cls):
        return cls
x = X()

print(X.ala == X.ala)
print(X.ala is X.ala)
print(x.ala == x.ala)
print(x.ala is x.ala)

print x.ala
print X.ala

# sys.exit()


class Dog:
    def bark(self):
        print "Woof"

def new_bark(self):
    print "Woof Woof"

funcType = type(Dog.bark)

def wrap(f):
    print "lala"
    return f

Dog.bark = wrap(Dog.bark)

new_bark(3)

# sys.exit()

foo = Dog()

funcType = type(Dog.bark)

print funcType
# "Woof"
foo.bark()

print "foo.bark is foo.bark BEFORE"
print foo.bark is foo.bark

foo.bark = new_bark
print foo.bark

# replace bark with new_bark for this object only
foo.bark = funcType(new_bark, foo, Dog)

print "foo.bark is foo.bark"
print foo.bark is foo.bark

print foo.bark
foo.bark()
# "Woof Woof"

sys.exit()

def generate_f():
    def f():
        return f.x
    return f

f = generate_f()

f.x = 314
g = f

del f
print g()

sys.exit()

x = "lala" + "buba"

locals()[x] = 5

print(lalabuba)

sys.exit()

def ala(x, y = 2):
    return x+y

# print(ala 2, 3)
# sys.exit()
# print ala.im_class

class X:
    pass
    # ala = ala

X.ala = ala

x.ala = ala

class X:

    @class_method
    def ala():
        return 3
x = X()

print(X.ala == X.ala)
print(X.ala is X.ala)
print(x.ala == x.ala)
print(x.ala is x.ala)

# print X().ala(2,3)

# print X.ala(X(),3)

# assert X.ala is X.ala

sys.exit()

def buba(*args, **kwargs):
    print [x*x for x in args]#.append(y)
    return {val: name for name, val in kwargs.items()}

# def lala(**args, x=2):
    # print args.append(x)

# lala(1,2,3)

print buba(1,2,3, a = 3)
print buba(*[1,2])

sys.exit()

print ala(2,3)
print ala(2,y=4)
print ala(y=5,x=3)
print ala(5,x=3)


class A(object):
    # x = ""
    pass
    # def __init__(self):
        # self.x = 314
        # pass
    # ala_ma_kota = 2

o = A()
# o = object()

# o.__dict__['x'] = 314
o.x = 314

def print_x(self):
    print self.x

A.ala_ma_kota = print_x


o.ala_ma_kota()

# sys.exit()

if "        ":
    print "blank is True"
else:
    print "blank is False"
