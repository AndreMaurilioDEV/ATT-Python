from abc import ABC, abstractmethod # import ABC

class Veiculo(ABC):

  # Construtor da classe
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.velocidade = 0

  # metodos abstratos da class
  @abstractmethod
  def acelerar(self): 
    pass

  @abstractmethod
  def frear(self): 
    pass

  @abstractmethod
  def mostrar_velocidade(self): 
    pass