class vehicle():
    def __init__(self,mark: str,model:str):
        self.mark = mark
        self.model = model
    def fuel_type(self):
        fuel_type = fuel_type.upper()
        if ('GASOLINE'!= fuel_type and 'DIESEL' != fuel_type and 'ALCOHOL' != fuel_type):
            print(fuel_type)
        else:
            print('Unkonw value')

    
    def passangers_capacity(self, passengers: int):
        if passengers < 0:
            print('Its not a vehicle')
        else:
            print(f'Will bord {passengers} passengers')

test= vehicle('toyota','supra')
test.fuel_type('gasoline')
test.passangers_capacity(1)

# conta = vehicle('toyota','supra')
# conta.gas_type()