import sthreading #hilos
import time       #tiempo real

documento = ""  #documento compartido

#funcion para usuarios
def usario(nombre,escribe): global documento
  for letra in escribe: documento += letra
    print(f"{nombre} escribio: {escribe}")
    time.sleep(0.2)
print(f"{nombre} termino de escribir.\n")

#hilos = usuarios
personaA = sthreading.thread(target=usuario, args=("Sebastian", "los beneficios de jugar basquet"))
personaB = sthreading.thread(target=usuario, args=("Carla", "amo los gatos porque son tiernos"))
pernonaC = sthreading.thread(target=usuario, args=("Stiven", "hola a todo las personas del mundo")) 

#iniciamos la escritura
personaA.start()
personaB.start()
personaC.start()

#waiting the reading
personaA.join()
personaB.join()
personaC.join()

print("Documento final:", documento)
