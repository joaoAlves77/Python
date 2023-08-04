'''
Crie um programa que defina a classe "Aluno"
com um construtor que recebe três parâmetros,
o nome, a idade e a nota do aluno.
O programa deve criar duas instancias da classe
"Aluno", "a1" e "a2", com diferentes valores para
os parâmetros nome, idade e nota.
Em seguida, o programa deve imprimir o nome,
a idade e a nota de cada um dos alunos criados.
E por último, calcular e imprimir a media das 
notas dos dois alunos criados.
'''
class Aluno:
    def __init__(self, nome, idade, nota_aluno):
        self.nome = nome
        self.idade = idade
        self.nota_aluno = nota_aluno

print("Aluno 1")
a1 = Aluno("jão", 18, 10)
print(f'aluno: {a1.nome}\nidade: {a1.idade}\nnota: {a1.nota_aluno}')

print("\nAluno 2")
a2 = Aluno('maria', 19, 9)
print(f"aluno: {a2.nome}\nidade: {a2.idade}\nnota: {a2.nota_aluno}")

media = (a1.nota_aluno + a2.nota_aluno) / 2
print("\nmedia dos alunos é:", media)