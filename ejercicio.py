import threading
import time

capacidad = 10
buffer = [-1 for i in range(capacidad)]
in_index = 0
out_index = 0
mutex = threading.Semaphore()
vacio= threading.Semaphore(capacidad)
lleno= threading.Semaphore(0)
