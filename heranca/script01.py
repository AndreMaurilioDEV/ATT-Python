from abstracao.script import Veiculo

# Classe Moto herda de Veiculo
class Moto(Veiculo):

  # Chama o construtor da classe pai Carro
  def __init__(self, marca, modelo, velocidade = 0):
    super().__init__(marca, modelo, velocidade)

  # Sobreescreve o metódo acelerar da classe Veiculo, adicionando 10 de velocidade e mostra a velocidade atual
  def acelerar(self):
    self.velocidade += 15
    print(f"Acelerou!! Velocidade Atual: {self.velocidade} km/h")

# Sobreescreve o metódo frear da classe Veiculo, se a velocidade for maior que 0, diminui em 10 e mostra a velocidade atual
  def frear(self):
    if (self.velocidade > 0):
      self.velocidade -= 10
      print(f"Freou!! Velocidade Atual: {self.velocidade} km/h")
    else: 
      print("Moto Parada")

  
# Instancia um objeto de Moto
minhamoto = Moto("Honda", "CB2000", 20)
minhamoto.acelerar()
minhamoto.frear()