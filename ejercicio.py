import threading
import time

capacidad = 10
buffer = [-1 for i in range(capacidad)]
in_index = 0
out_index = 0
mutex = threading.Semaphore()
vacio= threading.Semaphore(capacidad)
lleno= threading.Semaphore(0)

#Clase Productor
class Productor(threading.Thread):
    
    def run(self):
        global capacidad
        global in_index
        global out_index
        global buffer
        global mutex
        global vacio
        global lleno
        items_producidos = 0
        contador=0

        while True:
            vacio.acquire()
            mutex.acquire()
            contador += 1
            buffer[in_index] = contador
            in_index = (in_index + 1) % capacidad
            print("Productor", self.name, "produjo:", in_index)
            
            mutex.release()
            lleno.release()
            time.sleep(1)
            items_producidos += 1