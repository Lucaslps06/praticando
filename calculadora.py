import sys


def obter_number_input(msg):
    num = input(msg)
    if num.isalpha():
        print("Digite apenas número")
        sys.exit()
    return int(num)


def realizar_operacao(operacao, num1, num2):
    if operacao == "1":
        soma = num1 + num2
        return soma
    elif operacao == "2":
        sub = num1 - num2
        return sub
    elif operacao == "3":
        mult = num1 * num2
        return mult
    elif operacao == "4":
        divis = num1 / num2
        return divis


num1 = obter_number_input("Digite um número: \n")
num2 = obter_number_input("Digite outro: \n")

print("Fale a operação que você quer?")
print("1 soma")
print("2 subtração")
print("3 multiplicação")
print("4 divisão: \n")

operacao = input("Digite o número da operação: \n")

if operacao.isalpha():
    print("Digite apenas número")
    sys.exit()

resultado = realizar_operacao(operacao, num1, num2)

operacoes = {
    "1": {"operacao": "soma", "sinal": "+"},
    "2": {"operacao": "subtração", "sinal": "-"},
    "3": {"operacao": "multiplicação", "sinal": "*"},
    "4": {"operacao": "divisão", "sinal": "/"},
}

print(
    f"O resultado da operação de {operacoes[operacao]["operacao"]} de {num1} {operacoes[operacao]["sinal"]} {num2} é {resultado}"
)
