import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

nombre_archivo = "resultados_tester_semilla320_20250723_151213.csv"
ruta_archivo = os.path.join(".", "resultados", nombre_archivo)
# probar con distintos separadores y encodings si no abre bien, el sniffer.csv no se lleva bien con pandas
df = pd.read_csv(ruta_archivo, encoding='latin1', sep = ",")
df["Longitud"] = pd.to_numeric(df["Longitud"], errors="coerce")
df["Tiempo"] = pd.to_numeric(df["Tiempo"], errors="coerce")

print(df.head())

sns.set(style="whitegrid", palette="muted", font_scale=1.2)

df_filtrado = df[df['Tipo de lista'] == "Lista ordenada"].copy().reset_index(drop=True)

        
# plt.figure(figsize=(12, 7))
# sns.set(style="whitegrid", palette="colorblind", font_scale=1.2)

# ax = sns.scatterplot(
# data=df_filtrado,
# x="Longitud",
# y="Tiempo",
# hue="Algoritmo",
# marker="o",
# linewidth=2.2
#         )

# titulo = "Tiempo por longitud de lista - Lista ordenada"
# ax.set_title(titulo, fontsize=16, weight='bold')
# ax.set_xlabel("Longitud de lista", fontsize=13)
# ax.set_ylabel("Tiempo (segundos)", fontsize=13)
# ax.legend(title="Algoritmo", title_fontsize=12, fontsize=11)

# ax.set_xlim(df_filtrado["Longitud"].min(), df_filtrado["Longitud"].max())
# ax.set_ylim(df_filtrado["Tiempo"].min(), df_filtrado["Tiempo"].max())

# plt.tight_layout()

# nombre_archivo = f"tiempo_vs_longitud_Lista_ordenada.png"
# output_path = os.path.join("graficos", nombre_archivo)
# os.makedirs(os.path.dirname(output_path), exist_ok=True)

# plt.savefig(output_path)
# plt.close()
print(df_filtrado["Longitud"].min(), df_filtrado["Longitud"].max())
print(df_filtrado["Tiempo"].min(), df_filtrado["Tiempo"].max())
df_filtrado["Longitud"].head()