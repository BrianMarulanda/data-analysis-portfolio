# 🧹 Limpieza y Normalización de Datos de Usuario (Store 1)

Este proyecto se enfoca en la fase de **Data Wrangling** y preprocesamiento de una base de datos de clientes de Store 1. El objetivo fue transformar datos crudos e inconsistentes en un dataset estructurado, garantizando la integridad de la información para futuros análisis estadísticos.

## 📋 Descripción del Dataset
Los datos originales presentaban inconsistencias en nombres, tipos de datos erróneos y problemas potenciales con entradas de texto en campos numéricos. Las columnas analizadas incluyen:
- `user_id`: Identificador único.
- `user_name`: Nombre y apellido (con espacios y caracteres especiales).
- `user_age`: Edad (en formato float).
- `fav_categories`: Categorías de compra.
- `total_spendings`: Gastos por categoría.

## 🛠️ Procesos Técnicos Realizados
- **Normalización de Texto:** Se implementaron los métodos `.strip()` y `.replace()` para eliminar espacios redundantes y guiones bajos en los nombres de usuario.
- **Validación de Tipos de Datos:** Conversión manual de la columna de edad de `float` a `int` para asegurar la coherencia del modelo.
- **Robustez del Código:** Implementación de bloques `try-except` para capturar errores de entrada cuando la edad no era un valor numérico, evitando la interrupción del flujo de ejecución.
- **Estructuración de Listas:** Segmentación de cadenas de texto en sublistas (Nombre/Apellido) mediante el método `.split()`.
- **Agregación de Datos:** Uso de la función `sum()` para calcular el gasto total consolidado por cada cliente.

## 🚀 Conclusiones
A través de este proceso se logró:
1. Reducir el ruido en los datos de texto en un 100%.
2. Estandarizar el formato de las variables numéricas.
3. Preparar una lista limpia (`users_clean`) lista para ser convertida a un DataFrame de Pandas o cargada en una base de datos SQL.

---
**Archivo principal:** `Sprint 1 DA 56 Brian Marulanda.ipynb`
