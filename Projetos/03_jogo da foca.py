import random 

def jogar_focar():
    palavras = ['abacaxi', 'banana', 'laranja', 'uva', 'melancia', 'morango', 'limão']
    palavra = random.choice(palavras)

    letras_erradas = []
    letras_certas = []
    tentativas = 6

    while True:
        if tentativas == 0:
            print(f'Você perdeu! A palavra era {palavra}')
            break

        letra = input('Digite uma letra em minusculo: ').lower()

        if letra in letras_certas or letra in letras_erradas:
            print('Você já tentou essa letra! Tente outra.')
            continue

        if letra in palavra:
            letras_certas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        palavra_escondida = ""
        for letra_palavra in palavra:
            if letra_palavra in letras_certas:
                palavra_escondida += letra_palavra
            else:
                palavra_escondida += '_'

        print(f'Palavra: {palavra_escondida}')
        print(f'Tentativas Restantes: {tentativas}')
        print(f'Letras erradas: {letras_erradas}')

        if '_' not in palavra_escondida:
            print('Parabéns Você venceu!')
            break

jogar_focar()