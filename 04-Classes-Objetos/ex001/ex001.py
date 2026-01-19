# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Construtor
        self.nome = "" # Atributos de instância
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria" #Sem parênteses é atributo
g1.idade = 17
g1.aniversario() #Com parênteses é metodo
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.aniversario()
#print(g3.aniversario())
