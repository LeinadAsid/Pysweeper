import random
import time

def count_bombas(campo, x, y):
    '''Conta o numero de bombas ao redor de uma posição
    matriz, int, int -> int'''

    Ncol = len(campo)
    Nlin = len(campo[0])

    N_bombas = 0
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            x_neibor = x + i
            y_neibor = y + j

            if (x_neibor >= 0 and x_neibor < Ncol and
                y_neibor >= 0 and y_neibor < Nlin):
        
                if (campo[x_neibor][y_neibor] == "m"):
                    N_bombas = N_bombas + 1
                
                    
    return N_bombas

def gerar_campo(N_bombas, x, y):
    '''Gera uma matriz que representa o campo com as bombas aleatoriamente espalhadas
    int(N° de bombas), int(Ncol), int(Nlin) -> matriz'''
    
    random.seed(time.time())
    
    board = [[0 for i in range(x)] for j in range(y)]

    while N_bombas > 0:
        Xbom = random.randint(0, x - 1)
        Ybom = random.randint(0, y - 1)

        if ( board[Xbom][Ybom] == "m" ):
            pass
        else:
            board[Xbom][Ybom] = "m"
            N_bombas = N_bombas - 1
        
    return board

def draw(campo):
    '''desenha o campo na tela'''
    nCol = len(campo)
    nLin = len(campo[0])
    
    for linha in campo:
        for i in range(nLin):
            print(str(linha[i]) + " ", end = '')

        print("")


def mostraBombas(campoR, campoE):
    '''Ao perder revela todas as casas escondidas
    matriz, matriz -> None'''
    nCol = len(campoR)
    nLin = len(campoR[0])

    for i in range(nCol):
        for j in range(nLin):
            if (campoR[i][j] == 'm'):
                campoE[i][j] = 'm'
            else:
                campoE[i][j] = count_bombas(campoR, i, j)
                

    return

def main():
    '''Loop principal'''
    
    campoEscondido = [['*' for i in range(10)] for j in range(10)] # gera matriz 9 por 9 com valores "*"
    
    campoRevelado = gerar_campo(10,10,10) # gera campo.
    
    q = True
    perdeu = False
    
    print('Bem vindo ao campo minado!\n')
        
    while q:
        
        draw(campoEscondido)
        
        p_q = input("\nContinuar (*) ou desistir (d) do jogo? ")
        if ( p_q == "*" and perdeu == False):
            
            posicao = input("\nSelecione uma casa para revela-la (ex. 0 1) -> coluna 0 linha 1: ") 
            XY = posicao.split(' ')
            x = int(XY[0])
            y = int(XY[1])
            
            if (campoRevelado[x][y] != 'm' and campoEscondido[x][y] == '*'):
                campoEscondido[x][y] = count_bombas(campoRevelado, x, y)

            elif (campoEscondido[x][y] != '*'):
                print("\nPosição invalida! campo já descoberto.")

            else:
                mostraBombas(campoRevelado, campoEscondido)
                campoEscondido[x][y] = "M"
                perdeu = True
                print("\nVocê perdeu. Tente novamente!\n")
                
        elif(p_q == "d"):
            print("\nObrigado por jogar!")
            return

        elif(p_q == "*" and perdeu == True):
            campoEscondido = [['*' for i in range(10)] for j in range(10)]
            campoRevelado = gerar_campo(10,10,10)
            perdeu = False
            
        else:
            print("\nInput invalido tente novamente")
            pass

        
if __name__ == '__main__':
   main()
