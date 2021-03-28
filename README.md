# Calculadora.py
Repositório de projetos que eu programei, para ajudar iniciantes em python

Repositório para ajudar iniciantes, essa calculadora tem 12 opções, foi programa em python3, com a biblioteca math que ajudou e a datetime para colocar o time.sleep
para dá um realismo no programa.

Tem as conversões de octal, hexadecimal e binario, com o código que já tem no python que é de oct, hex e bin, que já vem no python, foi bem fácil programar essa parte
já que não foi preciso fazer muito esforço, era só colocar oct, hex e bin. Não teve nenhuma dificuldade.

Perguntas: 

Porque foi colocada em um while?

O while eu poderia ter colocado o True, para rodar infinitamente, ao menos a pessoa colocar a opção 12 que é de saída, e também servia para que se o usuario quisesse voltar
ele poderia voltar, não precisaria ficar escrevendo códigos e códigos infinitamente, tudo é mais fácil no python, se vocês verem no meu outro repositório ou outros que eu soltarei
vocês perceberão que eu não vou usar um while != 12, e sim um while True, para rodar infinitamente só se a pessoa apertar o número que é a tecla de sair, que para o programa
fora isso, ele vai rodar infinitamente. While é muito bom pra isso, é bem útil.

Porque não usei o for?

O for ele é usado quando você sabe o valor, até quando vai, como eu não sabia que o usuario queria tantas vezes usar o programa, usei o while. Exemplo:
Eu quero um programa que conte de 0 a 10, então eu uso o for, porque eu sei o que a pessoa quer, e até quando termina e etc.
Mas quando eu não sei quantas vezes a pessoa quer utilizar, ou até quando vai, eu usei o while. Os dois são laços de repetição. Eu prefiro mais o while do que o for.


Para que serve o if, elif e else?

O elif no python é "mais se", exemplo:
Eu estou no supermercado e estou com cartão de cŕedito, débito e dinheiro, a compra deu R$900 e o programa da caixa que eles fazem tem os metodos de pagamentos, como:
você pode comprar em dinheiro, débito e crédito. Minha compra deu R$900, então começa assim:

if pagamento == débito:

      print("Ok, escolha confirmada")
      
elif pagamento == cŕedito:

      print("Ok, escolha confirmada")
else:

      print("Ok, escolha confirmada")

em português fica:

se pagamento for igual a débito:

     print("ok, escolha confirmada")
     
mais se pagamento for igual a crédito:

     print("ok, escolha confirmada")
     
se não:

     print("ok, escolha confirmada")

Então o elif é usado para mais de uma opção.
