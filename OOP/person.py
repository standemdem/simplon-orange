class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    def __repr__(self):
        return f'[Person: {self.name, self.pay}]'

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus = .10):
        # bad way to implement a new giveRaise method because it duplicates the code
        # self.pay = int(self.pay * (1 + percent + bonus))
        # good way
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    #self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('---All three---')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10) #exemple of polymorphism, python select the right method for each obj
        print(obj)