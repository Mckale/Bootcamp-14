class Animal:

    def __init__(self):
        self.type="none"
        self.fodder="Two bales"
        self.milk="20lts"
        self.value="$40"

    def eat_schedule(x):
        if x==8:
            print("Time to eat")
        elif x==3:
            print("Time to eat")
            
    def drink_schedule(x):
        if x==10:
            print("Time to drink water")
        elif x==2:
            print("Time to drink water")

    def milk_schedule(x):
        if x==7:
            print("Time to milk")
        elif x==6:
            print("Time to milk")
        
class Cow(Animal):
    def __init__(self):
        self.type="Type: Cow"
        self.fodder="Fodder: Two bales"
        self.milk="Milk(lts): 20lts"
        self.value="Price$1.5 per liter"
pass


class Goat(Animal):
    def __init__(self):
        self.type="Type: Goat"
        self.fodder="Fodder: Two bales"
        self.milk="Milk(lts): 20lts"
        self.value="Price$1.5 per liter"
pass


animal=Animal()

print(animal.type)
print(animal.fodder)
print(animal.milk)
print(animal.value)

goat=Goat()

print(goat.type)
print(goat.fodder)
print(goat.milk)
print(goat.value)

cow=Cow()

print(cow.type)
print(cow.fodder)
print(cow.milk)
print(cow.value)

