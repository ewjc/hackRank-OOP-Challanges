OOP Challange!

Problem 1: --------------------------------------------------------------
def sleep(name):
    print('{name} sleeps for 8 hours').format(name=name)

Problem 2:--------------------------------------------------------------
def eat(name, food):
    print('{name} eats {food}').format(name=name, food=food)
    if food == favoriteFood:
        print('YUM! {name} wants more {food}').format(name=name, food=food)

Problem 3:--------------------------------------------------------------
class Tiger(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        name = self.name
        self.food = food
        favoriteFood = 'meat'
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)
    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        name = self.name
        print('{name} sleeps for 8 hours').format(name=name)

Problem 4:--------------------------------------------------------------
class Bear(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        name = self.name
        self.food = food
        favoriteFood = 'fish'
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} hibernates for 4 months').format(name=name)

Problem 5:--------------------------------------------------------------
class Animal(object):
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    def eat(self, food):
        name = self.name
        favoriteFood = self.favoriteFood
        self.food = food
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} sleeps for 8 hours').format(name=name)

# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")

    def sleep(self):
        name = self.name
        print('{name} hibernates for 4 months').format(name=name)

Problem 6:--------------------------------------------------------------
class Animal(object):
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    def eat(self, food):
        name = self.name
        favoriteFood = self.favoriteFood
        self.food = food
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} sleeps for 8 hours').format(name=name)

class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")

class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")

    def sleep(self):
        name = self.name
        print('{name} hibernates for 4 months').format(name=name)

class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "marshmallows")

    def sleep(self):
        name = self.name
        print('{name} sleeps in a cloud').format(name=name)

class Giraffe(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "leaves")

    def eat(self, food):
        name = self.name
        favoriteFood = self.favoriteFood
        self.food = food
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)
        elif food is not favoriteFood:
            print('YUCK! {name} spits out {food}').format(name=name, food=food)

class Bee(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "pollen")

    def eat(self, food):
        name = self.name
        favoriteFood = self.favoriteFood
        self.food = food
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)
        elif food is not favoriteFood:
            print('YUCK! {name} spits out {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} never sleeps').format(name=name)

Problem 7:--------------------------------------------------------------
# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        name = self.name
        self.animals = animals
        self.food = food
        print('{name} is feeding {food} to {number} animals').format(name=name, food=food, number=len(animals))
        for animal in range(0, len(animals)):
            animals[animal].eat(food)
            animals[animal].sleep()
        
Problem 8:--------------------------------------------------------------
