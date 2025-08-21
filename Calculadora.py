numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


print("Escolha a operação: +, -, *, /")
operacao = input("Digite a operação desejada:")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
else: 
    print("Operação inválida")
    
