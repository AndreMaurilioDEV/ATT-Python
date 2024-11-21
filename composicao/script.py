class Motor:
    # Construtor da classe
    def __init__(self, potencia):
        self.potencia = potencia 

    # Exibe a potencia do motor
    def __str__(self):
        return f"{self.potencia}"