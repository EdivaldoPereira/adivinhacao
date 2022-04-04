print ("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print ("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
else:
    if(maior):
        print("Você errou! Seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você error! Seu chute foi menor que o número secreto.")

print("Fim de jogo")