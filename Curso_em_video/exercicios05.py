number_input = input("Fale um numero inteiro: \n")

if number_input.isdigit():
    number = int(number_input)
    antecessor = number - 1
    posterior = number + 1
    print(f"O número anterior a {number} é o {antecessor} e o posterior é {posterior}.")

elif number_input.isalpha():
    print("Letras não são permitidas, somente numeros inteiros")

else:
    print("São permitidos somente numeros inteiros")
