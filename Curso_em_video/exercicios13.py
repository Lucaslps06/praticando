salario = float(input("Me fale seu salario atual \n").replace(",", "."))

salario_novo = salario + (salario * 0.15)

print(f"O seu salario vai de R${salario:.2f} para R${salario_novo:.2f}")
