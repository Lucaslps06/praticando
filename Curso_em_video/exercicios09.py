# n1 = int(input("Digite um número: \n"))

# tabuada = f"A tabuada de {n1} é "
# for i in range(10):
#     tabuada += str(n1 * (i + 1)) + "; "
# print(tabuada)

n1 = int(input("Digite um número: \n"))

for i in range(10):
    print(f"{n1}x{i+1} = {n1 * (i + 1)} \n")
