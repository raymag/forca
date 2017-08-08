#Sendo o objetivo do programa simular um jogo da forca,
#Primeiramente importamos a biblioteca Random, nativa do python
#Assim podemos trabalhar com números e escolhas aleatórias
import random

#Aqui, declaramos algumas váriaveis fundamentais para o nosso código
#Lista de palavras iniciais (Default)
palavras = ['abacate','chocolate','paralelepipedo','goiaba']
#Nossos erros e acertos, ainda vazios
letrasErradas = ''
letrasCertas = ''
#E aqui declaramos uma lista que porta os 'estados de forca' do programa
FORCAIMG = ['''

 
  +---+
  |   |0
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Aqui definimos uma função que irá nos pedir palavras e adicionalas à nossa lista anterior.
def Insert():
    print('''
Insira palavras...
Quando desejar parar, por favor,
tecle enter sem digitar nenhum
caractere.''')
    while True:
        q = input('Informe: ')
        #Caso  o usuário não digite nenhum caractere e pressionar o enter, a função prosseguirá com o código
        if q == '':
            break
        palavras.append(q)
        q = 'Palavra adicionada com sucesso'

#Aqui definimos a função principal do programa, ela é o cerne de nosso código
def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    #Invocamos à nossa função insert aqui, e esta irá nos requisitar palavras
    Insert()
    #A variável palavraSecreta carregará a função sortearPalavra
    palavraSecreta = sortearPalavra()
    #Aqui definimos a variável palpite à qual nos será útil em breve
    palpite = ''
    #Invocamos a função desenhaJogo passando as nossas variáveis como parâmetros
    desenhaJogo(palavraSecreta,palpite)


    #Aqui criamos um loop que irá verificar se o usuário perdeu ou ganhou o jogo
    while True:
        # A variável palpite irá receber o resultado da função receberPalpite(), esta irá nos permitir tentar um palpite
        palpite = receberPalpite()
        # Aqui invocamos a função desenhaJogo, passando com parâmetros a palavraSecreta e o palpite, esta irá coordenar toda a parte gráfica do programa
        desenhaJogo(palavraSecreta,palpite)
        #Aqui verificamos se o jogador ganhou o perdeu o jogo, em ambos os casos, o nosso loop será quebrado
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            

#Esta função irá informar se o jogador perdeu ou não o jogo; Usando valores booleanos no processo
def perdeuJogo():
    global FORCAIMG #Usando o comando global, ligamos a variável FORCAIMG local com as anteriores
    if len(letrasErradas) == len(FORCAIMG): #Verifica se o número de letras erradas é igual a quantidade de elementos da lista FORCAIMG, caso sim, retorna o valor booleano True
        return True
    else: #Caso a afirmação anterior seja falsa, o valor retornado também será Falso
        return False


def ganhouJogo(palavraSecreta): #Esta função confere se o jogador ganhou o jogo
    global letrasCertas #Primeiramente ele liga a variável letrasCertas
    ganhou = True #Declara a  variável ganhou com o valor True
    #Se cada letra na PalavraSecreta estiver dentro da lista letrasCertas, o ganhou continuará como Verdadeiro, caso contrário, tornará-se Falso
    for letra in palavraSecreta:  
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        


def receberPalpite(): #Esta função permite o jogador a fazer palpites das letras corretas
    
    palpite = input("Adivinhe uma letra: ") #primeiro o programa faz a requisição de uma informação ao usuário
    palpite = palpite.upper() #E este, torna todas as letras da informação maiúsculas
    if len(palpite) != 1: #Caso o jogador informe mais de um caractere por vez, o programa irá imprimir a seguinte frase
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: #E caso, o palpite esteja dentro de letrasCertas ou de letrasErradas, o programa
        #Informará que o jogador já disse esta letra
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": #Caso o jogador informe algo além de letras, o programa irá requisitar apenas letras
        print('Por favor escolha apenas letras')
    else: #Caso, todas as afirmações e condições anteriores sejam falsas, a função irá  retornar a variável palpite
        return palpite
    

def desenhaJogo(palavraSecreta,palpite): #Como já informado, esta função coordena a parte gráfica do jogo
    #Inicialmente fazemos referências à variáveis já decladas
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #E aqui imprimos o elemento de FORCAIMG que é equivalente ao número de letras erradas até o momento
    
     
    vazio = len(palavraSecreta)*'-' #Esta string terá o mesmo número de caracteres que a palavra secreta, sendo formada apenas por '_'
    
    if palpite in palavraSecreta: #Caso o palpite esteja dentro da palavraSecreta, isto irá adicionar o palpite dentro de letrasCertas
        letrasCertas += palpite
    else: #Caso contrário, irá adicionar o palpite às letrasErradas
        letrasErradas += palpite

    #Este bloco irá trocar os espaços vazios (__) pelas letras acertadas
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]

    #Este bloco irá imprimir as letras acertadas e erradas para o jogador, como também a variável vazio
    print('Acertos: ',letrasCertas ) 
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra(): #Esta é a função que escolhe uma palavra aleatória da lista de palavras e as torna maiúsculas
    global palavras
    return random.choice(palavras).upper()

    
principal() #Aqui invocamos a nossa função principal, pode-se dizer que é o comando inicial de todo o nosso código
