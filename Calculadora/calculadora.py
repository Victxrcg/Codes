from operacoes.soma import Soma
from operacoes.subtração import Subtracao
from operacoes.Multiplicação import Multiplicacao
from operacoes.Divisão import Divisao

class Calculadora:
    def __init__(self):
        self.operacoes = {
            "Soma": Soma(),
            "Subtração": Subtracao(),
            "Multiplicação": Multiplicacao(),
            "Divisão": Divisao()
        }

    def realizar_operacao(self, operacao, a, b):
        if operacao in self.operacoes:
            return self.operacoes[operacao].calcular(a, b)
        else:
            return "Operação inválida!"
