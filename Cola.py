import multiprocessing
from multiprocessing import Process, Queue, Lock
import time
import random
# Para mas información sobre multiprocessing: https://docs.python.org/3/library/multiprocessing.html
# Para mas información sobre Queue: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.queues

# Este código implementa un sistema de productores y consumidores utilizando multiprocessing en Python.
# Los productores generan números enteros aleatorios y los almacenan en una cola compartida.    
# Los consumidores extraen números de la cola y los procesan (en este caso, simplemente los imprimen).
# La cola tiene una capacidad máxima, lo que significa que los productores esperarán si la cola
# está llena, y los consumidores esperarán si la cola está vacía.

def productor(id_productor, cola, max_intentos=None):
    """
    Proceso productor que intenta infinitamente almacenar números enteros en la cola.
    """
    intento = 0
    while max_intentos is None or intento < max_intentos:
        numero = random.randint(1, 100)
        try:
            # put() espera automáticamente si la cola está llena
            cola.put(numero, timeout=2)
            print(f"Productor {id_productor}: Almacenó el número {numero}")
            time.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            print(f"Productor {id_productor}: Error al almacenar - {e}")
        intento += 1

def consumidor(id_consumidor, cola, max_intentos=None):
    """
    Proceso consumidor que intenta infinitamente extraer valores de la cola.
    """
    intento = 0
    while max_intentos is None or intento < max_intentos:
        try:
            # get() espera automáticamente si la cola está vacía
            numero = cola.get(timeout=2)
            print(f"Consumidor {id_consumidor}: Extrajo el número {numero}")
            time.sleep(random.uniform(0.5, 2))
        except Exception as e:
            print(f"Consumidor {id_consumidor}: Error al extraer - {e}")
        intento += 1

def main():
    """
    Función principal que orquesta productores y consumidores.
    """
    # Crear una cola con capacidad máxima
    tamaño_cola = 5
    cola = Queue(maxsize=tamaño_cola)
    
    num_productores = 5
    num_consumidores = 5
    
    # Crear lista de procesos
    procesos = []
    
    # Crear procesos productores
    for i in range(num_productores):
        p = Process(target=productor, args=(i, cola, 10))  # max_intentos para limitar la ejecución
        procesos.append(p)
        p.start()
    
    # Crear procesos consumidores
    for i in range(num_consumidores):
        c = Process(target=consumidor, args=(i, cola, 10))  # max_intentos para limitar la ejecución
        procesos.append(c)
        c.start()
    
    # Esperar a que terminen todos los procesos
    for proceso in procesos:
        proceso.join()
    
    print("\nTodos los procesos han finalizado.")

if __name__ == "__main__":
    main()