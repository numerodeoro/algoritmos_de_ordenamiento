import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

nombre_archivo = "resultados_tester_semilla320_20250723_151213.csv"
ruta_archivo = os.path.join(".", "resultados", nombre_archivo)
# probar con distintos separadores y encodings si no abre bien, el sniffer.csv no se lleva bien con pandas
df = pd.read_csv(ruta_archivo, encoding='latin1', sep = ",")

print(df.head())

sns.set(style="whitegrid", palette="muted", font_scale=1.2)

def graficar_por_tipo(df, tipo_lista):
    df_filtrado = df[df['Tipo de lista'] == tipo_lista]
    titulo = "Tiempo por longitud de lista en listas "+ tipo_lista
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_filtrado, x="Longitud", y="Tiempo", hue="Algoritmo")
    plt.title(titulo)
    plt.ylabel("Tiempo (segundos)")
    plt.xlabel("Longitud de lista")
    output_path = os.path.join("graficos", "tiempo_vs_longitud.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()


for tipo_lista in ["Aleatoria", "Casi Ordenada"]:
    graficar_por_tipo(df, tipo_lista)