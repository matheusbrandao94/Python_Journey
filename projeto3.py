import random
import math
menor = int(input("Menor Número: "))
maior = int(input("Maior Número: "))

x = random.randint(menor,maior)
cont = 5
while cont > 0:
    resposta = int(input("Chute um Número: "))
    if resposta == x:
        print("Parabéns Você Ganhou")
        print(f"O Valor de x é: {x}")
        break
    elif x < resposta:
        print("O Número é Muito Alto")
    elif x > resposta:
        print("O Número é Muito Baixo")
    cont -=1

if cont == 0:
    print("Você Perdeu")
    print(f"O Valor de x é: {x}")

  