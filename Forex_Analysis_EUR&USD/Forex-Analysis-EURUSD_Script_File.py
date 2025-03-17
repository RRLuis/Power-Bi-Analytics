import os
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
warnings.filterwarnings('ignore')

#****************************************
# 1) Descarga datos de los últimos 2 años

end_date = datetime.now()
start_date = end_date - timedelta(days=2*365)
ticker = "EURUSD=X"

# Descarga datos de Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Crea el directorio si no existe
os.makedirs("data", exist_ok=True)

# 2) Guardar datos crudos (table Power Bi)
data.to_csv("data/raw_eur_usd_data.csv", sep=",", decimal=".")

# 4) Manejo de missing values
data = data.dropna()

# 5) Asegurar formato fecha
data.reset_index(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])

# 6) Agregar media móvil de 7 días
data['7d_ma'] = data['Close'].rolling(window=7).mean()

# 7) Copia del DataFrame con índice de fecha
df_copy = data.set_index('Date').copy()

# Guardar datos procesados (en formato parquet and csv)
df_copy.to_parquet("data/processed_eur_usd_data.parquet")
df_copy.to_csv("data/processed_eur_usd_data.csv", sep=",", decimal=".")

#****************************************
# 2) EDA y Transformación Logarítmica

# Cargar datos procesados desde archivo parquet
data = pd.read_parquet("data/processed_eur_usd_data.parquet")
data.head(5)

# Deshacer el multi-índice de columnas, manteniendo el ultimo nivel
data.columns = data.columns.get_level_values(0)
data.columns.name = None

# Crear columna logarítmica de la tasa de cierre
data['Close_log'] = np.log(data['Close'])

# Guardar los datos con la transformación logarítmica (Para tablero Power Bi)
data.to_csv("data/processed_eur_usd_data_with_log.csv", sep=",", decimal=".")

# a) Crear histogramas de distribución
fig, axes = plt.subplots(1, 2, figsize=(12,5))
sns.histplot(data['Close'], ax=axes[0], kde=True)
axes[0].set_title("Distribución de la tasa de cambio (Original)")
sns.histplot(data['Close_log'], ax=axes[1], kde=True, color='orange')
axes[1].set_title("Distribución de la tasa de cambio (Log)")
plt.tight_layout()
plt.show()

# Resumen de estadísticas originales vs transformadas
stats_original = data['Close'].describe()
stats_log = data['Close_log'].describe()
print("Estadísticas Originales:\n", stats_original)
print("\nEstadísticas Logarítmicas:\n", stats_log)

# Agregar columna de año-mes
data['year_month'] = data.index.to_period('M')
monthly_avg = data.groupby('year_month')['Close'].mean()
print("Promedio mensual:\n", monthly_avg)

# Eliminar duplicados
data = data[~data.index.duplicated(keep='last')]

#****************************************
#3) Modelado: Regresión para Predecir Tasas Futuras

# Crear features rezagadas (lag features)
df_model = data[['Close_log']].copy()
df_model['Close_log_lag1'] = df_model['Close_log'].shift(1)
df_model['Close_log_lag2'] = df_model['Close_log'].shift(2)
df_model.dropna(inplace=True)

# Split en train y test (por ejemplo, último mes como test)
train_size = int(len(df_model)*0.9)
train = df_model.iloc[:train_size]
test = df_model.iloc[train_size:]
X_train = train[['Close_log_lag1','Close_log_lag2']]
y_train = train['Close_log']
X_test = test[['Close_log_lag1','Close_log_lag2']]
y_test = test['Close_log']
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("R²:", r2)

# Predicción a futuro (3 periodos)
# Se toman las últimas filas para crear el pronóstico
last_row = df_model.iloc[-2:]
future_preds = []

# Generar predicciones iterativas:
current_lag1 = df_model['Close_log'].iloc[-1]
current_lag2 = df_model['Close_log'].iloc[-2]

for i in range(3):
    X_future = np.array([[current_lag1, current_lag2]])
    future_log = model.predict(X_future)[0]
    future_preds.append(np.exp(future_log))

    # Actualizar lag para siguiente predicción
    current_lag2 = current_lag1
    current_lag1 = future_log

print("Predicciones a futuro (3 periodos) en valor original:")
print(future_preds)

# Guardar predicciones y métricas
predictions_df = pd.DataFrame({
'Date': pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=3),
'Predicted_Close': future_preds
})

#Almacenar datos para table Power Bi
predictions_df.to_csv("data/future_predictions.csv", index=False, sep="," , decimal=".")

y_test_orig = np.exp(y_test)
y_pred_orig = np.exp(y_pred)
test_dates = test.index
future_dates = predictions_df['Date']

future_preds = predictions_df['Predicted_Close']

plt.figure(figsize=(12,6))
plt.plot(test_dates, y_test_orig, label='Real (Test)', color='blue')
plt.plot(test_dates, y_pred_orig, label='Predicho (Test)', color='red',linestyle='--')
plt.plot(future_dates, future_preds, label='Predicciones Futuras', color='green', marker='o')
plt.title('Predicciones Futuras (3 Periodos) + Conjunto de Prueba')
plt.xlabel('Fecha')
plt.ylabel('Precio Close')
plt.legend()
plt.grid(True)
plt.axvline(x=test_dates[-1], color='grey', linestyle='--')
plt.show()