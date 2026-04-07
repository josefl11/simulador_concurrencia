# Simulador de Edición Concurrente de Documentos

## Descripción

Este proyecto simula la edición concurrente de múltiples documentos utilizando hilos en Python. Se implementa control de acceso a recursos compartidos, simulación de memoria RAM y generación de evidencia mediante archivos.

## Objetivo

Demostrar conceptos de sistemas operativos como concurrencia, sincronización y gestión de memoria en un entorno controlado.

## Tecnologías

- Python 3
- threading
- queue
- os

## Funcionalidades

- Ejecución concurrente con múltiples hilos (workers)
- Sincronización mediante Lock
- Simulación de memoria RAM:
  - RAM total
  - Consumo por operación
  - Espera por falta de memoria
- Registro de eventos en archivo (run.log)
- Generación de documentos finales (doc1.txt, doc2.txt, doc3.txt)
- Métricas:
  - RAM máxima utilizada
  - Usuario con mayor consumo de RAM
  - Usuario que generó el pico de RAM
  - Eventos de espera por memoria

## Ejecución

Ejecutar el archivo principal:


## Evidencia generada

- run.log → Registro de ejecución
- doc1.txt, doc2.txt, doc3.txt → Documentos generados

## Conceptos aplicados

### Concurrencia
Uso de múltiples hilos ejecutándose en paralelo.

### Sincronización
Uso de Lock para evitar condiciones de carrera.

### Memoria (Unidad 2)
Simulación de gestión de memoria RAM con control de acceso y espera.

### Sistema de archivos
Uso de llamadas al sistema (os.open, os.write) para generar logs.

## Conclusión

El proyecto demuestra cómo múltiples procesos pueden interactuar sobre recursos compartidos, controlando acceso, memoria y generando evidencia de ejecución.
