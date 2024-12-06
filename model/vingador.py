from model.database import Database
from datetime import datetime

class Vingador:
    
    CATEGORIAS_PERMITIDAS = ['Humano', 'Meta-humano', 'Androide', 'Deidade', 'Alienígena']
    lista_vingadores = []

    def __init__(self, id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, convocado=False, tornozeleira=False, chip_gps=False, prisao = False):
        self.id = id
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria.capitalize()
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self._convocado = convocado
        self._tornozeleira = tornozeleira
        self._chip_gps = chip_gps
        self.prisao = prisao
        self.lista_vingadores.append(self)

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        categoria = categoria.capitalize()
        if categoria not in self.CATEGORIAS_PERMITIDAS:
            print(f"Categoria '{categoria}' inválida.")
            self._categoria = self._solicitar_categoria_valida()
        else:
            self._categoria = categoria

    @property
    def tornozeleira(self):
        return 'Sim' if self._tornozeleira else 'Não'

    @tornozeleira.setter
    def tornozeleira(self, valor):
        self._tornozeleira = valor

    @property
    def chip_gps(self):
        return 'Sim' if self._chip_gps else 'Não'

    @chip_gps.setter
    def chip_gps(self, valor):
        self._chip_gps = valor

    @property
    def convocado(self):
        return 'Sim' if self._convocado else 'Não'
    
    @convocado.setter
    def convocado(self, valor):
        self._convocado = valor

    def _solicitar_categoria_valida(self):
        while True:
            categoria = input(f"Digite uma categoria válida ({', '.join(self.CATEGORIAS_PERMITIDAS)}): ").capitalize()
            if categoria in self.CATEGORIAS_PERMITIDAS:
                return categoria
            print(f"Categoria '{categoria}' inválida.")

    @classmethod
    def listar_vingadores(cls):
        print(f"{'Nome do Herói'.ljust(20)} |  {'Nome Real'.ljust(20)} |  {'Categoria'.ljust(15)} |  {'Tornozeleira'.ljust(15)} |  {'Rastreado'.ljust(15)}")
        print('-' * 95)
        for vingador in cls.lista_vingadores:
            print(vingador)

    def listar_detalhes_vingador(self):
        print()
        print(f"Vingador: {self.nome_heroi}")
        print(f"Nome Real: {self.nome_real}")
        print(f"Categoria: {self.categoria}")
        print(f"Poderes: {', '.join(self.poderes)}")
        print(f"Poder Principal: {self.poder_principal}")
        print(f"Fraquezas: {', '.join(self.fraquezas)}")
        print(f"Nível de Força: {self.nivel_forca}")
        print(f"Convocado: {self.convocado}")
        print(f"Tornozeleira: {self.tornozeleira}")
        print(f"Chip GPS: {self.chip_gps}")
        return None

    def __str__(self):
        return f'{self.nome_real.ljust(20)} |  {self.nome_heroi.ljust(20)} |  {self.categoria.ljust(15)} |  {self.tornozeleira.ljust(15)} |  {self.chip_gps.ljust(15)}'


    def convocar(self):
        self.convocado = True
        self.registrar_convocacao()
        return f'{self.nome_heroi} convocado!'
    def tornozelar(self):
        self.tornozeleira = True
        self.registrar_tornozeleira()
        return f'{self.nome_heroi} está com a tornozeleira!'
    def chipizar(self):
        self.chip_gps = True
        self.registrar_chip()
        return f'{self.nome_heroi} chipado!'
    def prender(self):
        self.prisao = True
        self.registrar_prisao()
        return f'{self.nome_heroi} preso!'

    def registrar_convocacao(self):
        try:
            db = Database()
            db.connect()

            data_convocacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            query = """
            INSERT INTO Convocacao (heroi_id, descricao, data_convocacao)
            VALUES (%s, %s, %s)
            """
            descricao = f"Convocação do herói {self.nome_heroi}"
            values = (self.id, descricao, data_convocacao)
            
            db.execute_query(query, values)
            print(f"Convocação de {self.nome_heroi} registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar a convocação: {e}")
        finally:
            db.disconnect()
    def registrar_chip(self):
        try:
            db = Database()
            db.connect()

            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            query = """
            INSERT INTO Gps (idheroi, nome_heroi, localizacao, data_hora)
            VALUES (%s, %s, %s, %s)
            """
            localizacao = {"Está na..."}  # Isso parece ser um exemplo, por favor, ajuste conforme necessário
            nome_heroi = f"{self.nome_heroi}"
            values = (self.id, nome_heroi, localizacao, data_hora)
            
            db.execute_query(query, values)
            print(f"Chip de {self.nome_heroi} registrado com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar o chip: {e}")
        finally:
            db.disconnect()

    
    def registrar_prisao(self):
        try:
            db = Database()
            db.connect()

            data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            query = """
            INSERT INTO Prisao (idheroi, motivo, data)
            VALUES (%s, %s, %s)
            """
            motivo = f"Prisão do herói {self.nome_heroi}"
            values = (self.id, motivo, data)
            
            db.execute_query(query, values)
            print(f"Prisão de {self.nome_heroi} registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar a prisão: {e}")
        finally:
            db.disconnect()


    def registrar_tornozeleira(self):
        try:
            db = Database()
            db.connect()

            data_torno = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            query = """
            INSERT INTO tornozeleira (idheroi, data_torno)
            VALUES (%s, %s)
            """
            values = (self.id, data_torno)
            
            db.execute_query(query, values)
            print(f"Tornozeleira de {self.nome_heroi} registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar a convocação: {e}")
        finally:
            db.disconnect()


    
    @staticmethod
    def carregar_herois():
        try:
            db = Database()
            db.connect()

            query = 'SELECT idheroi, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
            herois = db.select(query)  
            for heroi in herois:
                Vingador(*heroi)
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect()


    @staticmethod
    def listar_convocados():
        print(f"{'Nome do Herói'.ljust(20)} |  {'Nome Real'.ljust(20)} |  {'Categoria'.ljust(15)} |  {'Convocado'.ljust(15)}")
        print('-' * 80)
        for vingador in Vingador.lista_vingadores:
            if vingador.convocado == 'Sim':
                print(vingador)

    @staticmethod
    def listar_tornozeleirados():
        print(f"{'Nome do Herói'.ljust(20)} |  {'Nome Real'.ljust(20)} |  {'Categoria'.ljust(15)} |  {'Tornozeleira'.ljust(15)}")
        print('-' * 80)
        for vingador in Vingador.lista_vingadores:
            if vingador.tornozeleira == 'Sim':
                print(vingador)

    @staticmethod
    def listar_prisioneiros():
        print(f"{'Nome do Herói'.ljust(20)} |  {'Nome Real'.ljust(20)} |  {'Categoria'.ljust(15)} |  {'Prisioneiro'.ljust(15)}")
        print('-' * 80)
        for vingador in Vingador.lista_vingadores:
            if vingador.convocado == 'Sim' and vingador.tornozeleira == 'Sim':
                print(vingador)
