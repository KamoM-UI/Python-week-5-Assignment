#Assignment 2 

class vehicle:
    alive = False

class car(vehicle):
    def move(self):
        return "Driving!"
    
class plane(vehicle):
    def move(self):
        return "Flying!"
    
class boat(vehicle):
    def move(self):
        return "Sailing!"
    
class helicopter(vehicle):
    def move(self):
        return "Hovering!"

vehicles = [car(), plane(), boat(), helicopter()]
for v in vehicles:
    print(v.move())