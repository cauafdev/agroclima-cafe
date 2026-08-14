# src/coleta.py
# Funções reutilizáveis para coletar dados climáticos e de produção
# cafeeira (ex.: APIs como INMET, NASA POWER, Open-Meteo, IBGE) para a
# região de Lavras-MG. Usado principalmente pelo notebook 01_coleta.ipynb.
import requests
import pandas as pd

# Código IBGE do município de Lavras-MG, usado nas consultas ao SIDRA.
CODIGO_IBGE_LAVRAS = 3138203


def coletar_clima(ano_inicio=2000, ano_fim=2024):
    """Baixa temperatura máx/mín e precipitação diárias de Lavras-MG via Open-Meteo."""
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": -21.24,
        "longitude": -44.99,
        "start_date": f"{ano_inicio}-01-01",
        "end_date": f"{ano_fim}-12-31",
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": "America/Sao_Paulo",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    dados = response.json()
    df = pd.DataFrame(dados["daily"])

    caminho_saida = f"data/raw/lavras_clima_{ano_inicio}_{ano_fim}.csv"
    df.to_csv(caminho_saida, index=False)
    print(f"Arquivo salvo em {caminho_saida}")
    return df


def coletar_producao_cafe(ano_inicio=2000, ano_fim=2024):
    """Baixa série anual de produção de café em Lavras-MG via IBGE (PAM, tabela 1613, SIDRA).

    Fonte: Produção Agrícola Municipal, produto "Café (em grão) Total" (código 2723).
    Granularidade municipal, sem necessidade de conta/login.
    """
    url = (
        "https://apisidra.ibge.gov.br/values/t/1613"
        f"/n6/{CODIGO_IBGE_LAVRAS}/v/216,214,112/p/all/c82/2723"
    )

    response = requests.get(url)
    print(response.status_code)

    dados = response.json()
    df = pd.DataFrame(dados[1:])  # primeira linha é o cabeçalho descritivo do SIDRA
    df = df[["D3C", "D2N", "V"]].rename(columns={"D3C": "ano", "D2N": "variavel", "V": "valor"})
    df["ano"] = df["ano"].astype(int)
    df["valor"] = pd.to_numeric(df["valor"])
    df = df[(df["ano"] >= ano_inicio) & (df["ano"] <= ano_fim)]

    producao = df.pivot(index="ano", columns="variavel", values="valor").reset_index()
    producao = producao.rename(columns={
        "Área colhida": "area_colhida_ha",
        "Quantidade produzida": "quantidade_produzida_t",
        "Rendimento médio da produção": "rendimento_medio_kg_ha",
    })
    producao.columns.name = None

    caminho_saida = f"data/raw/lavras_producao_cafe_{ano_inicio}_{ano_fim}.csv"
    producao.to_csv(caminho_saida, index=False)
    print(f"Arquivo salvo em {caminho_saida}")
    return producao


def validar_dados(df, coluna_data="time"):
    print("Número de linhas:", len(df))
    print("Primeira data:", df[coluna_data].iloc[0])
    print("Última data:", df[coluna_data].iloc[-1])
    print("Valores faltando por coluna:")
    print(df.isna().sum())
