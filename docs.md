# Documentación Técnica

## Descripción

El sistema simula múltiples usuarios editando documentos de forma concurrente, utilizando hilos en Python. Se controla el acceso a memoria y recursos compartidos.

---

## Concurrencia

Se implementa con:

- threading.Thread → crea múltiples hilos
- queue.Queue → organiza tareas

Cada hilo representa un usuario que ejecuta tareas en paralelo.

---

## Sincronización

Se utiliza:

- threading.Lock()

Protege:
- Acceso a memoria (RAM)
- Escritura en documentos
- Registro en el log

Evita condiciones de carrera.

---

##  Gestión de Memoria

Se simula RAM con:

- RAM_TOTAL → memoria disponible
- ram_usada → memoria actual
- memoria_letra → consumo por operación
- espera_memoria → procesos en espera
- ram_maxima → pico de uso

### Funcionamiento:

1. El hilo intenta usar memoria
2. Si hay → ejecuta
3. Si no → espera
4. Luego libera memoria

---

## Métricas

El sistema calcula:

- RAM máxima usada
- Usuario que más RAM consumió
- Usuario que generó el pico de memoria
- Eventos de espera

---

## Almacenamiento

Se utilizan archivos:

- run.log → registro de ejecución
- doc1.txt, doc2.txt, doc3.txt → documentos finales

También se usan funciones del sistema operativo:

- os.open
- os.write
- os.close

---

## Log del sistema

Formato:

usuario,documento,evento,RAM

Ejemplo:

Sebastian,doc1,letra=H,RAM=1.5

---

## Conclusión

El sistema implementa:

- Concurrencia real
- Sincronización con exclusión mutua
- Simulación de memoria
- Uso de archivos como evidencia

Cada ejecución puede generar un orden diferente.
El documento final contiene la combinación de todo lo escrito por los usuarios.

## Conclusión

El proyecto demuestra el comportamiento de la concurrencia en Python y cómo múltiples hilos pueden interactuar con un recurso compartido.
