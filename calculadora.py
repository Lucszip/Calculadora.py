import math
opcao = 0
while opcao != 12:
    print("""
    [1] = Multiplicação
    [2] = Soma
    [3] = Subtração
    [4] = divisão
    [5] = Raiz quadrada
    [6] = Tabuada
    [7] = hipotenusa
    [8] = conversão para binario
    [9] = conversão para octal
    [10] = conversão para hexadecimal
    [11] = par ou impar
    [12] = Sair
    """)
    opcao = int(input("Qual opção você deseja?: "))
    if opcao == 1: #multiplicação
        n1 = int(input("Escolha um número: "))
        n2 = int(input("Escolha outro numero: "))
        n3 = n1 * n2
        print("A multiplicação desses dois números é igual: {0} ".format(n3))
        print("=-"*20)
    elif opcao == 2: #soma
        n1 = int(input("Escolha um número: "))
        n2 = int(input("Escolha outro numero: "))
        n3 = n1 + n2
        print("A soma desses dois numeros é igual: {0} ".format(n3))
        print("=-"*20)
    elif opcao == 4: #divisão 
        n1 = int(input("Escolha um número: "))
        n2 = int(input("Escolha outro número: "))
        n3 = n1 / n2
        print("A divisão desses dois números é igual: {0} ".format(n3))
        print("=-"*20)
    elif opcao == 5: #raiz quadrada, serve tanto pra exata e não exata
        n1 = int(input("Coloque um valor: "))
        raiz = math.sqrt(n1)
        print("A raiz de {0} é igual a: {1} ".format(n1,raiz))
        print("=-"*20)
    elif opcao == 6: #tabuada de qualquer número
        n1 = int(input("Coloque o número que você queira ver a tabuada: "))
        for tabua in range(1,11):
            print("{0} x {1} = {2} ".format(n1,tabua,n1 * tabua))
        print("=-"*20)
    elif opcao == 7: #calcular a hipotenusa, quanto ela vai medir
        cao = float(input("Comprimento do cateto oposto: "))
        caa = float(input("Comprimento do cateto adjacente: "))
        hi = math.hypot(cao,caa)
        print("A hipotenusa vai medir: {0} ".format(hi))
        print("=-"*20)
    elif opcao == 8: #saber o numero em binario
       n1 = int(input("Digite um número inteiro: "))
       print("{0} convertido para binario é igual: {1} ".format(n1,bin(n1)[2:]))
       print("=-"*20)
    elif opcao == 9: #saber o numero em octal
        n1 = int(input("Digite um número inteiro: "))
        print("{0} convertido para octal é igual: {1} ".format(n1,oct(n1)[2:]))
        print("=-"*20)
    elif opcao == 10: #saber o numero em hexadecimal
        n1 = int(input("Digite um número inteiro: "))
        print("{0} convertido para hexadecimal é igual: {1} ".format(n1,hex(n1)[2:]))
        print("=-"*20)
    elif opcao == 11: #verificar se o numero é par ou impar
        n1 = int(input("Digite um número: "))
        if n1 % 2 == 0:
            print("Esse número é par")
        else:
            print("Esse número é impar ")
    elif opcao == 12:
        exit("Até mais, volte sempre")
    else:
        print("Opção não encontrada")