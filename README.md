# Algoritmos Genéticos

Un algoritmo genético (GA) es un método de optimización inspirado en el proceso de selección natural. Es utilizado para encontrar soluciones aproximadas a problemas complejos mediante la evaluación de una población de posibles soluciones.

> [!TIP]
> Los conceptos a continuación se podrían traducir a la forma en la cómo los pájaros construyen sus nidos, hay unos que los hacen en ramas altas y otros en ramas bajas del árbol. Aquellos pájaros que hacen su nido en zonas más seguras, tendrán más crías, y esas crías heredarán esas habilidades de sus padres. Con el tiempo, los pájaros aprenderán a construir nidos en mejores lugares.

## Población

En los GA se trabaja con una población de individuos, donde cada individuo representa una posible solución al problema. Estos individuos se codifican típicamente como cadenas de genes, que podrían ser secuencias binarias, números o cualquier otra representación que describa la solución al problema.

## Función de evaluación (Fitness)

Cada individuo es evaluado usando una función de evaluación o función de fitness. Esta función mide qué tan buena es la solución que representa ese individuo en resolver el problema. Cuando mayor sea el valor de fitness, mejor es la solución.


## Selección (Selection)

En la fase de selección, los individuos con un fitness más alto tienen una mayor probabilidad de ser seleccionados para reproducirse y formar la próxima generación. Este proceso emula la supervicencia del más apto.

## Mutación (Mutation)

La mutación introduce variaciones aleatorias en los genes de un individuo. Esto ayuda a mantener la diversidad genética dentro de la población y evita que el algoritmo se estanque en soluciones subóptimas.

## Iteración y evolución

El proceso de selección, cruce y mutación se repite varias generaciones. Con cada generación, la población deberá acercarse a una solución óptima del problema.



