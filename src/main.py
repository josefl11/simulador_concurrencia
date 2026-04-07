import threading
import time
import queue
import os

#CONFIGURACION:
RAM_TOTAL = 100 # MB
ram_usada = 0
memoria_letra = 1.5
espera_memoria = 0
ram_maxima = 0
uso_ram_usuario = {}

#DOCUMENTOS:
documentos = {
    "doc1": "",
    "doc2": "",
    "doc3": ""
}

#COLA:
cola = queue.Queue()

cola.put(("Sebastian", "Hola, bienvenidos a mi blog", "doc1"))
cola.put(("Carolina", "Ajuste financiero ", "doc1"))
cola.put(("Pablo", "Las consecuencias del cambio climatico en el mundo", "doc2"))
cola.put(("Alejandro", "Apuntes esenciales algebra: ", "doc3"))

#LOCK:
lock = threading.Lock()

#LOG:
fd = os.open("run.log", os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o644)

def log(mensaje):
    os.write(fd, (mensaje + "\n").encode())

#WORKER
def worker(nombre_hilo):
    global ram_usada, espera_memoria, ram_maxima

    while True:
        try:
            nombre, texto, doc = cola.get_nowait()
        except queue.Empty:
            return

        for letra in texto:

            #CONTROL DE MEMORIA
            while True:
                with lock:
                    if ram_usada + memoria_letra <= RAM_TOTAL:
                        ram_usada += memoria_letra
                        ram_maxima = max(ram_maxima, ram_usada)
                        
                        #REGISTRAR USO DE RAM POR USUARIO
                        uso_ram_usuario[nombre] = uso_ram_usuario.get(nombre, 0) + memoria_letra
                        break
                    else:
                        espera_memoria += 1

                time.sleep(0.05)

            #SECCION CRITICA
            with lock:
                documentos[doc] += letra
                print(f"[{nombre_hilo}] {nombre} escribió '{letra}' en {doc}")
                log(f"{nombre},{doc},letra={letra},RAM={ram_usada}")

            time.sleep(0.1)

            #LIBERAR MEMORIA
            with lock:
                ram_usada -= memoria_letra

        print(f"{nombre} terminó en {doc}")
        cola.task_done()

#HILOS:
WORKERS = 3

hilos = [
    threading.Thread(target=worker, args=(f"T{i+1}",))
    for i in range(WORKERS)
]

for l in hilos:
    l.start()

for l in hilos:
    l.join()

#RESULTADOS:
os.close(fd)

print("\n------ RESULTADO FINAL ------")
for doc, contenido in documentos.items():
    print(f"{doc}: {contenido}")

print("\n--- CONTENIDO DEL LOG ---")
with open("run.log", "r") as f:
    print(f.read())

print("\n--- CONFIGURACIÓN ---")
print(f"RAM TOTAL: {RAM_TOTAL} MB")
print(f"Memoria por letra: {memoria_letra} MB")
print(f"Workers: {WORKERS}")
print(f"RAM máxima usada: {ram_maxima}")
if uso_ram_usuario:
    usuario_top = max(uso_ram_usuario, key=uso_ram_usuario.get)
    print(f"Usuario que mas RAM utilizo: {usuario_top}({uso_ram_usuario[usuario_top]}MB)")
print(f"Eventos de espera por memoria: {espera_memoria}")

if espera_memoria > 0:
    print("Hubo procesos en espera por falta de memoria")
else:
    print("No hubo espera por memoria")

open("run.log", "w").close()

#GUARDAR ARCHIVOS:
for doc, contenido in documentos.items():
    with open(f"{doc}.txt", "w") as f:
        f.write(contenido)

#GUARDAR ARCHIVOS:
for doc, contenido in documentos.items():
    with open(f"{doc}.txt", "w") as f:
        f.write(contenido)
