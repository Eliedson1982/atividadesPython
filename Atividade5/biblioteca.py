#2) Faça um sistema bibliotecário:
    #Printar uma lista com 10 livros;
    #Pedir o nome de quem está solicitando;
    #Escolher o livro;
    #Printar o livro selecionado com o nome de quem solicitou.

class Biblioteca:
    def __init__(self, livro):
        self.livro = livro




        #Parte 2 do código

from biblioteca import Biblioteca

livro_0 = Biblioteca("Harry Potter 1")
livro_1 = Biblioteca("Harry Potter 2")
livro_2 = Biblioteca("Harry Potter 3")
livro_3 = Biblioteca("Harry Potter 4")
livro_4 = Biblioteca("Harry Potter 5")
livro_5 = Biblioteca("Harry Potter 6")
livro_6 = Biblioteca("Harry Potter 7")
livro_7 = Biblioteca("Harry Potter 8")
livro_8 = Biblioteca("Harry Potter 9")
livro_9 = Biblioteca("Harry Potter 10")

print("Seja bem-vindo(a) à biblioteca Liblioteca, onde você pode viajar por lugares incríveis e viver muitas aventuras com nossos livros!!\n")
cliente = input("Para começarmos com a retirada, por favor, insira seu nome: ")
print(cliente,", aqui está nossa lista de livro: \n [0] - Harry Potter 1\n [1] - Harry Potter 2\n [2] - Harry Potter 3\n [3] - Harry Potter 4\n [4] - Harry Potter 5\n [5] - Harry Potter 6\n [6] - Harry Potter 7\n [7] - Harry Potter 8\n [8] - Harry Potter 9\n [9] - Harry Potter 10")

selecao = int(input("Selecione o livro que você queira retirar: "))

lista_livros = [livro_0, livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9]

opcao_sel = int(selecao)

for opcao in lista_livros:
    if opcao_sel >= 10:
        print("Infelizmente não foi encontrado este exemplar, por favor, tente de novo..")
        break
    if opcao_sel <= 9:
        print(cliente,", seu livro ", lista_livros[opcao_sel].livro, "foi agendado com sucesso, esperamos a sua vinda para a entrega do livro.")
        print("Obrigado e volte sempre!!")
        break
