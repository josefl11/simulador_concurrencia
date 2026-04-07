# Documentación Técnica

## Descripción

El sistema simula múltiples usuarios editando documentos de forma concurrente mediante el uso de hilos en Python.  
Además, incorpora control de memoria simulada y registro de ejecución para evidenciar el comportamiento del sistema.

---

## Concurrencia

La concurrencia se implementa utilizando:

- threading.Thread: creación de múltiples hilos (usuarios)
- queue.Queue: gestión de tareas pendientes

Cada hilo representa un usuario que obtiene tareas desde la cola y escribe en documentos compartidos de manera simultánea.
Debido a esto, el contenido final puede aparecer mezclado, lo cual evidencia ejecución concurrente real.

---

## Sincronización

Se utiliza un mecanismo de exclusión mutua:
- threading.Lock()

Este protege:
- Acceso a la memoria (RAM simulada)
- Escritura en documentos compartidos
- Registro en el archivo de log

Su uso evita condiciones de carrera y garantiza consistencia en los datos.

---

## Gestión de Memoria (Unidad 2)

Se simula el uso de memoria RAM mediante las siguientes variables:
- RAM_TOTAL: memoria total disponible
- ram_usada: memoria actualmente utilizada
- memoria_letra: consumo por cada operación (letra)
- espera_memoria: número de veces que un proceso espera
- ram_maxima: máximo uso alcanzado

### Funcionamiento

1. El hilo solicita memoria antes de escribir
2. Si hay suficiente memoria ejecuta la operación
3. Si no hay memoria entra en espera
4. Después de escribir libera la memoria utilizada

---

## Interpretación del uso de RAM

Durante la ejecución se registran valores como:

RAM=4.5

Esto indica cuántos hilos estaban activos simultáneamente:
- 1.5 MB: 1 hilo
- 3.0 MB: 2 hilos
- 4.5 MB: 3 hilos

Un valor alto de RAM indica mayor nivel de concurrencia.

---

## Métricas del sistema

El sistema calcula y muestra:
- RAM máxima utilizada
- Usuario que más RAM consumió
- Usuario que generó el mayor pico de memoria
- Número de eventos de espera por memoria

Estas métricas permiten analizar el rendimiento del sistema.

---

## Almacenamiento

Se generan archivos como evidencia de ejecución:
- run.log: registro detallado del sistema
- doc1.txt, doc2.txt, doc3.txt: documentos finales

También se utilizan funciones del sistema operativo:
- os.open
- os.write
- os.close

Esto simula interacción directa con el sistema operativo.

---

## Log del sistema

El archivo run.log registra los eventos en el siguiente formato:
usuario,documento,evento,RAM

Ejemplo:
Sebastian,doc1,letra=H,RAM=1.5

Incluye:
- Inicio de procesos
- Escritura de letras
- Uso de memoria
- Finalización

---

## Comportamiento del sistema

- Los documentos pueden contener texto mezclado debido a la concurrencia
- El orden de ejecución cambia en cada corrida
- La memoria limita la ejecución simultánea de procesos
- El sistema refleja un entorno real de múltiples procesos compitiendo por recursos

---

## Conclusión

El sistema cumple contiene:
- Concurrencia real demostrable  
- Sincronización mediante exclusión mutua  
- Integración con gestión de memoria 
- Evidencia mediante archivos (log y documentos)  

Además, permite observar de forma práctica cómo múltiples procesos interactúan con recursos compartidos en un entorno controlado.
