from modelos.carro import Carro
import os

class Interface: 


    def imprime_titulo_app():
        print('''

  ░█▀▄▀█ ░█▀▀▀█ 　 ░█──░█ █▀▀ █── █──█ █▀▀█ 　 ░█▀▀█ █▀▀█ █▀▀█ █▀▀ 
 ░█░█░█ ░█──░█ 　 ─░█░█─ █▀▀ █── █▀▀█ █──█ 　 ░█─── █▄▄█ █▄▄▀ ▀▀█ 
░█──░█ ░█▄▄▄█ 　 ──▀▄▀─ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ░█▄▄█ ▀──▀ ▀─▀▀ ▀▀▀ | 
   
 ''')
    
    @staticmethod
    def apresentar_menu_principal():
        Interface.imprime_titulo_app()
        print('''

    Menu Principal
1.Cadastrar um novo carro
2.Listar todos os carros cadastrado
3.Sair
              ''')
        Interface.ler_opcao_usuario()

    @staticmethod
    def imprime_titulo_tela(titulo):
        os.system('cls')
        Interface.imprime_titulo_app
        print(f'{str(titulo).upper()}')
        print('*' * 20)
        print()
        
    def cadastrar_carro():
        Interface.imprime_titulo_tela('cadastrando novo carro e modelo...')
        modelo = input('Modelo do carro:')
        ano = int(input('Ano de Fabricação: '))
        placa = input('Placa do veículo (opcional): ')
        marca = input ('Marca ou Fabricante  (opcional): ')
        cor = input ('Cor original  (opcional): ')

        carro = Carro(modelo, ano,placa, marca, cor)

        print(f'O carro foi cadastro: \n{carro}')
        
    def ler_opcao_usuario():
        try:
         opcao = int(input('Digite sua opção:'))

         if opcao == 1:
            Interface.cadastrar_carro()
         elif opcao == 2:
            Interface.imprime_titulo_tela('listando carros')
            Carro.listar_carros()
         elif opcao == 3:
            print ('Encerrando o programa')
            exit()
         else:
            print ('ERRADO, escolha entre 1, 2 e 3')
            Interface.voltar_ao_menu_principal()
        except ValueError:
            print ('ERRADO, escolha entre 1, 2 e 3')

        Interface.voltar_ao_menu_principal()

        
    @staticmethod
    def voltar_ao_menu_principal():
        print()
        input('Pressione ENTER para voltar ao menu principal')
        os.system('cls')
        Interface.apresentar_menu_principal()