def mostrar(nome, valor):
    # Função para exibir o nome da escala e o valor formatado
    if valor == int(valor):
        # Se o valor for inteiro, mostra sem casas decimais
        print(f"{nome}: {int(valor)}")
    else:
        # Se o valor for decimal, mostra normalmente
        print(f"{nome}: {valor}")

# Solicita ao usuário a temperatura e a escala (ex: 30 C)
entrada = input("Digite uma temperatura a ser convertida: ")

# Divide a entrada em valor e escala
partes = entrada.split()

# Converte o valor para float e armazena a escala
temperatura = float(partes[0])
escala = partes[1].upper()

# Verifica a escala e faz as conversões necessárias
if escala == "C":
    # Celsius para Fahrenheit e Kelvin
    F = (temperatura * 9/5) + 32
    K = temperatura + 273.15

    mostrar("Fahrenheit", F)
    mostrar("Kelvin", K)
elif escala == "F":
    # Fahrenheit para Celsius e Kelvin
    C = (temperatura - 32) * 5/9
    K = (temperatura - 32) * 5/9 + 273.15

    mostrar("Celsius", C)
    mostrar("Kelvin", K)
elif escala == "K":
    # Kelvin para Celsius e Fahrenheit
    C = temperatura - 273.15
    F = (temperatura - 273.15) * 9/5 + 32

    mostrar("Celsius", C)
    mostrar("Fahrenheit", F)
else:
    # Caso a escala não seja reconhecida
    print("Entrada errada")
    exit()