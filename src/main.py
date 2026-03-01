import threading
import time

documento = ""  # documento compartido
lock = threading.Lock()  # bloquea para que un hilo escriba a la vez

def usuario(nombre, texto):
    global documento
    for letra in texto:
        with lock:  # asegura que solo un usuario escriba en este momento
            documento += letra
            print(f"{nombre} escribió: {letra}")
        time.sleep(0.2)
    print(f"{nombre} terminó de escribir.\n")

# hilos para cada usuario
personaA = threading.Thread(target=usuario, args=("Sebastian", "me gusta jugar básquet"))
personaB = threading.Thread(target=usuario, args=("Carla", "Amo los gatos"))
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
