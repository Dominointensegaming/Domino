class PecaDomino:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        
    def __repr__(self):
        return(f"{self.lado1} | {self.lado2}")
    
    def combinar(self, outro_lado):
        return self.lado1 == outro_lado or self.lado2 == outro_lado
    
    def invert(self):
        self.lado1, self.lado2 = self.lado2, self.lado1 
        
    
class Coelho:
    def __init__(self, nome, idade, cor, raça):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raça = raça
        
    def pula(self):
        return f"{Coelho.nome} pulou"
    
    def come(self, comida):
        return f"{self.nome} está comendo {comida}"

OMeuCoelho = Coelho(nome="Teco", idade=8, cor="preto", raça="Vira Latas")

print(OMeuCoelho)
print(OMeuCoelho.pula)
print(OMeuCoelho.come("couve"))