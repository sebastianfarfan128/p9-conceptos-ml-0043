# Sebastian Farfan NC = 0043
import pandas as pd

# 1. Crear el dataset de ejemplo del hospital
datos_hospital = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 23, 60, 35, 50],
    'nivel_glucosa': [148, 85, 183, 89, 137],
    'presion_arterial': [72, 66, 64, 60, 40],
    'indice_masa_corporal': [33.6, 26.6, 23.3, 28.1, 43.1],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]  # 1: Positivo, 0: Negativo
}

df_hospital = pd.DataFrame(datos_hospital)

# 2. Separar las Features (X) eliminando el 'id_paciente'
# Usamos .drop() para quitar la columna id_paciente y el Target
X = df_hospital.drop(columns=['id_paciente', 'diagnostico_diabetes'])

# 3. Separar la Variable Objetivo (y)
y = df_hospital['diagnostico_diabetes']

# 4. Mostrar la estructura resultante
print("--- DATOS COMPLETOS DEL HOSPITAL ---")
print(df_hospital)

print("\n--- FEATURES / ENTRADAS (X) [Sin id_paciente] ---")
print(X)

print("\n--- TARGET / SALIDA (y) ---")
print(y)

print("Elaborado por Sebastian Farfan NC = 0043")