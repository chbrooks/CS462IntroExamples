
## a simple example of how classes and inheritance works in Python

class Mammal :
    "Documentation for the mammal class"
    ### Here's our constructor. Note the use of self.
    ### We use the default value for type to provide multiple constructors
    def __init__(self, type='') :
        self.type = type

    def sayName(self) :
        print('I am a ' + self.type) ## note the use of '+' for string concatenation

    ### this is a builtin method that controls how an object is printed
    ### return the string indicating how the object should be displayed
    def __repr__(self) :
        return self.type

class Flyer :
    "Class for things that can fly"
    def __init__(self, type='') :
        self.type=type
    def canFly(self) :
        return True

class Bird(Flyer) :
    def init(self, type='') :
        Flyer.__init__()    ## This is the equivalent of 'super()' in Java
        self.type = type
    def sayName(self) :
        print("I am a bird that is a " + self.type)

class Penguin(Bird) :
    def canFly(self) :
        return False

class Bat (Mammal, Flyer) :
    def __init__(self, type="bat") : ## note the default argument.
        self.type = type
    def sayName(self) :
        Mammal.sayName(self) ## First call the parent class' method, then continue.
        print("I am not a vampire, though")

if __name__ == '__main__':
    a1 = Mammal('cat')
    b1 = Bird("duck")
    c1 = Bat("bat")
    c2 = Bat()
    b1.sayName()
    c2.sayName()
