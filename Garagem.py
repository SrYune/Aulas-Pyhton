
CAPACIDADE = 20
VALOR_HORA = 8.00

veiculos = []
faturamento = 0.0


def registrar_entrada():
    global veiculos

    if len(veiculos) < CAPACIDADE:
        placa = input("Digite a placa do veículo: ").upper()

        veiculos.append(placa)

        print("Entrada registrada com sucesso!")
    else:
        print("Estacionamento lotado!")


def registrar_saida():
    global faturamento, veiculos

    placa = input("Digite a placa do veículo: ").upper()

    if placa in veiculos:
        horas = int(input("Quantas horas o veículo ficou estacionado? "))

        valor = horas * VALOR_HORA

        print("Valor a pagar: R$", valor)

        faturamento = faturamento + valor

        veiculos.remove(placa)

        print("Saída registrada com sucesso!")
    else:
        print("Veículo não encontrado no estacionamento.")


def consultar_vagas():
    ocupadas = len(veiculos)
    disponiveis = CAPACIDADE - ocupadas

    print("\n--- CONSULTA DE VAGAS ---")
    print("Capacidade total:", CAPACIDADE)
    print("Veículos estacionados:", ocupadas)
    print("Vagas disponíveis:", disponiveis)


def consultar_faturamento():
    print("\n--- FATURAMENTO ---")
    print("Total arrecadado: R$", faturamento)


def menu():
    opcao = -1

    while opcao != 0:
        print("\n===== SISTEMA DE ESTACIONAMENTO =====")
        print("1 - Registrar entrada de veículo")
        print("2 - Registrar saída de veículo")
        print("3 - Consultar vagas disponíveis")
        print("4 - Consultar faturamento")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            registrar_entrada()

        elif opcao == 2:
            registrar_saida()

        elif opcao == 3:
            consultar_vagas()

        elif opcao == 4:
            consultar_faturamento()

        elif opcao == 0:
            print("Sistema encerrado!")

        else:
            print("Opção inválida!")


menu()
