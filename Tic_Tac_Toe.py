def desenhar_tabuleiro(tabuleiro):
    print('-------------')
    for i in range(3):
        print('|', tabuleiro[i*3], '|', tabuleiro[i*3+1], '|', tabuleiro[i*3+2], '|')
        print('-------------')

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i*3+j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[i+j*3] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i*4] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i*2+2] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha():
    tabuleiro = [' '] * 9
    jogador = 'X'

    while True:
        desenhar_tabuleiro(tabuleiro)

        # Solicita a jogada do usuário
        while True:
            try:
                posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
                if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                    break
                else:
                    print("Posição inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        tabuleiro[posicao] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            desenhar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            break

        if ' ' not in tabuleiro:
            desenhar_tabuleiro(tabuleiro)
            print("Deu velha!")
            break

        jogador = 'O' if jogador == 'X' else 'X'

jogo_da_velha()