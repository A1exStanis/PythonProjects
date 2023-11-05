# 1. Create add method to add two countries together. This method should create another country object with the name of the two countries combined and the population of the two countries added together.

# ```

# bosnia = Country('Bosnia', 10_000_000)

# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia.add(herzegovina)

# bosnia_herzegovina.population -> 15_000_000

# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self,name:str,population:int):
        self.name = name
        self.population = population
    def add(self,value):
        name = self.name + " " + value.name
        population = self.population + value.population
        return Country(name,population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.population)


# 2. Implement the previous method with a magic method

# ```

# bosnia = Country('Bosnia', 10_000_000)

# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia + herzegovina

# bosnia_herzegovina.population -> 15_000_000

# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self,name:str,population:int):
        self.name = name
        self.population = population
    def __add__(self,other):
        name = self.name + " " + other.name
        population = self.population + other.population
        return Country(name,population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.name)


# 3. Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate, brake and display_speed. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. 
# Remember that the speed cannot be negative.

class Car:
    def __init__(self,brand,model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        speed = self.speed + 5
        return Car(self.brand,self.model,self.year,speed)
    
    def brake(self):
        if self.speed >= 5:
            speed = self.speed - 5
        else:
            speed = 0
        return Car(self.brand,self.model,self.year,speed)
    
    def display_speed(self):
        print(f"{self.brand} {self.model} has speed {self.speed}")

ferrari  = Car("Ferrari","458 Italia",2014,20)
porsche = Car("Porsche","918",2015,310)
ferrari = ferrari.accelerate()
porsche = porsche.brake()

ferrari.display_speed()
porsche.display_speed()