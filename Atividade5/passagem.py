#1) Crie um sistema para criação de pacotes de viagem onde você pedirá o nome de quem irá viajar, mostrar as opções e printar a que foi escolhida.

class Viagem: 
    def __init__(self, pacote):
        self.pacote = pacote



#Parte 2 do código

from passagem import Viagem

viagem_0 = Viagem("Afeganistão")
viagem_1 = Viagem("Vista Alegre do Prata")
viagem_2 = Viagem("Mundial do LOL 2022")
viagem_3 = Viagem("England")
viagem_4 = Viagem("Grécia")
viagem_5 = Viagem("Meu coração")

print("Bem-vindo(a)!\nTemos ofertas de pacotes para você conhecer o mundo inteiro!! \n")
cliente = input("Digite seu nome para começarmos com a compra: ")
print(cliente,", temos 6 opções de viagens para você, escolha sua opção e aproveite!!\n [0] - Afeganistão\n [1] - Vista Alegre do Prata\n [2] - Mundial do LOL 2022\n [3] - England\n [4] - Grécia\n [5] - Meu coração")

selecao = int(input("Selecione o número do pacote para começarmos:"))

lista_passagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4, viagem_5]

opcao_sel = int(selecao)

for opcao in lista_passagem:
    if opcao_sel >= 6:
        print("\nNão foi possível completar a operação, tente novamente..")
        break
    if opcao_sel <= 5:
        print(cliente,"seu pacote escolhido foi ", lista_passagem[opcao_sel].pacote)
        print("Operação realizada com sucesso, volte sempre!!!")
        break
