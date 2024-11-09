from random import randint  # Esta Linha serve para importar a biblioteca Random, que irá ser chamada posteriormente para utilizar o Randint

print('#### Iníciando Jogo ####') # Esta Linha irá imprimir no console tudo que estiver dentro dos parenteses e aspas simples. Resultado: #### Iníciando Jogo ####

random = randint(0, 100) #  Esta Linha da a instrução para o Randint aleatorizar um número de 0, a 100
chute = 0; # Esta linha armazena o número 0 na variavel chute
chances = 10; # Esta linha armazena o número 01 na variavel chances
while chute != random: # Esta linha da a instrução ao laço de repetição que enquanto o chute (Que é o número que o jogador irá informar posteriormente) for diferente do Número aleatório que a maquina gerou a repetição deve continuar
    chute = input('Chute um número entre 0 a 100: ') #  Esta linha faz com que a variavel chute receba um numero que o jogador digitar no console
    if chute.isnumeric(): # Esta linha verifica se o numero que o jogador informou é um numero
        chute = int(chute) # Esta linha transforma o valor string que o jogador informou e o converte em um numero inteiro (Quando se digita um numero no console atraves da instrução input o valor informado sempre se torna uma string, por isso é nescessario esta conversão)
        chances = chances - 1 # Esta linha serve para diminuir uma das 10 chances que o jogador tem (Agora ficando com 9)
        if chute == random: # Esta linha verifica se chute é igual ao numero que a Maquina gerou
            print('') # Esta linha serve para dar uma quebra de linha no console
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances)) # Esta linha irá imprimir no console tudo que estiver dentro das aspas simples. Resultado: Parabéns, você venceu! O número era X e você ainda tinha X chances. sendo o que está após as aspas é a instrução do que será inserido nas duas {} (Chaves)
            print('') # Esta linha Esta linha serve para dar uma quebra de linha no console
            break; # Esta linha para a repetição do While
        else: # Esta linha informa o que será executado caso a verificação do If for Falsa
            print('') # Esta linha serve para dar uma quebra de linha no console
            if chute > random: # Esta linha verifica se chute é maior que random
                print('Você errou!!! Dica: É um número menor.') # Esta linha irá imprimir no console tudo que estiver dentro dos parenteses e aspas simples. Resultado: Você errou!!! Dica: É um número menor.
            else: # Esta linha informa o que será executado caso a verificação do If for Falsa
                print('Você errou!!! Dica: É um número maior.') # Esta linha irá imprimir no console tudo que estiver dentro dos parenteses e aspas simples. Resultado: Você errou!!! Dica: É um número maior.
            print('Você ainda possui {} chances.'.format(chances)) # Esta linha Esta linha irá imprimir no console tudo que estiver dentro das aspas simples. Resultado: Você ainda possui X chances. sendo o que está após as aspas é a instrução do que será inserido na {} (Chave)
            print('') # Esta linha Esta linha serve para dar uma quebra de linha no console
        if chances == 0: # Esta linha verifica se as chances são iguais ao numero 0
            print('') # Esta linha Esta linha serve para dar uma quebra de linha no console
            print('Suas chances acabaram, você perdeu!') # Esta linha irá imprimir no console tudo que estiver dentro dos parenteses e aspas simples. Resultado: Suas chances acabaram, você perdeu!
            print('') # Esta linha Esta linha serve para dar uma quebra de linha no console
            break; # Esta linha para a repetição do While

print('#### Fim do Jogo ####') # Esta Linha irá imprimir no console tudo que estiver dentro dos parenteses e aspas simples. Resultado: #### Fim do Jogo ####