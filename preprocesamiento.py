import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Creamos unos datos de prueba (simulando un archivo Excel/CSV)
datos_prueba = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Ana', None],
    'Edad': [25, 30, 35, 25, 40],
    'Ciudad': ['Quito', 'Guayaquil', 'Cuenca', 'Quito', 'Guayaquil']
}
df = pd.DataFrame(datos_prueba)

print("--- DATOS ORIGINALES ---")
print(df)

# 2. Eliminar duplicados (La fila de Ana repetida se borrará)
df = df.drop_duplicates()

# 3. Manejar valores nulos (El 'None' se cambiará por 'Desconocido')
df['Nombre'] = df['Nombre'].fillna('Desconocido')

# 4. Normalizar variables numéricas (La Edad se pondrá en una escala estándar)
scaler = StandardScaler()
df[['Edad']] = scaler.fit_transform(df[['Edad']])

# 5. Codificar variables categóricas (Las ciudades se volverán números: 0, 1, 2)
encoder = LabelEncoder()
df['Ciudad_Codificada'] = encoder.fit_transform(df['Ciudad'])

print("\n--- DATOS PREPROCESADOS ---")
print(df)