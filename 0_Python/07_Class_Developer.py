class Developer:
    def __init__(self, name, pay, title, zipcode):
        self.name = name
        self.pay = pay
        self.title = title
        self.zipcode = zipcode
    def lastName(self):
        return self.name.split()[-1]
    def firstName(self):
        return self.name.split()[0]
    def giveRise(self, percent):
        self.pay *= (1.0 + percent)

bob = Developer('Bob Smith', 120000, 'Engineer', 77001)
sue = Developer('Sue Jones', 130000, 'Manager', 77002)

print(bob.firstName(),'`s last name is',bob.lastName())
print(sue.firstName(), 'is the first name')
print(sue.firstName(),'`s ZIP code is',sue.zipcode)

sue.giveRise(.10)
print('Sue`s new pay:', sue.pay)

bob.giveRise(.15)
print('Bob`s new pay:', bob.pay)

space = "My Name is Ramil"
lspace = list(space)
print(lspace)

k = filter(None, lspace)

print(k)