class ContaBancaria:

  # Construtor da classe
  def __init__(self, numero_conta, titular, saldo):
      self.__numero_conta = numero_conta
      self.__titular = titular
      self.__saldo = saldo

  # Metodo da classe que realiza depósito se o valor do saldo for válido
  def depositar(self, valor):
      if valor > 0:
          self.__saldo += valor
          print(f"Depósito de R${valor} foi realizado!")
      else:
          print("Valor do depósito é inválido.")

  # Metodo da classe que realiza saque se o valor do saldo for válido
  def sacar(self, valor):
      if (self.__saldo > 0):
        self.__saldo -= valor
        print(f"Saque de R${valor} realizado")
      else:
        print("Saldo Insuficiente")

  # Metodo da classe que consulta o saldo
  def consultarSaldo(self):
      return self.__saldo
  

# Instancia um objeto de ContaBancaria
nova_conta = ContaBancaria(1, "André", 1000)
nova_conta.consultarSaldo()
nova_conta.depositar(15)
nova_conta.sacar(500)