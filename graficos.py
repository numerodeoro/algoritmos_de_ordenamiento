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
    #revisar el código de la gráfica d las listas casi ordenadas
    df_filtrado = df[df['Tipo de lista'] == tipo_lista]

    if tipo_lista == "Aleatoria":
        categorias_unicas = df_filtrado["Categorías o Proporción desorden"].unique()

        for cant_cat in categorias_unicas:
            sub_df = df_filtrado[df_filtrado["Categorías o Proporción desorden"] == cant_cat]

            plt.figure(figsize=(12, 7))
            sns.set(style="whitegrid", palette="colorblind", font_scale=1.2)

            ax = sns.lineplot(
                data=sub_df,
                x="Longitud",
                y="Tiempo",
                hue="Algoritmo",
                marker="o",
                linewidth=2.2
            )

            titulo = f"Aleatoria - {cant_cat} categorías"
            ax.set_title(titulo, fontsize=16, weight='bold')
            ax.set_xlabel("Longitud de lista", fontsize=13)
            ax.set_ylabel("Tiempo (segundos)", fontsize=13)
            ax.legend(title="Algoritmo", title_fontsize=12, fontsize=11)

            plt.tight_layout()

            # Crear nombre de archivo único
            nombre_archivo = f"tiempo_vs_longitud_aleatoria_{cant_cat}_categorias.png"
            output_path = os.path.join("graficos", nombre_archivo)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            plt.savefig(output_path)
            plt.close()

    else:
        plt.figure(figsize=(12, 7))
        sns.set(style="whitegrid", palette="colorblind", font_scale=1.2)

        ax = sns.lineplot(
            data=df_filtrado,
            x="Longitud",
            y="Tiempo",
            hue="Algoritmo",
            marker="o",
            linewidth=2.2
        )

        titulo = f"Tiempo por longitud de lista - {tipo_lista}"
        ax.set_title(titulo, fontsize=16, weight='bold')
        ax.set_xlabel("Longitud de lista", fontsize=13)
        ax.set_ylabel("Tiempo (segundos)", fontsize=13)
        ax.legend(title="Algoritmo", title_fontsize=12, fontsize=11)

        plt.tight_layout()

        nombre_archivo = f"tiempo_vs_longitud_{tipo_lista.replace(' ', '_').lower()}.png"
        output_path = os.path.join("graficos", nombre_archivo)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
        plt.close()
for tipo_lista in ["Aleatoria", "Casi Ordenada"]:
    graficar_por_tipo(df, tipo_lista)