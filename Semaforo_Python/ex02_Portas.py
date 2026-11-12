
import multiprocessing
import time
import random

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def pessoa(id):
    global semaforo

    velocidade = random.randint(4, 6)
    tempo_caminhada = 200 / velocidade

    print('Pessoa #', id, 'começou a caminhar.')
    print('Pessoa #', id, 'velocidade:', velocidade, 'm/s')

    time.sleep(tempo_caminhada)

    print('Pessoa #', id, 'chegou à porta.')

    with semaforo:
        atravessar_porta(id)


def atravessar_porta(id):
    tempo_rand = random.randint(1000, 2000)
    tempo_porta = tempo_rand / 1000

    print('Pessoa #', id, 'está abrindo e atravessando a porta.')

    time.sleep(tempo_porta)

    print('Pessoa #', id, 'atravessou a porta em',
          tempo_porta, 'segundos.')

def main():
    parametros = [0] * 4
    i = 0

    for i in range(0, 4, 1):
        parametros[i] = i + 1

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)

        with multiprocessing.Pool(
            processes=4,
            initializer=init,
            initargs=(sem,)
        ) as pool:
            pool.map(pessoa, parametros)

if __name__ == '__main__':
    main()
