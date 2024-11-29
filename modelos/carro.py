class Carro:
 
    lista_de_carros = []
 
    numero_rodas = 4
 
    # No JavaScript: constructor() {}
    def __init__(
        self, modelo, ano, placa="não informado", marca="não informada", cor="Branco"):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.marca = marca
        self.cor = cor
        Carro.lista_de_carros.append(self)
   
    @classmethod
    def listar_carros(cls):
        print(f'{'Modelo'.ljust(20)} | {'Ano'.ljust(10)} | {'Placa'.ljust(10)} | {'Marca'.ljust(20)} | {'Cor'.ljust(20)}')
        for carro in Carro.lista_de_carros:
            print(f"{str(carro.modelo).ljust(20)} | {str(carro.ano).ljust(10)} | {str(carro.placa).ljust(10)} | {str(carro.marca).ljust(20)} | {str(carro.cor).ljust(20)}")
 
    def __str__(self):
        return f'{'Modelo'.ljust(20)} | {'Ano'.ljust(10)} | {'Placa'.ljust(10)} | {'Marca'.ljust(20)} | {'Cor'.ljust(20)} \n{str(self.modelo).ljust(20)} | {str(self.ano).ljust(10)} | {str(self.placa).ljust(10)} | {str(self.marca).ljust(20)} | {str(self.cor).ljust(20)}'
 
 
 