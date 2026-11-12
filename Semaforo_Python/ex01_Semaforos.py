
import multiprocessing
import time

sentido = None
semaforo = None

def init(s, sem):
    global sentido
    global semaforo

    sentido = s
    semaforo = sem


def carro(id, direcao):
    global sentido
    global semaforo

    with semaforo:
        sentido.value = direcao

        if sentido.value == 1:
            print('Carro #', id, 'passando no sentido Norte')

        elif sentido.value == 2:
            print('Carro #', id, 'passando no sentido Sul')

        elif sentido.value == 3:
            print('Carro #', id, 'passando no sentido Leste')

        elif sentido.value == 4:
            print('Carro #', id, 'passando no sentido Oeste')

        time.sleep(2)

        print('Carro #', id, 'saiu do cruzamento')

def main():
    parametros = [0] * 4
    i = 0

    estado = multiprocessing.Value('i', 0)

    parametros[0] = (1, 1)
    parametros[1] = (2, 2)
    parametros[2] = (3, 3)
    parametros[3] = (4, 4)

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)

        with multiprocessing.Pool(
            processes=4,
            initializer=init,
            initargs=(estado, sem)
        ) as pool:
            pool.starmap(carro, parametros)

if __name__ == '__main__':
    main()

