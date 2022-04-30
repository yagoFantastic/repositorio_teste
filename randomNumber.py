#(OBS): Criar um mensurador de quantas tentativas levou para descobrir um numero randomico
#1° crie um input para receber os numeros do usuario
#2° crie um loop para verificar a acertividades dos numeros 
#3° import o metodo random para gerar o numero mas atenção fora do loop
#4° diga se o numero esta perto ou longe de acordo com o numero randomico e o digitado pelo usuario
#5° retorne quantos vezes o usuario tentou acertar o numero e nao conseguio

import random
numero_random = random.randint(1,10)

confirmacao = input('Quer Tentar bater a maquina Digite [Sim] ou [Nao]: ').upper()

numero_tentativas = 0
while confirmacao == "SIM":
    numero_usuario = int(input('Digite um numero entre 1 e 10 e veja se consegue bater a maquina: '))

    if(numero_usuario < numero_random and numero_random != numero_usuario):
        print(f'Errou seu numero é MENOR!')
        numero_tentativas +=1
    elif(numero_usuario > numero_random and numero_random != numero_usuario):
        print(f'Errou seu numero é MAIOR!')
        numero_tentativas +=1
    else:
        print(f'Acertou {numero_random} e seu numero {numero_usuario}')
        numero_tentativas +=1    
    confirmacao = input('Quer Tentar bater a maquina Digite [Sim] ou [Nao]: ').upper()
print(f'Voce realizou {numero_tentativas} tentativas para acerta o numero {numero_random}')       