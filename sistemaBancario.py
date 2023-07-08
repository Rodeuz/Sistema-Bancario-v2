import textwrap

def menu(): 
  tecla = input("""
  [d] para Depositar 
  [s] para Sacar 
  [e] para ver o Extrato
  [nc] Criar Nova conta
  [lc] Listar contas
  [nu] Criar Novo Usuario
  [n] para Sair

  => """)
  return tecla

def depositar(saldo,valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("\nDepósito realizado com sucesso!")
  else:
    print("\n Operação falhou! O valor informado é inválido. ")

  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  ultrapassou_saldo = valor > saldo
  ultrapassou_limite = valor > limite
  ultrapassou_saques = numero_saques >= limite_saques

  if ultrapassou_saldo:
    print("\n\n--------Saldo Insuficiente------------")
  elif ultrapassou_limite:
    print("\n\n--------Saque acima do limite permitido------------")
  elif ultrapassou_saques:
    print("\n----------limite de saque diario atingido----------\n")

  elif valor > 0:
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    print("\n------------Saque realizado com sucesso!------------")

  else:
    print("\nOperação falhou! O valor informado é inválido.")

  return saldo, extrato

def mostrar_extrato(saldo,/,*, extrato):
  print("\n ------------------ EXTRATO ------------------")
  print("Não foram realizados movimentações." if not extrato else extrato)
  print(f"\nSaldo:\t\tR$ {saldo:.2f}")
  print("------------------------------------------------")

def novo_usuario(usuarios):
  cpf = input("Informe o CPF (somente números): ")
  usuario = filtro_usuario(cpf, usuarios)

  if usuario:
    print("\n--- Já existe usuário com esse CPF! ---")
    return

  nome = input("Informe o nome completo: ")
  nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

  usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereco": endereco})

  print("------------ Usuário criado com sucesso! ------------")


def filtro_usuario(cpf, usuarios):
  usuario_filtrados =  [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuario_filtrados[0] if usuario_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtro_usuario(cpf, usuarios)

  if usuario:
        print("\n------------- Conta criada com sucesso! -------------")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  

  print("\n------------ Usuário não encontrado------------")


def listar_contas(contas):
  for conta in contas:
      linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
      """
      print("=" * 100)
      print(textwrap.dedent(linha))

def main():
  SAQUE_LIMITE = 3
  AGENCIA = '0001'

  saldo = 0
  limite = 500
  extrato = ''
  numero_saques = 0
  usuarios = []
  contas = []
  sistema = True

  while sistema == True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("informe o valor do depósito: "))

      saldo,extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))

      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=SAQUE_LIMITE,
      )
    
    elif opcao == "e":
      mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      novo_usuario(usuarios)

    elif opcao == "nc":
      numero_conta = len(contas) + 1
      conta = nova_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
    
    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "n":
      break
    
    else:
      print("Operação inválida")

main()



