altura = float(input("Me fale a altura da parede \n").replace(",", "."))
comprimento = float(input("e o comprimento \n").replace(",", "."))

# altura.isnumeric or altura.is
area = altura * comprimento

tinta = area / 2

print(f"A area {area} prescisa de {tinta} litros de tinta para pintar")
