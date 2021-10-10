import time
import random
import threading
import queue

queue = queue.Queue(maxsize=5)
filosofos = ['Aristoteles', 'Platon', 'Socrates', 'Karl Marx', 'John Locke']

def turno():
    index = 0
    while index < 5:
        if  not queue.full():
            item = filosofos[index]
            queue.put(item)
            print('Siguiente turno: ', item)
            time_sleep = random.randint(1,3)
            time.sleep(time_sleep)
        index+=1


def finalizar_turno():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            print('Turno finalizado:', item)
            time_sleep = random.randint(1,3)
            time.sleep(time_sleep)

if __name__ == '__main__':
    turno_hilo = threading.Thread(target=turno)
    finalizar_turno_hilo = threading.Thread(target=finalizar_turno)

    turno_hilo.start()
    finalizar_turno_hilo.start()