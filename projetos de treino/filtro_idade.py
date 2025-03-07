# 1
firstAge = int(input("Qual a idade inicial do filtro? \n"))
secondAge = int(input("Qual a idade final do filtro? \n"))

pessoas = [
    {"name": "Daniel", "age": 24},
    {"name": "Lucas", "age": 18},
    {"name": "Vitor", "age": 28},
]


def filtrar_pessoa(pessoa):
    return firstAge <= pessoa["age"] <= secondAge


pessoasFiltradas = filter(filtrar_pessoa, pessoas)

nomes = list(pessoasFiltradas)

print(nomes)
