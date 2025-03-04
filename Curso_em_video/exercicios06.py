number_imput = input("Digite um número: \n")

if number_imput.isnumeric():
    number = int(number_imput)
    print(f"o dobro de {number} é {number*2} e sua raiz quadrada é {number**(1/2):.3f}")

else:
    print("Digite somente numeros")
