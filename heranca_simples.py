class Veiculo:
    def __init__(self, cor,placa,numero_rodas):
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")



class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    # def esta_carregado(self, valor_carga):
        # self.valor_carga = valor_carga

        # if valor_carga <= 300:
        #     print("Não estou carregado") Feito por mim
        # else:
        #     print("Limite de carga exedido")
        def __init__(self, cor,placa,numero_rodas,carregado):
            super().__init__(cor, placa, numero_rodas)
            self.carregado = carregado
        
        def esta_carregado(self):
            print (f"{"Sim" if self.carregado else "Nao"} estou carregado")



moto = Motocicleta("preta", "bca-3214", 2)
# moto.ligar_motor()

carro= Carro("prata","bca-3214", 4)
# carro.ligar_motor()

caminhao = Caminhao("vermelho","bca-3214", 8, False)
# caminhao.ligar_motor()
# caminhao.esta_carregado()

print (caminhao)
