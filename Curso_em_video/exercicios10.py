real = float(input("Quantos reais você tem? \n").replace(",", "."))

dolar = real / 5.89

print(f"No momento você pode comprar {dolar:.2f} dolares.")
