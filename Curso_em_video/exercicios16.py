import math

number1 = float(
    input("Digite um numereo real: \n Exemplo (1,234) \n").replace(",", ".")
)

print(f"O numero {number1} tem a parte inteira {math.trunc(number1)}")
