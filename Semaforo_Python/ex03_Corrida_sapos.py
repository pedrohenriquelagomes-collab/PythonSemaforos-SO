
import multiprocessing
import random
import time

sem = None
posicao = None

def init(s, p):
    global sem
    global posicao

    sem = s
    posicao = p

def sapo(id):
    global sem
    global posicao

    distancia = 0
    pulo_maximo = random.randint(1, 5)

    print(f"Sapo {id} começou a corrida!")

    while distancia < 20:
        salto = random.randint(0, pulo_maximo)
        distancia += salto

        print(f"Sapo {id}: pulou {salto} cm | Percorreu {distancia} cm")

        time.sleep(0.3)

    with sem:
        posicao.value += 1
        colocacao = posicao.value

        print(f"Sapo {id} chegou em {colocacao}º lugar!")

def main():
    params = [1, 2, 3, 4, 5]

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        colocacao = manager.Value('i', 0)

        with multiprocessing.Pool(
            processes=5,
            initializer=init,
            initargs=(semaforo, colocacao)
        ) as pool:
            pool.map(sapo, params)

if __name__ == "__main__":
    main()
