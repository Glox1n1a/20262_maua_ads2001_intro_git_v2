import calculadora
opcao = int(input("digite um numero de 1 a 4 para escolher a operação desejada: "))

if opcao == 1:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = calculadora.somar(a, b)
print(f"O resultado da soma é: {resultado}") 
elif opcao == 2:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = calculadora.subtrair(a, b)
print(f"O resultado da subtração é: {resultado}")
elif opcao == 3:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = calculadora.multiplicar(a, b)
print(f"O resultado da multiplicação é: {resultado}")
elif opcao == 4:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = calculadora.dividir(a, b)
print(f"O resultado da divisão é: {resultado}")