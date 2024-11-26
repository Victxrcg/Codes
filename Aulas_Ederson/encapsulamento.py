class encapsulamento():
    def __init__(self,num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def adicionar(self):
        return self.__num1 + self.__num2

cal = encapsulamento(20,30)
print(cal.adicionar())

