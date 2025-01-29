class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)
        self.ativo = False

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo} | Ativo: {self.ativo}'
    
    def mudar_status_conta(self):
            self.ativo = not self.ativo
        

    
cb1 = ContaBancaria('Jonas', 1500000)
cb2 = ContaBancaria('Matheus', 5000000)

print(cb1)
print(cb2)
ContaBancaria.mudar_status_conta(cb1)
print(cb1)
