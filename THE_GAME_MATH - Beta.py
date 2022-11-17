def sim():
    print('')
    print('Então vamos lá')
    print('')


def sair():
    print('Tchal, até a próxima')
    exit()


def analfabeto_s_n():
    global opcao
    print('Você é analfabeto? Responda com s ou n')
    opcao = input('Vamos jogar agora? (s/n) ')
    print('')


def questao(n, pergunta, rc):
    global resposta
    print('')
    print('Questão ', n, ':')
    resposta = input(pergunta)
    print('')
    resultado(rc, resposta, n)


def resultado(rc, ru, n):
    global nota
    if ru == 'adm1020':
        exit()

    if ru == rc:
        print('Parabéns, Você acertou')
        print('')
        print('A resposta era ', rc)
        print('')
        nota = nota + 1
        print('Você acertou ', nota, '/10 questões deste quiz')
        print('')
        if n != 10:
            print('Próxima Questão...')

    else:
        print('Que Pena, Você Errou')
        print('')
        print('A resposta correta era ', rc)
        print('')
        print('Você acertou ', nota, '/10 questões deste quiz')
        print('')
        if n != 10:
            print('Próxima Questão...')


nota = 0
resposta = 0
x = 1

print('Seja Bem-Vindo ao THE GAME MATH')
print('')

while x == 1:

    nick = input('Qual seu Nickname? ')
    print('')
    print('Olá', nick, 'tenha um ótimo jogo')
    print('BOA SORTE!!!')
    print('')
    opcao = input('Vamos jogar agora? (s/n) ')

    while opcao != 's' and opcao != 'n':
        analfabeto_s_n()

    if opcao == 'n':
        sair()

    if opcao == 's':
        sim()

    questao(1, 'Quanto é 50 x 4? ', '200')

    questao(2, 'Quanto é 50/3? ', '16,6')

    questao(3, 'Quanto é 10x40? ', '400')

    questao(4, 'Quanto é 30 elevado a 2? ', '900')

    questao(5, 'Quanto é 40/10? ', '4')

    questao(6, 'Quanto é 20e3? ', '8000')

    questao(7, 'Quanto é 70/4? ', '17,5')

    questao(8, 'Quanto é 500/4? ', '125')

    questao(9, 'Quanto é 5000x3? ', '15000')

    questao(10, 'Quanto é 20-5x10+500? ', '470')

    opcao = input('Deseja jogar mais uma partida? (s/n) ')

    while opcao != 's' and opcao != 'n':
        analfabeto_s_n()

    if opcao == 'n':
        sair()

    if opcao == 's':
        sim()
