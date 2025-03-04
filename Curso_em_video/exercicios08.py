metros = float(input("Digite um valor em metros: \n").replace(",", "."))

mm = metros * 1000
cm = metros * 100

print(f"{metros} metros é igual a {cm:.0f} centímetros")
print(f"{metros} metros é igual a {mm:.0f} milímetros")
