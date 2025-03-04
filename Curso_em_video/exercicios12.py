preco = float(input("Me fale o preço do produto \n").replace(",", "."))

desconto = preco - (preco * 0.05)

print(f"O valor do produto com o desconto vai de R${preco:.2f} para R${desconto:.2f}")
