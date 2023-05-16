from ejercicio import *
if __name__ == '__main__':
    productor = Productor()
    consumidor = Consumidor()
    productor.start()
    consumidor.start()
    productor.join()
    consumidor.join()