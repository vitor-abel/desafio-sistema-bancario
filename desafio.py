menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[q] Sair

=> """

saldo = 0.
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def sacar (*,saldo, saque, extrato, limite, numero_saques, limite_saques):
    if(numero_saques<LIMITE_SAQUES):
        if(saque>=0):
            if (saque<=limite):
                if (saldo-saque>=0):
                    saldo -= saque
                    numero_saques = numero_saques+1
                    extrato += f"Saque: R${saque:.2f}\n"
                    print("Saque concluído")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor superior ao limite de R$500,00")
        else:
            print("Valores negativos são inválidos para saque")
    else:
        print("Número de saques excedeu o limite de 3 saques diários")
    return saldo, extrato

def depositar (saldo, deposito, extrato, /):
    if (deposito >= 0):
        saldo += deposito;
        extrato += f"Depósito: R${deposito:.2f}\n"
        print("Depósito concluído")
    else:
        print("Valor inválido para depósito")
    return saldo, extrato

def exibir_extrato (saldo, / , *, extrato):
    print("Extrato:")
    print(extrato)
    print(f"Saldo atual da conta: R${saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input ("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já possui usuário cadastrado")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço do usuário (Logradouro, Número, Bairro, Cidade, Sigla de Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado")

def filtrar_usuario(cpf,usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito= float(input("O quanto você quer depositar? "))
        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "s":
        saque = float(input("O quanto você quer sacar? "))
        saldo, extrato = sacar(saldo = saldo, saque = saque, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        contas.append(conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")