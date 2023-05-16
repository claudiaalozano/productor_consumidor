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

        while items_producidos < 20:
            vacio.acquire()
            mutex.acquire()
            contador += 1
            buffer[in_index] = contador
            in_index = (in_index + 1) % capacidad
            print("Productor produjo:", contador)
            
            mutex.release()
            lleno.release()
            time.sleep(1)
            items_producidos += 1

#Clase Consumidor
class Consumidor(threading.Thread):
        
        def run(self):
            global capacidad
            global in_index
            global out_index
            global buffer
            global mutex
            global vacio
            global lleno
            items_consumidos = 0
            
    
            while items_consumidos < 20:
                lleno.acquire()
                mutex.acquire()
                item = buffer[out_index]

                
                out_index = (out_index + 1) % capacidad
                print("Consumidor consumio:", item)
                
                mutex.release()
                vacio.release()
                time.sleep(2.5)
                items_consumidos += 1