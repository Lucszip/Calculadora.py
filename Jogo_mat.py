#Jogo da matematica criado pelo Lucas
import time
print("=-"*30)
print("Jogo de matematica")
print("=-"*30)
jogador = str(input("\033[0;33m Digite seu nome: \033[m ")) #Para conhecer o jogador
n = 0
pontos = 0
erros = 0
while True: #usamos While True para definir ele como infinito, somente o break pode interromper
    print("""\033[0;33m Bem vindo a lista de opções: \033[m
        \033[0;33;31m [1] \033[m = \033[0;36m Fácil \033[m
        \033[0;33;31m [2] \033[m = \033[0;36m Dificil \033[m
        \033[0;33;31m [3] \033[m = \033[0;36m Impossivel \033[m 
        \033[0;33;31m [4] \033[m = \033[0;36m Sair \033[m 
        """)
    print(f"\033[0;36m Até agora tem {pontos} pontos de acertos \033[m e \033[0;32m {erros} erros ")
    n = int(input("\033[0;33m Escolha a opção: \033[m ")) #escolha de opção para a lista de fácil, dificil, impossivel e sair
    if n == 1: 
        print("""
        \033[0;33;31m [1] \033[m = \033[0;36m Desafio de soma \033[m
        \033[0;33;31m [2] \033[m = \033[0;36m Desafio de multiplicação \033[m
        \033[0;33;31m [3] \033[m = \033[0;36m Desafio de divisão \033[m
        \033[0;33;31m [4] \033[m = \033[0;36m Desafio da Raiz Quadrada \033[m
        \033[0;33;31m [5] \033[m = \033[0;36m Sair \033[m
        """)
        facil = int(input("\033[0;33m Digite a opção: \033[m ")) #a lista dos desafios na opção fácil
        if facil == 1:  #usamos o if para quando a pessoa clicar, vai aparecer a tela abaixo
            print("="*45)
            print(f"Seja bem vindo ao jogo de matematica, {jogador}")
            print("Nivel: fácil ")
            print("Desafio da soma ")
            print("="*45)
            pontos_soma = 0 #um contador para saber quantos pontos/acertos a pessoa fez no desafio da soma nivel fácil
            erros_soma = 0 #um contador para saber quantos erros a pessoa fez no desafio da soma nivel fácil
            soma = 190 #declaração de variavel 
            soma1 = 20 #declaração de variavel
            resultado = 190 + 20 #soma das variaveis soma e soma1 
            soma2 = 213 #declaração de variavel
            soma3 = 125 #declaração de variavel
            resultado1 = 213 + 125 #soma das variaveis soma2 e soma3
            soma4 = 10 #declaração de variavel
            soma5 = 50 #declaração de variavel
            resultado2 = 10 + 50 #soma das variaveis soma 4 e soma 5
            soma6 = 35  #declaração de variavel
            soma7 = 57 #declaração de variavel
            resultado3 = 35 + 57 #soma das variaveis soma6 e soma7
            soma8 = 123 #declaraçãp de variavel 
            soma9 = 253 #declaração de variavel
            resultado4 = 123 + 253 #soma das variaveis soma8 e soma9
            while True:  #colocar em loop, até ser interrompido por um break
                desafio_facil = int(input(f"Quanto é? {soma} + {soma1}: ")) #declarei a variavel como int (int - numero inteiro), input - (entrada de dados) - f - .format, disponivel somente versão 3.6 pra cima
                if desafio_facil == resultado: #se desafio_facil for igual a resultado mostra print("acertou")
                    print("\033[0;36m Você acertou :D \033[m") #\033 usado para colocar cor, 36m é cor azul
                    print("\033[0;36m Passando para nova etapa... \033[m") #o mesmo aqui
                    pontos += 1 #quando você acerta, você ganha um ponto (esse ponto é o total)
                    pontos_soma += 1 #quando vocẽ acerta, você ganha um ponto, somente nesse desafio fácil de soma
                    time.sleep(3) #biblioteca de tempo importada, para demorar 3s para ir outra pergunta
                elif desafio_facil != resultado:
                    print(f"\033[0;32m Você errou, era {resultado} \033[m") #\033[0;32m 32m é para verde
                    erros += 1 #quando você erra, vocẽ ganha um ponto de erro (esse ponto é o total)
                    erros_soma += 1 #quando você erra, você ganha um ponto de erro, somente nesse desafio facil de soma
                desafio_facil1 = int(input(f"Quanto é? {soma2} + {soma3}: ")) 
                if desafio_facil1 == resultado1:
                    print("\033[0;36m Você acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m")
                    pontos += 1
                    pontos_soma += 1
                    time.sleep(3)
                elif desafio_facil1 != resultado1:
                    print(f"\033[0;32m Você errou, era {resultado1} \033[m ")
                    erros += 1
                    erros_soma += 1
                desafio_facil2 = int(input(f"Quanto é {soma4} + {soma5}: "))
                if desafio_facil2 == resultado2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_soma += 1
                    time.sleep(3)
                elif desafio_facil2 != resultado2:
                    print(f"\033[0;32m Você errou, era {resultado2} \033[m ")
                    erros += 1
                    erros_soma += 1
                desafio_facil3 = int(input(f"Quanto é {soma6} + {soma7}: "))
                if desafio_facil3 == resultado3:
                    print("\033[0;36 Você acertou :D \033[m ")
                    print("\033[0;36 Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_soma += 1
                    time.sleep(3)
                elif desafio_facil3 != resultado3:
                    print(f"\033[0;32m Você errou, era {resultado3} \033[m ")
                    erros += 1
                    erros_soma += 1
                desafio_facil4 = int(input(f"Quanto é {soma8} + {soma9}: "))
                if desafio_facil4 == resultado4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Nivel fácil de soma, acabado \033[m ")
                    pontos_soma += 1
                    pontos += 1
                elif desafio_facil4 != resultado4:
                    print(f"\033[0;32m Você errou, era {resultado4} \033[m ")
                    print("\033[0;36m Nivel fácil de soma, acabado \033[m ")
                    erros += 1
                    erros_soma += 1
                print(f"\033[0;36m Você acertou até agora {pontos_soma} \033[m e \033[0;32m errou até agora {erros_soma} \033[m ")
                print(" Voltando... ")
                time.sleep(3) 
                break #para interromper o while True e voltar para tela de inicio, que tem facil, dificil e impossivel
        elif facil == 2:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador}")
            print("Nivel: Fácil ")
            print("Desafio da Multiplicação ")
            print("="*45)
            pontos_multi = 0 #pontos para o desafio da multiplicação, se alguém acertar, ela ganha
            erros_multi = 0 #pontos para alguém que erre nesse desafio de multiplicação nivel dificil
            mult = 5 #declaração de variavel
            mult1 = 12 #declaração de variavel
            multiplicacao = 5 * 12 #soma das variaveis mult e mult1, só pegando os numeros
            mult2 = 2 #declaração de variavel
            mult3 = 8 #declaração de variavel
            multiplicacao1 = 2 * 8 #soma das variaveis mul2 e mult3, só pegando os numeros 
            mult4 = 3 #declaração de variavel
            mult5 = 6 #declaração de variavel
            multiplicacao2 = 3 * 6 #
            mult6 = 4 
            mult7 = 4
            multiplicacao3 = 4 * 4
            mult8 = 6
            mult9 = 9
            multiplicacao4 = 6 * 9
            while True: #deixar em loop
                desafio_facil5 = int(input(f"Quanto é? {mult} X {mult1}: "))
                if desafio_facil5 == multiplicacao:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_multi += 1 #contador, para quando a pessoa acertar , ela ganha um ponto
                    time.sleep(3) 
                elif desafio_facil5 != multiplicacao: #se desafio_facil5 for diferente de multiplicacao
                    print(f"\033[0;32m Você errou, era {multiplicacao} \033[m") #lança esse print
                    erros += 1 #contador, para quando a pessoa errar, ela ganha um ponto
                    erros_multi += 1 #mesma coisa
                desafio_facil6 = int(input(f"Quanto é? {mult2} X {mult3}: "))
                if desafio_facil6 == multiplicacao1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_multi += 1
                    time.sleep(3)
                elif desafio_facil6 != multiplicacao1:
                    print(f"\033[0;32m Você errou, era {multiplicacao1} \033[m")
                    erros_multi += 1
                    erros += 1
                desafio_facil7 = int(input(f"Quanto é? {mult4} X {mult5}: "))
                if desafio_facil7 == multiplicacao2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_multi += 1
                    time.sleep(3)
                elif desafio_facil7 != multiplicacao2:
                    print(f"\033[0;32m Você errou, era {multiplicacao2} \033[m")
                    erros_multi += 1
                    erros += 1
                desafio_facil8 = int(input(f"Quanto é? {mult6} X {mult7}: "))
                if desafio_facil8 == multiplicacao3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_multi += 1
                    time.sleep(3)
                elif desafio_facil8 != multiplicacao3:
                    print(f"\033[0;32m Você errou, era {multiplicacao3} \033[m ")
                    erros_multi += 1
                    erros += 1
                desafio_facil9 = int(input(f"Quanto é? {mult8} X {mult9}: "))
                if desafio_facil9 == multiplicacao4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Nivel fácil de multiplicação, acabado \033[m ")
                    pontos += 1
                    pontos_multi += 1
                elif desafio_facil9 != multiplicacao4:
                    print(f"\033[0;32m Você errou, era {multiplicacao4} \033[m ")
                    print("\033[0;36m Nivel fácil de multiplicação, acabado \033[m ")
                    erros_multi += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {pontos_multi} \033[m e \033[0;32m errou até agora {erros_multi} \033[m ") #print para mostrar quantos acertos e erros até agora nesse desafio
                print(" Voltando... ")
                time.sleep(3)
                break
        elif facil == 3: #se a pessoa escolher a opção 3, aparece isso abaixo
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador}")
            print("Nivel: Fácil ")
            print("Desafio da Divisão ")
            print("="*45)
            pontos_divi = 0 #contador de pontos , se uma pessoa acertar o desafio da divisão nivel fácil
            erros_divi = 0
            divi = 4
            divi1 = 2
            resu_divi = 4 / 2
            divi2 = 12
            divi3 = 6
            resu_divi1 = 12 / 6
            divi4 = 24
            divi5 = 2
            resu_divi2 = 24 / 2
            divi6 = 6
            divi7 = 3
            resu_divi3 = 6 / 3
            divi8 = 8
            divi9 = 4
            resu_divi4 = 8 / 4
            while True: #para deixar o programa em loop, só pode ser quebrado com o break
                desafio_facil10 = int(input(f"Quanto é? {divi} / {divi1}: "))
                if desafio_facil10 == resu_divi:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_divi += 1
                    time.sleep(3)
                elif desafio_facil10 != resu_divi:
                    print(f"\033[0;32m Você errou, era {resu_divi} \033[m ")
                    erros_divi += 1
                    erros += 1
                desafio_facil11 = int(input(f"Quanto é? {divi2} / {divi3}: "))
                if desafio_facil11 == resu_divi1:
                    print("\033[0;36m Você acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m")
                    pontos += 1
                    pontos_divi += 1
                    time.sleep(3)
                elif desafio_facil11 != resu_divi1:
                    print(f"\033[0;36m Você errou, era {resu_divi1} \033[m ")
                    erros_divi += 1
                    erros += 1
                desafio_facil12 = int(input(f"Quanto é? {divi4} / {divi5}: "))
                if desafio_facil12 == resu_divi2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_divi += 1
                    time.sleep(3)
                elif desafio_facil12 != resu_divi2:
                    print(f"\033[0;32m Você errou, era {resu_divi2} \033[m ")
                    erros_divi += 1
                    erros += 1
                desafio_facil13 = int(input(f"Quanto é {divi6} / {divi7}: "))
                if desafio_facil13 == resu_divi3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos += 1
                    pontos_divi += 1
                    time.sleep(3)
                elif desafio_facil13 != resu_divi3:
                    print(f"\033[0;32m Você errou, era {resu_divi3} \033[m ")
                    erros_divi += 1
                    erros += 1
                desafio_facil14 = int(input(f"Quanto é {divi8} / {divi9}: "))
                if desafio_facil14 == resu_divi4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Nivel fácil de divisão, acabado \033[m ")
                    pontos += 1
                    pontos_divi += 1
                    time.sleep(3)
                elif desafio_facil14 != resu_divi4:
                    print(f"\033[0;32m Você errou, era {resu_divi4} \033[m ")
                    print(f"\033[0;32m Nivel fácil de divisão, acabado \033[m ")
                    erros_divi += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {pontos_divi} \033[m e \033[0;32m errou até agora {erros_divi} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif facil == 4: #se a pessoa escolher a opção 4, aparece isso abaixo
            print("="*45)
            print(f"Seja bem vindo ao jogo de matematica, {jogador} ")
            print("Nivel: Fácil ")
            print("Desafio da Raiz Quadrada ")
            print("="*45)
            pontos_raiz = 0
            erros_raiz = 0
            raiz = 2
            result_raiz = 1.41
            raiz1 = 4
            result_raiz1 = 2
            raiz2 = 9
            result_raiz2 = 3
            raiz3 = 5
            result_raiz3 = 2.23
            raiz4 = 12
            result_raiz4 = 3.46
            raiz5 = 3
            result_rauz5 = 1.73
            while True: #loop 
                desafio_facil15 = float(input(f"Qual é o resultado dessa raiz? {raiz}: ")) #float é numero flutuante , se eu add int, quando aparecer 4.8, vai aparecer errado, como é int e n float
                if desafio_facil15 == result_raiz:
                    print("\033[0;36m Você acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif desafio_facil15 != result_raiz:
                    print(f"\033[0;32m Você errou, era {result_raiz} \033[m ")
                    erros_raiz += 1
                    erros += 1  
                desafio_facil16 = float(input(f"Qual é o resultado dessa raiz? {raiz1}: "))
                if desafio_facil16 == result_raiz1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif desafio_facil16 != result_raiz1:
                    print(f"\033[0;32m Você errou, era {result_raiz1} \033[m ")
                    erros_raiz += 1
                    erros += 1
                desafio_facil17 = float(input(f"Qual é o resultado dessa raiz? {raiz2}: "))
                if desafio_facil17 == result_raiz2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif desafio_facil17 != result_raiz2:
                    print(f"\033[0;32m Você errou, era {result_raiz2} \033[m ")
                    erros_raiz += 1
                    erros += 1
                desafio_facil18 = float(input(f"Qual é o resultado dessa raiz? {raiz3}: "))
                if desafio_facil18 == result_raiz3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif desafio_facil18 != result_raiz3:
                    print(f"\033[0;32m Você errou, era {result_raiz3} \033[m ")
                    erros_raiz += 1
                    erros += 1
                desafio_facil19 = float(input(f"Qual é o resultado dessa raiz? {raiz4}: "))
                if desafio_facil19 == result_raiz4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    pontos_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif desafio_facil19 != result_raiz4:
                    print(f"\033[0;32m Você errou, era {result_raiz4} \033[m ")
                    print(f"\033[0;32m Nivel fácil de raiz quadrada, acabado \033[m ")
                    erros_raiz += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {pontos_raiz} \033[m e \033[0;32m errou até agora {erros_raiz} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif facil == 5:
            print("Até mais... ")
            exit()
            time.sleep(3)
    elif n == 2: #nivel dificil
        print("""
        \033[0;33;31m [1] \033[m = \033[0;36m Desafio de soma \033[m
        \033[0;33;31m [2] \033[m = \033[0;36m Desafio de multiplicação \033[m
        \033[0;33;31m [3] \033[m = \033[0;36m Desafio de divisão \033[m
        \033[0;33;31m [4] \033[m = \033[0;36m Desafio da Raiz Quadrada \033[m
        \033[0;33;31m [5] \033[m = \033[0;36m Sair \033[m
        """)
        dificil = int(input("\033[0;33m Digite a opção: \033[m "))
        if dificil == 1:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Dificil ")
            print("Desafio da soma ")
            print("="*45)
            points_som = 0
            errer_som = 0
            soma_difi = 230
            soma_difi1 = 136
            result_soma = soma_difi + soma_difi1
            soma_difi2 = 165
            soma_difi3 = 189
            result_soma1 = soma_difi2 + soma_difi3
            soma_difi4 = 286
            soma_difi5 = 243
            result_soma2 = soma_difi4 + soma_difi5
            soma_difi6 = 90
            soma_difi7 = 243
            result_soma3 = soma_difi6 + soma_difi7
            soma_difi8 = 129
            soma_difi9 = 129
            result_soma4 = soma_difi8 + soma_difi9
            while True:
                difi_soma = int(input(f"Quanto é? {soma_difi} + {soma_difi1}: "))
                if difi_soma == result_soma:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_som += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_soma != result_soma:
                    print(f"\033[0;32m Você errou, era {result_soma} \033[m")
                    errer_som += 1
                    erros += 1
                difi_soma1 = int(input(f"Quanto é? {soma_difi2} + {soma_difi3}: "))
                if difi_soma1 == result_soma1:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_som += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_soma1 != result_soma1:
                    print(f"\033[0;32m Você errou, era {result_soma1} \033[m ")
                    errer_som += 1
                    erros += 1
                difi_soma2 = int(input(f"Quanto é? {soma_difi4} + {soma_difi5}: "))
                if difi_soma2 == result_soma2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_som += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_soma2 != result_soma2:
                    print(f"\033[0;32m Você errou, era {result_soma2} \033[m ")
                    errer_som += 1
                    erros += 1
                difi_soma3 = int(input(f"Quanto é? {soma_difi6} + {soma_difi7}: "))
                if difi_soma3 == result_soma3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_som += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_soma3 != result_soma3:
                    print(f"\033[0;32m Você errou, era {result_soma3} \033[m ")
                    errer_som += 1
                    erros += 1
                difi_soma4 = int(input(f"Quanto é? {soma_difi8} + {soma_difi9}: "))
                if difi_soma4 == result_soma4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print(f"\033[0;36m Nivel Dificil de soma, acabado \033[m ")
                    points_som += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_soma4 != result_soma4:
                    print(f"\033[0;32m Você errou, era {result_soma4} \033[m ")
                    print(f"\033[0;32m Nivel Dificil de soma, acabado \033[m ")
                    errer_som += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {points_som} \033[m e \033[0;32m errou até agora {errer_som} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif dificil == 2:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Dificil ")
            print("Desafio da Multiplicação ")
            print("="*45)
            points_mul = 0
            errer_mul = 0
            multe = 6
            multe1 = 6
            result_multe = 6 * 6
            multe2 = 9
            multe3 = 9
            result_multe1 = 9 * 9
            multe4 = 5
            multe5 = 6
            result_multe2 = 5 * 6
            multe6 = 7
            multe7 = 7
            result_multe3 = 7 * 7
            multe8 = 8
            multe9 = 6
            result_multe4 = 8 * 6
            while True: #loop
                difi_multi = int(input(f"Quanto é? {multe} X {multe1}: "))
                if difi_multi == result_multe:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_mul += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_multi != result_multe:
                    print(f"\033[0;32m Você errou, era {result_multe} \033[m ")
                    errer_mul += 1
                    erros += 1
                difi_multi1 = int(input(f"Quanto é? {multe2} X {multe3}: "))
                if difi_multi1 == result_multe1:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_mul += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_multi1 != result_multe1:
                    print(f"\033[0;32m Vocẽ errou, era {result_multe1} \033[m ")
                    errer_mul += 1
                    erros += 1
                difi_multi2 = int(input(f"Quanto é? {multe4} X {multe5}: "))
                if difi_multi2 == result_multe2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_mul += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_multi2 != result_multe2:
                    print(f"\033[0;36m Você errou, era {result_multe2} \033[m ")
                    errer_mul += 1
                    erros += 1
                difi_multi3 = int(input(f"Quanto é? {multe6} X {multe7}: "))
                if difi_multi3 == result_multe3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_mul += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_multi3 != result_multe3:
                    print(f"\033[0;36m Você errou, era {result_multe3} \033[m ")
                    errer_mul += 1
                    erros += 1
                difi_multi4 = int(input(f"Quanto é? {multe8} X {multe9}: "))
                if difi_multi4 == result_multe4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print(f"\033[0;36m Nivel Dificil de multiplicação, acabado \033[m ")
                    points_mul += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_multi4 != result_multe4:
                    print("\033[0;32m Você errou \033[m ")
                    print(f"\033[0;32m Nivel Dificil de multiplicação, acabado \033[m ")
                    erros += 1
                    errer_mul += 1
                print(f"\033[0;36m Você acertou até agora {points_mul} \033[m e \033[0;32m errou até agora {errer_mul} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif dificil == 3:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Dificil ")
            print("Desafio da Divisão ")
            print("="*45)
            points_div = 0
            errer_div = 0
            divi = 14
            divi1 = 2
            result_divi = 14 / 2
            divi2 = 25
            divi3 = 5
            result_divi1 = 25 / 5
            divi4 = 81
            divi5 = 9
            result_divi2 = 81 / 9
            divi6 = 16
            divi7 = 2
            result_divi3 = 16 / 2
            divi8 = 38
            divi9 = 2
            result_divi4 = 38 / 2
            while True:
                difi_div = int(input(f"Quanto é? {divi} / {divi1}: "))
                if divi == result_divi:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_div += 1
                    pontos += 1
                    time.sleep(3)
                elif divi != result_divi1:
                    print(f"\033[0;32m Você errou, era {result_divi} \033[m ")
                    errer_div += 1
                    erros += 1
                difi_div1 = int(input(f"Quanto é? {divi2} / {divi3}: "))
                if difi_div1 == result_divi1:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_div += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_div1 != result_divi1:
                    print(f"\033[0;32m Você errou, era {result_divi1} \033[m")
                    errer_div += 1
                    erros += 1
                difi_div2 = int(input(f"Quanto é? {divi4} / {divi5}: "))
                if difi_div2 == result_divi2:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_div += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_div2 != result_divi2:
                    print(f"\033[0;36m Você errou, era {result_divi2} \033[m ")
                    errer_div += 1
                    erros += 1
                difi_div3 = int(input(f"Quanto é? {divi6} / {divi7}: "))
                if difi_div3 == result_divi3:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_div += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_div3 != result_divi3:
                    print(f"\033[0;36m Você errou, era {result_divi3} \033[m ")
                    errer_div += 1
                    erros += 1
                difi_div4 = int(input(f"Quanto é? {divi8} / {divi9}: "))
                if difi_div4 == result_divi4:
                    print("\033[0;36m Você acertou \033[m ")
                    print(f"\033[0;36m Nivel Dificil de divisão, acabado \033[m ")
                    points_div += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_div4 != result_divi4:
                    print(f"\033[0;32m Você errou, era {result_divi4} \033[m ")
                    print(f"\033[0;32m Nivel Dificil de divisão, acabado \033[m ")
                    errer_div += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {points_div} \033[m e \033[0;32m errou até agora {errer_div} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif dificil == 4:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Dificil ")
            print("Desafio da Raiz Quadrada ")
            print("="*45)
            points_raiz = 0
            errer_raiz = 0
            root = 17
            result_root = 4.12
            root1 = 21
            result_root1 = 4.58
            root2 = 64
            result_root2 = 8
            root3 = 100
            result_root3 = 10
            root4 = 121
            result_root4 = 11
            while True:
                difi_raiz = float(input(f"Qual é o resultado dessa raiz? {root}: "))
                if difi_raiz == result_root:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_raiz != result_root:
                    print(f"\033[0;32m Você errou, era {result_root} \033[m ")
                    errer_raiz += 1
                    erros += 1
                difi_raiz1 = float(input(f"Qual é o resultado dessa raiz? {root1}: "))
                if difi_raiz1 == result_root1:
                    print("\033[0;36m Você acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_raiz1 != result_root1:
                    print(f"\033[0;32m Você errou, era {result_root} \033[m ")
                    errer_raiz += 1
                    erros += 1
                difi_raiz2 = float(input(f"Qual é o resultado dessa raiz? {root2}: "))
                if difi_raiz2 == result_root2:
                    print("\033[0;36m Vocẽ acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_raiz2 != result_root2:
                    print(f"\033[0;32m Você errou, era {result_root2} ")
                    errer_raiz += 1
                    erros += 1
                difi_raiz3 = float(input(f"Qual é o resultado dessa raiz? {root3}: "))
                if difi_raiz3 == result_root3:
                    print("\033[0;36m Vocẽ acertou \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    points_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_raiz3 != result_root3:
                    print(f"\033[0;32m Você errou, era {result_root3} ")
                    errer_raiz += 1
                    erros += 1
                difi_raiz4 = float(input(f"Qual é o resultado dessa raiz? {root4}: "))
                if difi_raiz4 == result_root4:
                    print("\033[0;36m Vocẽ acertou \033[m ")
                    print(f"\033[0;36m Nivel Dificil de Raiz quadrada, acabado \033[m ")
                    points_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif difi_raiz4 != result_root4:
                    print(f"\033[0;32m Vocẽ errou, era {result_root4} ")
                    print(f"\033[0;32m Nivel Dificil de Raiz quadrada, acabado \033[m ")
                    errer_raiz += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {points_raiz} \033[m e \033[0;32m errou até agora {errer_raiz} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif dificil == 5:
            print("Até mais... ")
            exit()
            time.sleep(3)
    elif n == 3: #nivel impossivel
        print("""
        \033[0;33;31m [1] \033[m = \033[0;36m Desafio de soma \033[m
        \033[0;33;31m [2] \033[m = \033[0;36m Desafio de multiplicação \033[m
        \033[0;33;31m [3] \033[m = \033[0;36m Desafio de divisão \033[m
        \033[0;33;31m [4] \033[m = \033[0;36m Desafio da Raiz Quadrada \033[m
        \033[0;33;31m [5] \033[m = \033[0;36m Sair \033[m
        """)
        impossivel = int(input("\033[0;33m Digite a opção: \033[m "))
        if impossivel == 1:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Impossivel ")
            print("Desafio da Soma ")
            print("="*45)
            spots_som = 0
            errors_som = 0
            amount = 789
            amount1 = 675
            result_amount = amount + amount1
            amount2 = 875
            amount3 = 564
            result_amount1 = amount2 + amount3
            amount4 = 5685
            amount5 = 5231
            result_amount2 = amount4 + amount5
            amount6 = 7857
            amount7 = 4635
            result_amount3 = amount6 + amount7
            amount8 = 354
            amount9 = 764
            result_amount4 = amount8 + amount9
            while True:
                imposi_amo = int(input(f"Quanto é? {amount} + {amount1}: "))
                if imposi_amo == result_amount:
                    print("\033[0;36m Você acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_som += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_amo != result_amount:
                    print(f"\033[0;32m Você errou, era {result_amount} \033[m ")
                    errors_som += 1
                    erros += 1
                imposi_amo1 = int(input(f"Quanto é? {amount2} + {amount3}: "))
                if imposi_amo1 == result_amount1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_som += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_amo1 != result_amount1:
                    print(f"\033[0;32m Você errou, era {result_amount1} \033[m ")
                    errors_som += 1
                    erros += 1
                imposi_amo2 = int(input(f"Quanto é? {amount4} + {amount5}: "))
                if imposi_amo2 == result_amount2:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_som += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_amo2 != result_amount2:
                    print(f"\033[0;32m Vocẽ errou, era {result_amount2} \033[m")
                    errors_som += 1
                    erros += 1
                imposi_amo3 = int(input(f"Quanto é? {amount6} + {amount7}: "))
                if imposi_amo3 == result_amount3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_som += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_amo3 != result_amount3:
                    print(f"\033[0;32m Você errou, era {result_amount3} \033[m ")
                    errors_som += 1
                    erros += 1
                imposi_amo4 = int(input(f"Quanto é? {amount8} + {amount9}: "))
                if imposi_amo4 == result_amount4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print(f"\033[0;36m Nivel impossivel de soma, acabado \033[m ")
                    spots_som += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_amo4 != result_amount4:
                    print(f"\033[0;32 Você errou, era {result_amount4} \033[m ")
                    print(f"\033[0;32m Nivel Impossivel de soma, acabado \033[m ")
                    errors_som += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {spots_som} \033[m e \033[0;32m errou até agora {errors_som} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif impossivel == 2:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Impossivel ")
            print("Desafio da Multiplicação ")
            print("="*45)
            spots_multi = 0
            errors_multi = 0
            multiplion = 123
            multiplion1 = 5
            result_multiplion = 123 * 5
            multiplion2 = 84
            multiplion3 = 2
            result_multiplion1 = 82 * 2
            multiplion4 = 42
            multiplion5 = 2
            result_multiplion2 = 42 * 2
            multiplion6 = 64
            multiplion7 = 2
            result_multiplion3 = 64 * 2
            multiplion8 = 12
            multiplion9 = 4
            result_multiplion4 = 12 * 4
            while True:
                imposi_multi = int(input(f"Quanto é? {multiplion} X {multiplion1}: "))
                if imposi_multi == result_multiplion:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_multi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_multi != result_multiplion:
                    print(f"\033[0;32m Você errou, era {result_multiplion} \033[m ")
                    errors_multi += 1
                    erros += 1
                imposi_multi1 = int(input(f"Quanto é? {multiplion2} X {multiplion3}: "))
                if imposi_multi1 == result_multiplion1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_multi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_multi1 != result_multiplion1:
                    print(f"\033[0;32m Você errou, era {result_multiplion1} \033[m ")
                    errors_multi += 1
                    erros += 1
                imposi_multi2 = int(input(f"Quanto é? {multiplion4} X {multiplion5}: "))
                if imposi_multi2 == result_multiplion2:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_multi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_multi2 != result_multiplion2:
                    print(f"\033[0;32m Você errou, era {result_multiplion2} \033[m ") 
                    errors_multi += 1
                    erros += 1
                imposi_multi3 = int(input(f"Quanto é? {multiplion6} X {multiplion7}: "))
                if imposi_multi3 == result_multiplion3:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_multi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_multi3 != result_multiplion3:
                    print(f"\033[0;32m Você errou, era {result_multiplion3} \033[m ")
                    errors_multi += 1
                    erros += 1
                imposi_multi4 = int(input(f"Quanto é? {multiplion8} X {multiplion9}: "))
                if imposi_multi4 == result_multiplion4:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print(f"\033[0;36m Nivel Impossivel de Multiplicação, acabado \033[m ")
                    spots_multi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_multi4 != result_multiplion4:
                    print(f"\033[0;32m Você errou, era {result_multiplion4} \033[m")
                    print(f"\033[0;32m Nivel Impossivel de Multiplicação, acabado \033[m ")
                    errors_multi += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {spots_multi} \033[m e \033[0;32m errou até agora {errors_multi} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif impossivel == 3:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Impossivel ")
            print("Desafio da Divisão ")
            print("="*45)
            spots_divi = 0
            errors_divi = 0
            imposi_divi = 64
            imposi_divi1 = 2
            result_divi = 64 / 2
            imposi_divi2 = 32
            imposi_divi3 = 2
            result_divi1 = 32 / 2
            imposi_divi4 = 24
            imposi_divi5 = 2
            result_divi2 = 24 / 2
            imposi_divi6 = 46
            imposi_divi7 = 2
            result_divi3 = 46 / 2
            imposi_divi8 = 84
            imposi_divi9 = 4
            result_divi4 = 84 / 4
            while True:
                imposi_divi = int(input(f"Quanto é? {imposi_divi} / {imposi_divi1}: "))
                if imposi_divi == result_divi:
                    print("\033[0;36m Você acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_divi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_divi != result_divi:
                    print(f"\033[0;32m Você errou, era {result_divi} \033[m ")
                    errors_divi += 1
                    erros += 1
                imposi_divi1 = int(input(f"Quanto é? {imposi_divi2} / {imposi_divi3}: "))
                if imposi_divi1 == result_divi1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_divi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_divi1 != result_divi1:
                    print(f"\033[0;32m Vocẽ errou, era {result_divi1} \033[m")
                    errors_divi += 1
                    erros += 1
                imposi_divi2 = int(input(f"Quanto é? {imposi_divi4} / {imposi_divi5}: "))
                if imposi_divi2 == result_divi2:
                    print("\033[0;36m Você acertou ;D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_divi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_divi2 != result_divi2:
                    print(f"\033[0;32m Você errou, era {result_divi2} \033[m ")
                    errors_divi += 1
                    erros += 1
                imposi_divi3 = int(input(f"Quanto é? {imposi_divi6} / {imposi_divi7}: "))
                if imposi_divi3 == result_divi3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_divi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_divi3 != result_divi3:
                    print(f"\033[0;32m Você errou, era {result_divi3} \033[m ")
                    erros_divi += 1
                    erros += 1
                imposi_divi4 = int(input(f"Quanto é? {imposi_divi8} / {imposi_divi9}: "))
                if imposi_divi4 == result_divi4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print(f"\033[0;36m Nivel Impossivel de Divisão, acabado \033[m ")
                    spots_divi += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_divi4 != result_divi4:
                    print(f"\033[0;32m Você errou, era {result_divi4} \033[m ")
                    print(f"\033[0;32m Nivel Impossivel de Divisão, acabado \033[m ")
                    erros_divi += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {spots_divi} \033[m e \033[0;32m errou até agora {errors_divi} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif impossivel == 4:
            print("="*45)
            print(f"Seja bem vindo ao jogo de matemática, {jogador} ")
            print("Nivel: Impossivel ")
            print("Desafio da Raiz Quadrada ")
            print("="*45)
            spots_raiz = 0
            errors_raiz = 0
            radix = 28
            result_radix = 5.29
            radix1 = 63
            result_radix1 = 7.93
            radix2 = 144
            result_radix2 = 12
            radix3 = 784
            result_radix3 = 28
            radix4 = 625
            result_radix4 = 25
            while True:
                imposi_radix = float(input(f"Qual é o resultado dessa raiz? {radix}: "))
                if imposi_radix == result_radix:
                    print("\033[0;36m Vocẽ acertou :D \033[m")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_radix != result_radix:
                    print(f"\033[0;32m Vocẽ errou, era {result_radix} \033[m ")
                    errors_raiz += 1
                    erros += 1
                imposi_radix1 = float(input(f"Qual é o resultado dessa raiz? {radix1}: "))
                if imposi_radix1 == result_radix1:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_radix1 != result_radix1:
                    print(f"\033[0;32m Você errou, era {result_radix1} \033[m ")
                    errors_raiz += 1
                    erros += 1
                imposi_radix2 = float(input(f"Qual é o resultado dessa raiz? {radix2}: "))
                if imposi_radix2 == result_radix2:
                    print("\033[0;36m Vocẽ acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_radix2 != result_radix2:
                    print(f"\033[0;32m Você errou, era {result_radix2} \033[m ")
                    errors_raiz += 1
                    erros += 1
                imposi_radix3 = float(input(f"Qual é o resultado dessa raiz? {radix3}: "))
                if imposi_radix3 == result_radix3:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print("\033[0;36m Passando para nova etapa... \033[m ")
                    spots_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_radix3 != result_radix3:
                    print(f"\033[0;32m Você errou, era {result_radix3} \033[m ")
                    errors_raiz += 1
                    erros += 1
                imposi_radix4 = float(input(f"Qual é o resultado dessa raiz? {radix4}: "))
                if imposi_radix4 == result_radix4:
                    print("\033[0;36m Você acertou :D \033[m ")
                    print(f"\033[0;36m Nivel Impossivel de Raiz quadrada, acabado \033[m ")
                    spots_raiz += 1
                    pontos += 1
                    time.sleep(3)
                elif imposi_radix4 != result_radix4:
                    print(f"\033[0;32m Você errou, era {result_radix4} \033[m ")
                    print(f"\033[0;32m Nivel Impossivel de Raiz quadrada, acabado \033[m ")
                    errors_raiz += 1
                    erros += 1
                print(f"\033[0;36m Você acertou até agora {spots_raiz} \033[m e \033[0;32m errou até agora {errors_raiz} \033[m ")
                print(" Voltando... ")
                time.sleep(3)
                break
        elif impossivel == 5:
            print("Até mais... ")
            exit()
            time.sleep(3)
    elif n == 5:
        print("até mais ")
        exit()