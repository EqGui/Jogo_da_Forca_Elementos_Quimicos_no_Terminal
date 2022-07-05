from random import randint
from tkinter import *
cont = certo = erro = certo_novo = 0
lista = ('Hidrogenio', 'Helio', 'Litio', 'Berilio', 'Boro', 'Carbono', 'Nitrogenio', 'Oxigenio', 'Fluor', 'Neonio', 'Sodio', 'Magnesio', 'Aluminio',
'Silicio', 'Fosforo', 'Enxofre', 'Cloro', 'Argonio', 'Potassio', 'Calcio', 'Escandio', 'Titanio', 'Vanadio', 'Cromio', 'Manganes', 'Ferro',
'Cobalto', 'Niquel', 'Cobre', 'Zinco', 'Galio', 'Germanio', 'Arsenio', 'Selenio', 'Bromo', 'Criptonio', 'Rubidio', 'Estroncio', 'Itrio',
'Zirconio', 'Niobio', 'Molibdenio', 'Tecnecio', 'Rutenio', 'Rodio', 'Paladio', 'Prata', 'Cadmio', 'Indio', 'Estanho', 'Antimonio', 'Telurio',
'Iodo', 'Xenonio', 'Cesio', 'Bario', 'Lutecio', 'Hafnio', 'Tantalo', 'Tungstenio', 'Renio', 'Osmio', 'Iridio', 'Platina', 'Ouro', 'Mercurio',
'Talio', 'Chumbo', 'Bismuto', 'Polonio', 'Astato', 'Radonio', 'Francio', 'Radio')
sorteio = randint(0, 73)
elemento = lista[sorteio].upper()
resposta = elemento.replace(elemento,'_' * len(elemento))
print('='*80)
print('Bem-vindo ao jogo da forca de Elementos Químicos!')
print('='*80)
print(f'Pensei em um Elemento Químico de {len(elemento)} letras. Tente adivinhar!')
print(f'Situação Atual: {resposta}')
while True:
    cont += 1
    print('-'*80)
    letra = str(input(f'Qual a {cont}ª letra: ')).upper()
    for c in range (0, len(elemento)):
        if elemento[c] == letra:
            resposta = resposta[:c] + letra + resposta[c+1:]
            certo_novo = certo + 1
    if certo_novo == certo:
        erro += 1
    certo = certo_novo
    print(f'Você acertou {certo} letras. Ainda faltam {len(elemento) - certo} letras para completar o Elemento Químico.')
    print('='*80)
    print(f'Situação Atual: {resposta.upper()}')
    if erro == 0:
        print('Nenhum erro!')
    elif erro == 1:
        print('''       |_|
Você já tem a cabeça da forca (1 erro)''')
    elif erro == 2:
        print('''       |_|
        |
        |
Você já tem a cabeça e o tronco da forca (2 erros)''')
    elif erro == 3:
        print('''       |_|
      .º|º.
        |
Você já tem a cabeça, o tronco e os braços da forca (3 erros)''')
    elif erro == 4:
        print('''       |_|
      .º|º.
        |
      .º º. 
Você já tem a cabeça, o tronco, os braços e as pernas da forca (4 erros)''')
    elif erro == 5:
        print(f'''      _|_|__/
      .º|º.
        |
      .º º.
ENFORCADO! (5 erros). O jogo acabou e você perdeu!
O Elemento Químico era: {elemento.upper()}''')
        break
    if certo == len(elemento):
        print('=' * 80)
        print(f'Parabéns, você ganhou! Foram utilizadas {cont} letras e você errou {erro} vezes. Elemento Químico: {elemento.upper()}')
        break
    else:
        chute = str(input('Você quer chutar o Elemento Químico? [Enter para pular] ')).upper()
        while len(chute) < 4 and chute not in 'Nn':
            chute = str(input('Você quer chutar o Elemento Químico? [Enter para pular] ')).upper()
        if chute == elemento:
            print('='*80)
            print(f'Parabéns, você ganhou! Foram utilizadas {cont} letra e você errou {erro} vezes.' )
            break
        if chute != elemento and chute not in 'Nn':
            print(f'Errou! O Elemento Químico era: {elemento.upper()}')
            break