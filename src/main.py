import threading #hilos de usuarios-concurrencia
import time #tiempo real de escritura
import queue #cola de tareas-organizacion de procesos
import so #interaccion con el sistema operativo 

#configuracion de memoria_______________________
RAM_TOTAL = 60 #mb megabytes
ram_usada = 0 #memoria actual de uso
memoria_letra = 2 #consumo por cada operacion
espera_memoria = 0 #proceso en espera
ram_maxima = 0 #maximo uso alcanzado

#documentos compartidos__________________________
documento = {
    "doc1":"", "doc2":"", "doc3":""
}

#cola de tareas__________________________________
cola = queue.Queue()
#guarda tareas pendoentes 
cola.put(("Sebastian", "Hola, bienvenidos a mi block", "doc1"))
cola.put(("Carolina", "Ajuste financieron 04/04/2027", "doc1"))
cola.put(("Pablo", "Las consecuencias del cambio\n climatico en el mundo", "doc2"))
cola.put(("Alejandro", "Apuntes ensenciales para\nsaber todo sobre base de datos", "doc3"))

lock=threading.Lock() # asegura que un solo hilo se ejecute en el momento dado

#log a nivel del sistema operativo______________
fd = os.pen("run.log", os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o644) #simulan multiples paginas

#worker es quien ejecutara los hilos____________
def worker(nombre_hilo):
    nombre, texto, doc = cola.get_nowait()
    if ram_usada + memoria_letra <=  RAM_TOTAL: #decide si se puede ejecutar
        espera_men += 1 #cuenta bloqueos
        with lock:
            documentos[lock] = letra #solo un hilo podra escribir a la vez
        time.sleep(0.4)

# hilos para cada usuario
personaA = threading.Thread(target=usuario, args=("Sebastian", "Me gusta jugar básquet"))
personaB = threading.Thread(target=usuario, args=("Carla", "Amo a los gatos"))
personaC = threading.Thread(target=usuario, args=("Stiven", "Hola para todos"))

# iniciamos los hilos
personaA.start()
personaB.start()
personaC.start()

# esperamos a que terminen
personaA.join()
personaB.join()
personaC.join()

print("\nDocumento final:", documento)

# enlace: https://onlinegdb.com/ASg2AHEJT
