
import multiprocessing
import time
import random

sem_pista = None
sem_equipes = None

def init(pista, equipes):
    global sem_pista
    global sem_equipes

    sem_pista = pista
    sem_equipes = equipes

def carro(dados):
    global sem_pista
    global sem_equipes

    equipe = dados[0]
    numero = dados[1]

    with sem_equipes[equipe - 1]:
        with sem_pista:
            carro_correndo(equipe, numero)


def carro_correndo(equipe, numero):
    volta = 0
    tempo = 0.0

    for volta in range(1, 4):
        tempo = random.uniform(1, 3)
        time.sleep(tempo)

        print(
            'Equipe #', equipe,
            'Carro #', numero,
            'Volta #', volta,
            'Tempo:', round(tempo, 2), 'segundos'
        )

    print('Equipe #', equipe, 'Carro #', numero, 'saiu da pista')

def main():
    parametros = [0] * 14
    i = 0
    j = 0

    for i in range(1, 8, 1):
        for j in range(1, 3, 1):
            parametros[(i - 1) * 2 + (j - 1)] = (i, j)

    with multiprocessing.Manager() as gerenciador:

        sem_pista = gerenciador.Semaphore(5)

        sem_equipes = [None] * 7

        for i in range(0, 7, 1):
            sem_equipes[i] = gerenciador.Semaphore(1)

        with multiprocessing.Pool(
            processes=14,
            initializer=init,
            initargs=(sem_pista, sem_equipes)
        ) as pool:
            pool.map(carro, parametros)

if __name__ == '__main__':
    main()
