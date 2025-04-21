#Activity 1
class car:
     def __init__(self, make, model, year, color, top_speed):
         self.make = make
         self.model = model
         self.year = year
         self.color = color
         self.top_speed = top_speed

     def display_info(self):
         return f"Car make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}"

     def drive(self):
        return f"The {self.make} {self.model} is driving at {self.top_speed} km/h!"

     def __str__(self):
        return f"{self.year} {self.make} {self.model} (Top Speed: {self.top_speed} km/h)"
     



class ElectricCar(car):
    def __init__(self, make, model, year, top_speed, battery_range):
        super().__init__(make, model, year, top_speed, battery_range)
        self.battery_range = battery_range 

    def drive(self):
        return f"{self.make} {self.model} zooms silently with a range of {self.battery_range} km! at a {self.top_speed} km/h!"

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (Electric, Range: {self.battery_range} km)"


#car1 = car("Toyota", "Corolla", 2009, "Red", 185)
#print(car1.display_info())
#print(car1.drive())
#print(car1.__str__())


#car2 = ElectricCar("Tesla", "Model S", 2025, 200, 1000 )
#print(car2.drive())  
#print(car2.__str__()) 


         