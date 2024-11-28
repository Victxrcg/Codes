class vehicle():
    def __init__(self,mark: str,model:str):
        self.mark = mark
        self.model = model

    def fuel_type(self):
        
        return 'Unkonw value'

    
    def passangers_capacity(self):
        return 0
        
class car(vehicle):

    def fuel_type(self):
        return 'Gasoline/Alcohol'
    
    def passangers_capacity(self):
        return 5
    
class motorcycle(vehicle):

    def fuel_type(self):
        return 'Gasoline'

    def passangers_capacity(self):
        return 2

class truck(vehicle):

    def fuel_type(self):
        return 'Diesel'
    
    def  passangers_capacity(self):
        return 2
    
def system():

    vehicle = [
        car('toyota','Supra'),
        motorcycle('Kawasaki','Ninja'),
        truck('Volvo','H1200'),
        ]
     
    for vehicle in vehicle:
        print(f'Mark: {vehicle.mark}')
        print(f'Model: {vehicle.model}')
        print(f'Fuel type: {vehicle.fuel_type()}')
        print(f'Passengers capacity: {vehicle.passangers_capacity()}')
        print('-' * 30)
        
        




if __name__ == "__main__":
    system()
