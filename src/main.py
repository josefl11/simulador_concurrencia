import threading # hilos de usuarios
import time # tiempo real de escritura

documento = ""  # documento compartido
lock=threading.Lock() # asegura que un solo hilo se ejecute en el momento dado
def usuario(nombre, texto):
    global documento
    for letra in texto:
        with lock:
            documento += letra
            print(f"{nombre} escribió: {letra}")
        time.sleep(0.2)
    print(f"\n'{nombre} terminó de escribir'.\n")

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
