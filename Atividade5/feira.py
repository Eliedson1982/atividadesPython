#3) Criar um sistema de Feirinha (Vendas):
    #Printar uma lista com as frutas;
    #Pedir para quem está comprando inserir o nome;
    #Após isso, pedir para selecionar a fruta;
    #Após isso imprimir o nome do solicitante e a fruta.

class Feira:
    def __init__(self, fruta):
        self.fruta = fruta



        #Parte 2 do código

from feira import Feira

fruta_0 = Feira("Banana")
fruta_1 = Feira("Maçã")
fruta_2 = Feira("Melancia")
fruta_3 = Feira("Abacate")
fruta_4 = Feira("Mamão")
fruta_5 = Feira("Bergamota")

print("Bem-Vindo(a) à Frutinhax a Feira de frutas com menos frutas no Brasil!!\n")
comprador = input("Digite seu nome para podermos botar na notinha após a compra: ")

carrinho = []

i = 1
while i > 0:

    print(comprador,", esse é nosso catálogo de frutas, tem poucas, mas são saborosas:\n [0] - Banana\n [1] - Maçã\n [2] - Melancia\n [3] - Abacate\n [4] - Mamão\n [5] - Bergamota\n [9] - Sair")

    selecao = int(input("Insira as frutas que queira comprar: "))

    lista_frutas = [fruta_0, fruta_1, fruta_2, fruta_3, fruta_4, fruta_5]

    opcao_sel = int(selecao)

    if opcao_sel == 9:
        print("Você escolheu sair, volte sempre!!\n")
        print("Aqui está sua lista de compras:\n")
        print(carrinho)
        i == 0
        break

    elif opcao_sel >= 6:
        print("Desculpa, não temos essa opção de fruta, leia a mensagem inicial de novo e depois repita o processo..")


    elif opcao_sel <= 5:
        print(comprador,", sua fruta", lista_frutas[opcao_sel].fruta, "foi adicionada ao carrinho com sucesso!")
        nome_fruta = lista_frutas[opcao_sel].fruta
        carrinho.append(nome_fruta)
        continue
