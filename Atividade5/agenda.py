#4) Criar um sistema de Agenda com POO;

class Pessoas:
    def __init__(self, nome, sobrenome, num, endereço):
        self.nome = nome
        self.sobrenome = sobrenome
        self.num = num
        self.endereço = endereço


        #Parte 2 do código

from agenda import Pessoas

p1 = Pessoas('Eliedson', 'de Souza', 999999999, 'Rua Aberta')
p2 = Pessoas('José', 'da Silva', 912345678, 'Rua Aquela')
p3 = Pessoas('Leonardo', 'da Silva', 914725836, 'Rua Lá')
p4 = Pessoas('Germain', 'Shuantz', 963852741, 'Rua da Felicidade')
p5 = Pessoas('Artur', 'Miuler', 978451623, 'Rua Já Vai')

lista_pessoas = [p1, p2, p3, p4, p5]

print(p1)
