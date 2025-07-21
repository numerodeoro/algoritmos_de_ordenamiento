# Comparación de Algoritmos de Ordenamiento

Este proyecto tiene como objetivo evaluar el desempeño de distintos algoritmos de ordenamiento sobre listas de diferentes características. Se implementó un sistema de testing automatizado que permite comparar los tiempos de ejecución en función del tamaño de las listas, el grado de desorden y la cantidad de categorías posibles en sus elementos.

## 📂 Estructura del Proyecto
├── algoritmos/

│   ├── bubble.py

│   ├── insertion.py

│   ├── selection.py

│   ├── pivoteo.py

│   └── catSort_flat.py

├── utils/

│   └── generador_listas.py

├── tests/

│   └── tester.py

├── README.md

└── .gitignore


## ⚙️ Algoritmos Incluidos

- `sorted()` de Python (referencia base)
- `bubble()` (burbuja)
- `ordenar()` (inserción)
- `selec_sort()` (selección)
- `pivotear()` (propio, basado en un pivote)
- `catSort_flat()` (ordenamiento optimizado para listas con pocas categorías)

## 🧪 Funcionalidad del Tester

El script `tester.py` genera combinaciones de listas con diferentes parámetros y mide el tiempo de ejecución de cada algoritmo sobre ellas.  
Las listas pueden ser:
- **Aleatorias**: con una cantidad limitada de categorías posibles.
- **Casi ordenadas**: con cierto porcentaje de elementos desordenados.

Parámetros configurables:
- Longitudes de las listas (desde 10,000 hasta 1,000,000)
- Porcentaje de desorden (por ejemplo, 0.1, 0.4, 0.7)
- Cantidad de categorías (por ejemplo, 5, 25)
- Semilla para garantizar reproducibilidad

### 🧮 Formato del CSV generado

El archivo `resultados_tester.csv` incluye las siguientes columnas:

- `Semilla`
- `Algoritmo`
- `Tipo de lista` (`Aleatoria` o `Casi ordenada`)
- `Longitud`
- `Categorías o Proporción desorden`
- `Tiempo` (en segundos)

## 🚀 Cómo ejecutar el tester

```bash
python tester.py

Esto generará un archivo resultados_tester.csv con todos los tiempos registrados.

## ⚠️ Nota:

para ciertos algoritmos no óptimos o listas muy largas, los tiempos de ejecución pueden ser elevados. Se recomienda probar primero con listas pequeñas si se agregan nuevos algoritmos.

📈 Próximos pasos
Análisis comparativo de resultados (gráficos)

Mejora de la eficiencia en algoritmos propios

Inclusión de pruebas estadísticas (varianza, distribución de tiempos)

Interfaz visual para ejecución del tester

🧠 Observaciones
El algoritmo catSort_flat() mostró un rendimiento notable cuando se trabaja con listas de baja cardinalidad (pocas categorías).

sorted() de Python sirve como línea de base, pero los algoritmos personalizados permiten experimentar y entender el comportamiento con distintos tipos de entrada.

Desarrollado por:
María Marta Torres
Con ayuda de ideas, sueños con Fourier y testers cinematográficos 😄
