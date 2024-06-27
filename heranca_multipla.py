class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}"for chave, valor in self.__dict__.items()])}"
    


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    


class Gato(Mamifero):
    pass


class Ornintorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        print(Ornintorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

# gato = Gato(4, "Branco")
# print (gato)

ornintorrinco = Ornintorrinco(numero_patas=4, cor_pelo="vermelho", cor_bico="azul")
print (ornintorrinco)