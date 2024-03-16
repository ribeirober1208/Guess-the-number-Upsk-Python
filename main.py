import random, unittest

def advinhe_o_numero(intervalo):
    return random.randint(intervalo[0], intervalo[1])

def main():
    numero_secreto = random.randint(1, 100)
    tentativas_jogador = []
    tentativas_computador = []
    jogador = input("Olá! Qual o seu nome: ")
    contagem_tentativas = 0
    intervalo = [1, 100]

    while True:
        contagem_tentativas += 1
        
        tentativa_jogador = int(input("Adivinhe o número (entre 1 e 100): "))
        tentativas_jogador.append(tentativa_jogador)
        
        if tentativa_jogador == numero_secreto:
            print(f"Parabéns, {jogador}! Você venceu!!! Acertou o número secreto em {contagem_tentativas} tentativas.")
            print("Suas tentativas foram:", tentativas_jogador)
            print()
            break
            
        elif tentativa_jogador < numero_secreto:
            print(f"Ops! {jogador}, tente um número maior.")
            intervalo[0] = max(intervalo[0], tentativa_jogador + 1)
        else:
            print(f"Ops! {jogador}, tente um número menor.")
            intervalo[1] = min(intervalo[1], tentativa_jogador - 1)
        
        print()
        
        if tentativas_computador:
            if tentativas_computador[-1] < numero_secreto:
                intervalo[0] = tentativas_computador[-1] + 1
            else:
                intervalo[1] = tentativas_computador[-1] - 1
        
        aposta = advinhe_o_numero(intervalo)
        tentativas_computador.append(aposta)
        
        if aposta == numero_secreto:
            print(f"O computador acertou o número secreto em {contagem_tentativas} tentativas.")
            print("Tentativas do computador:", tentativas_computador)
            print()
            break
            
        elif aposta < numero_secreto:
            print(f"O computador fez sua aposta {aposta}, tente um número maior.")
        else:
            print(f"O computador fez sua aposta {aposta}, tente um número menor.")
        print()

if __name__ == '__main__':
    main()

