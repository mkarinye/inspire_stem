# this is a class that describes cars

class car : 
    def __init___(self,model,make,year_of_production,fuel_capacity,colour,horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power = horse_power

    def print_make(self,make):
        print(" The car is of {0} make" .format(self.make))

    def set_make(self,make):
        self.make = make

    def get_make(self):
        return self.make        

friends_car = car("Impalla","chrevolet","1969","2500 cc","lalic","390 Hp") 

my_car = car("Jaguar","Audi","1974","3500 cc","green","500 Hp") 
my_car.print_make("Audi")

my_car.set_make("Audi")
friends_car.set_make("NIssan")

print(my_car.get_make())
print(friends_car.get_make())

my_car.set_make("Audi")
friends_car.set_make("NIssan")


    