def linha_inicio_fim():
    print("_" * 50)


dias_alugados = int(input("Por quantos dias o carro ficou alugado? \n"))
km_rodados = float(input("Quantos Km foram rodados? \n"))

pg_dias = dias_alugados * 60
pg_km = km_rodados * 0.15

linha_inicio_fim()
print(
    f"O total a ser pagos é R${pg_dias + pg_km:.2f} \nR${pg_dias:.2f} referente aos dias alugados \nR${pg_km} referente aos quilometros rodados"
)
linha_inicio_fim()
