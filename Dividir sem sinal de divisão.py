dividendo = int(input("digite o numero que será dividido: "))
divisor = int(input("digite o numero que será o divisor: "))

resultado = 0
resto = 0

if divisor == 0:
    print("É impossível dividor qualquer número por 0")

if dividendo == 0:
    print("0 divido por qualquer número é 0")

while dividendo >= divisor:
    resto = dividendo - divisor
    dividendo -= divisor
    resultado += 1

print(f"O resultado da divisão é: {resultado}\n"
      f"O resto da divisão é: {resto} ")
