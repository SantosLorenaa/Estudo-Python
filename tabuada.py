while True:
    numero = input("Digite um número para ver sua tabuada ou sair para encerrar:")
    
    
    if numero.lower() == "sair":
        print("Encerrando o programa")
        break
    
    if numero.isdigit():
        numero = int(numero)
        print(f"\nTabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    else:
            print("Por favor, digite um número válido.")