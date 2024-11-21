# Trata objetos diferentes da mesma forma, já que ambas possuem a classe Base Veiculo
from heranca.script import Carro
from heranca.script01 import Moto

def teste_veiculo(veiculo):
    print(f"Teste com {veiculo.marca} {veiculo.modelo}:")
    veiculo.acelerar()
    veiculo.acelerar()
    veiculo.mostrar_velocidade()
    veiculo.frear()
    veiculo.mostrar_velocidade()

# Testando com uma instância de Carro
carro = Carro("Fiat", "Uno")
teste_veiculo(carro)

# Testando com uma instância de Moto
moto = Moto("Yamaha", "Fazer")
teste_veiculo(moto)