D = input("digite alguma palavra:")

print("O tipo primitivo desse valor é", type(D))

print("é alphanumérico?", D.isalnum())
print("é letra?", D.isalpha())
print("é numero?", D.isnumeric())
print("é decimal?", D.isdecimal())
print("é um espaço?", D.isspace())
print("é maiusculo?", D.isupper())
print("é minusculo?", D.islower())
print("a primeira letra é maiuscula?", D.istitle())
