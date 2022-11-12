#Monte um sistema com cadastro para:
	#Alunos;
  #Professores;
	#Cursos;
#Utilize conjuntos e orientação a objeto.

class Alunos:
    def __init__(self, documento, nome, matricula, curso):
        self.documento = documento
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

class Professores:
    def __init__(self, nome, disciplina, siape, curso):
        self.nome = nome
        self.disciplina = disciplina
        self.siape = siape
        self.curso = curso


        #Parte 2 do código

from sistema import Alunos, Curso, Professores

ads = Curso("Análise e Dev de Sistemas", "Matinal")
agronomia = Curso("Agronomia", "Integral")
biologia = Curso ("Lic. Ciências Biológicas", "Matinal")

aluno_jorge = Alunos("02376589145", "Jorge", "01", ads)
aluno_joao = Alunos("34578912345", "João", "02", agronomia)
aluno_jose = Alunos("56734512345", "José", "03", biologia)

prof_luis = Professores("Luis", "Lógica de Programação", "01", ads)
prof_gabriel = Professores("Gabriel", "Solos", "02", agronomia)
prof_matheus = Professores("Matheus", "Células", "03", biologia)

print(aluno_jorge.curso.periodo)
