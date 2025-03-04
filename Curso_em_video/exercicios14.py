tipo_de_coverção = int(
    input(
        "De qual maneira você quer converter? \n 1-Graus para Fahrenheit \n 2-Fahrenheit para Graus \n Digite o numero referente a converção:"
    )
)

if tipo_de_coverção == 1:
    G_F = int(input("Quantos Graus devo converter? \n"))

    F = (G_F * 9 / 5) + 32
    print(f"{G_F} Graus é igual a {F}Fahrenheit")

elif tipo_de_coverção == 2:
    F_G = int(input("Quantos Fahrenheit devo converter para Graus? \n"))
    G = (F_G - 32) * 5 / 9
    print(f"{F_G} Fahrenheit é igual a {G} Graus")

else:
    print("Essa opção não existe!")
