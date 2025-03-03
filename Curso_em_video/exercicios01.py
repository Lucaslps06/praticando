nome = input("Qual é o seu nome? \n")
dia = input("É um prazar te conhecer {}, que dia você nasceu? \n".format(nome))
mes = input("De que mês? \n")
ano = int(input("De que ano? \n"))

idade = 2025 - ano

print(
    "{} você nasceu dia {} do mês {} de {} ano e esse ano vai fazer {} anos".format(
        nome, dia, mes, ano, idade
    )
)
