# Sebastian Farfan NC = 0043
import pandas as pd
print(pd.__version__) # Output: 1.5.2
# 1. Crear un dataset de ejemplo simular a un CSV
datos18 = {
    'distancia_km': [4.5, 2.0, 5.2, 1.7, 3.1],
    'trafico_nivel': [3, 1, 2, 3, 2],
    'edad_repartidor': [37, 26, 40, 24, 33],
    'tiempo_entrega_min': [44, 14, 40, 19, 24]
}

df = pd.DataFrame(datos18)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Elaborado por Sebastian Farfan NC = 0043")