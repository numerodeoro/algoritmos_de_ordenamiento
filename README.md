# <img width="60" height="60" alt="image" src="https://github.com/user-attachments/assets/bce9f021-e7c5-40c4-8077-3a525c7c0c81" />        Comparación de Algoritmos de Ordenamiento

Este proyecto tiene como objetivo evaluar el desempeño de distintos algoritmos de ordenamiento sobre listas de diferentes características. Se diseñó un sistema de testing automatizado que permite comparar los tiempos de ejecución en función del tamaño de las listas, el grado de desorden y la cantidad de categorías posibles en sus elementos.
Nació con la idea de repasar algoritmos de ordenamientos ya existentes y terminó desembocando en algunas variantes propias de los ordenamientos (*catSort*, inspirando en el counting aunque con varios cambios y *pivotear*, casi calcado del quick sort, pero con cambio de pivote y ligeramente distinta metodología en la partición) y en el desarrollo de un tester personalizado de los algoritmos.

## 📂 Estructura del Proyecto
├── algoritmos/

│   ├── __init__.py

│   ├── bubble.py

│   ├── catSort_flat.py

│   ├── catSort_table.py

│   ├── dividir_unir.py

│   ├── insertion.py

│   ├── pivoteo.py

│   └── selection.py

├── utils/

│   ├── __init__.py

│   └── generador_listas.py

├── resultados/

│   ├── resultados_tester.csv

│   └── otros archivos .csv

├── tests/

│   ├── __init__.py

│   └── tester.py

├── tester.py

├── resultados.csv

├── README.md

└── .gitignore



## ⚙️ Algoritmos Incluidos

- `bubble()` (burbuja)
- `ordenar()` (inserción)
- `selec_sort()` (selección)
- `pivotear()` (versión del quick sort con pivote personalizado)
- `dividir_unir()` (versión del merge sort)
- `catSort_flat()` (ordenamiento optimizado para listas con pocas categorías, versión muy libre del counting sort, ver el README de ordenamientos catSort)

## 🧪 Funcionalidad del Tester

El script `tester.py` genera combinaciones de listas con diferentes parámetros y mide el tiempo de ejecución de cada algoritmo sobre ellas.  
Las listas pueden ser:
- **Aleatorias**: con una cantidad limitada de categorías posibles.
- **Casi ordenadas**: con cierto porcentaje de elementos desordenados.

Parámetros configurables:
- Longitudes de las listas mínima y máxima (desde 10,000 hasta 1,000,000 por defecto)
- Variación incremental en la longitud (por defecto es 495000)
- Porcentaje de desorden mínimo y máximo (por defecto desde 0.1 hasta 0.7)
- variación incremental del porcentaje de desorden (por defecto es 0.3)
- Cantidad de categorías mínima y máxima (por defecto, 5 y 25)
- variación incremental en la cantidad de categorías (por defecto es 10)
- Semilla para garantizar reproducibilidad (por defecto es seed=100)

### 🧮 Formato del CSV generado

El archivo `resultados_tester.csv` incluye las siguientes columnas:

- `Semilla`
- `Algoritmo`
- `Tipo de lista` (`Aleatoria` o `Casi ordenada`)
- `Longitud`
- `Categorías o Proporción desorden`
- `Tiempo` (en segundos)

## 🚀 Cómo ejecutar el tester
* Puede ejecutarse un *test de performance* para un solo algoritmo y lista con la función **test_eficiencia(algoritmo,lista)**
* También (recomendable), puede ejecutarse un *banco completo de pruebas* con distintos tipos de listas con la función **tester()**, esta última tiene argumentos personalizables para generar listas diferentes, pero se puede usar con valores configurados por defecto, todos los argumentos son opcionales para mayor facilidad de uso. Esto generará un archivo "resultados_tester.csv", con todos los tiempos registrados.

### ⚠️ Nota:
para ciertos algoritmos no óptimos o listas muy largas, los tiempos de ejecución pueden ser elevados. Se recomienda probar primero con listas pequeñas si se agregan nuevos algoritmos.

## 📈 Próximos pasos
### Análisis comparativo de resultados (gráficos)

### Mejora de la eficiencia en algoritmos propios

### Inclusión de pruebas estadísticas (varianza, distribución de tiempos)

### Interfaz visual para ejecución del tester

## 🧠 Observaciones
El algoritmo catSort_flat() mostró un rendimiento notable cuando se trabaja con listas de baja cardinalidad (pocas categorías).

sorted() de Python sirve como línea de base, pero los algoritmos personalizados permiten experimentar y entender el comportamiento con distintos tipos de entrada.

Desarrollado por:
María Marta Torres
Con ayuda de ideas, sueños de ordenamientos y testers cinematográficos 😄
