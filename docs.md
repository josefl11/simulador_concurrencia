# Documentación – Simulador de Documento Compartido en tiempo real

## Objetivo
Simular la edición concurrente de un documento compartido utilizando hilos en el lenguaje Python.
Demostrar cómo varios usuarios pueden escribir al mismo tiempo sobre un mismo recurso compartido.

## Descripción del funcionamiento
El programa crea una variable global llamada documento, la cual sera nuestro archivo compartido.
Cada usuario editor del documento se representa por un hilo (threading.Thread).

Cada hilo ejecuta la función usuario(nombre, texto), que:

Recorre el texto letra por letra.

Agrega cada letra al documento compartido.

Muestra en pantalla qué usuario escribió cada letra.

Simula tiempo real usando time.sleep().

Debido a que los hilos se ejecutan de manera concurrente, el texto final puede aparecer mezclado.

⚙️ Tecnologías utilizadas

Python 3

Módulo threading

Módulo time

## Conceptos aplicados
Hilos (Threads)

Permiten ejecutar múltiples tareas de forma simultánea dentro de un mismo programa.

Recurso compartido

La variable documento es utilizada por todos los hilos.

Concurrencia

Los hilos se ejecutan al mismo tiempo, lo que provoca que el orden de escritura no sea predecible.

Condición de carrera

Ocurre cuando varios hilos acceden y modifican un mismo recurso sin sincronización.

## Resultados

El programa muestra cómo el texto se mezcla debido a la concurrencia.

Cada ejecución puede generar un orden diferente.

El documento final contiene la combinación de todo lo escrito por los usuarios.

## Conclusión

El proyecto demuestra el comportamiento de la concurrencia en Python y cómo múltiples hilos pueden interactuar con un recurso compartido.
