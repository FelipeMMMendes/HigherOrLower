from data import data as df
from art import logo,vs
from random import randint

#temos 50 registros em nossos dados
#we have 50 registers in our data

#funcao para checar qual dos temas eh mais popular
#function to check which one is the most popular between the options
def checkValue(option1,option2):
    if option1['follower_count']>option2['follower_count']:
        #se a opcao 1 tiver mais relevancia, a funcao retorna true
        #if option 1 is more relevant, the function returns true
        return True
    else:
        #se a opcao 2 tiver mais relevancia, a funcao retorna false
        #if option 2 is more relevant, the function returns true
        return False    

#gera numeros aleatorios para determinar qual os temas
#get two random numbers to determine which will be the options of choice
index1 = randint(0,49)
index2 = randint(0,49)

choice1 = df[index1]
choice2 = df[index2]

#lista pra armazenar as posicoes que já foram escolhidas
#list to keep the positions that have already been picked
chosenAlready = []

#variavel flag para repeticao do jogo
#flag variable to the repetition of the game
gameIsOn = True


print(logo)

while gameIsOn:
    #imprime o painel de jogo, exibindo as duas opcoes e o VS (de versus)
    #print the main panel of the game, showing the two options and the VS (from versus)
    print(choice1['name'] + " (A)")
    print(vs)
    print(choice2['name'] + " (B)")

    #recebendo a escolha do jogador e determinando se ele acertou ou nao
    #getting the player's choice and determining if it's correct or no
    playerChoice = input("Which one has more followers? Type 'A' or 'B' ")

    #deixa a resposta minuscula
    #lower the answer
    playerChoice = playerChoice.lower()

    #se a funcao checkValue retornar true (significa que a opcao1 eh maior que a 2) 
    #e o jogador escolheu A, ele passou.

    #if the checkValue function returns true (it means that option1 is bigger than option 2) 
    #and the player has chosen A, meaning he pass to the next round.
    if checkValue(choice1,choice2)==True and playerChoice == 'a':
        print(f"You're right! {choice1['name']} has over {choice1['follower_count']} million followers")
        print(f"While {choice2['name']} has over {choice2['follower_count']} million followers")

        #adiciona o numero do primeiro para o chosenAlready e faz com que a opcao2 receba outro tema
        #add the number of the first to the chosenAlready and make the second option recieve another data
        chosenAlready.append(index1)
        choice1 = choice2
        index2 = randint(0,49)
        choice2 = df[index2]

    #mesma logica de antes, só que agora esse laço condicional vai ser ativado caso a opção 2 seja a maior
    #e o jogador tenha acertado

    #same logic as before, but now in this case it's for when the option 2 is bigger than 1 and the player
    #got that right.
    elif checkValue(choice1,choice2)==False and playerChoice == 'b':
        print(f"You're right! {choice2['name']} has over {choice2['follower_count']} million followers")
        print(f"While {choice1['name']} has over {choice1['follower_count']} million followers")
        chosenAlready.append(index1)
        choice1 = choice2
        index2 = randint(0,49)
        choice2 = df[index2]

    #caso o jogador tenha errado
    #if the player had got it wrong.
    else:
        print(f"You're wrong! {choice1['name']} has over {choice1['follower_count']} million followers")
        print(f"While {choice2['name']} has over {choice2['follower_count']} million followers")
        gameIsOn = False







