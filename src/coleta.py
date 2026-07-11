# src/coleta.py
# Funções reutilizáveis para coletar dados climáticos e de produção
# cafeeira (ex.: APIs como INMET, NASA POWER, Open-Meteo) para a região
# de Lavras-MG. Usado principalmente pelo notebook 01_coleta.ipynb.
import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": -21.24,
    "longitude": -44.99,
    "start_date": "2000-01-01",
    "end_date": "2024-12-31",
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "America/Sao_Paulo",
}

response = requests.get(url, params=params)
print(response.status_code)

dados = response.json()
diario = dados["daily"]

df = pd.DataFrame(diario)
print(df.head())
print(df.shape)

caminho_saida = "data/raw/lavras_clima_2000_2024.csv"
df.to_csv(caminho_saida, index=False)
print(f"Arquivo salvo em {caminho_saida}")

def validar_dados(df):
    print("Número de linhas:", len(df))
    print("Primeira data:", df["time"].iloc[0])
    print("Última data:", df["time"].iloc[-1])
    print("Valores faltando por coluna:")
    print(df.isna().sum())

validar_dados(df)
