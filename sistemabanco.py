depósito = 0
numero_saques = 1
saldo = 0
extrato = []
print(
"""
    MENU
DEPÓSITO = D
SAQUE = S
EXTRATO = E
SAIR = F
"""
)
while True:
    operacao = input("Digite qual operacao deseja realizar?")
    if operacao == 'D':
        depósito = int(input("Digite o valor a ser depósitado: "))
        lista_deposito = []
        extrato.append(f"Depósito: R$ {depósito}")
        saldo += depósito
    elif operacao == 'S':
        saque = int(input("Qual valor deseja sacar: "))
        if numero_saques <= 3 and saque <= saldo:
            print("Saque Liberado")
            saldo -= saque
            numero_saques += 1
            extrato.append(f"Saque: R$ {saque}")
        else:
            print("Saque Negado")
    elif operacao == 'E':
        acumulador = 0
        for i in range(len(extrato)):
            print(extrato[acumulador])
            acumulador += 1
    if operacao =='F':
        break