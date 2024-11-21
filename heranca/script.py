from abstracao.script import Veiculo
from composicao.script import Motor

# Classe Carro herda de Veiculo
class Carro(Veiculo):

  # Chama o construtor da classe pai Veiculo com atributo potencia instanciado da classe Motor
  def __init__(self, marca, modelo, velocidade = 0, potencia=0):
    super().__init__(marca, modelo, velocidade)
    self.motor = Motor(potencia)

  # Sobreescreve o metódo acelerar da classe Veiculo, adicionando 10 de velocidade e mostra a velocidade atual
  def acelerar(self):
    self.velocidade += 10
    print(f"Acelerou!! Velocidade Atual: {self.velocidade} km/h")

# Sobreescreve o metódo frear da classe Veiculo, se a velocidade for maior que 0, diminui em 10 e mostra a velocidade atual
  def frear(self):
    if (self.velocidade > 0):
      self.velocidade -= 10
      print(f"Freou!! Velocidade Atual: {self.velocidade} km/h")
    else: 
      print("Carro Parado")

  # Mostra a potencia do motor a partir da classe Instanciada
  def mostrar_potencia(self):
    print(f"Potência do motor: {self.motor.potencia}")

  
# Instancia um objeto de Carro
meucarro = Carro("Fiat", "Uno", 100, 400)
meucarro.acelerar()
meucarro.frear()