# src/risco.py
# Funções reutilizáveis para calcular índices e classificações de risco
# climático (seca, geada, excesso de chuva, etc.) e sua relação com as
# janelas de colheita/plantio do café. Usado principalmente pelos
# notebooks 03_eda.ipynb e 04_relatorio.ipynb.
import pandas as pd

# Cafeeiro sofre dano foliar com geada leve abaixo de ~3°C e dano severo
# (perda de produção) abaixo de 0°C (referência: EPAMIG).
LIMITE_GEADA_LEVE = 3.0
LIMITE_GEADA_SEVERA = 0.0

# Estação chuvosa em Lavras-MG vai de outubro a março; veranico é a
# interrupção anômala das chuvas dentro desse período.
MESES_ESTACAO_CHUVOSA = {10, 11, 12, 1, 2, 3}


def marcar_geada(df, limite=LIMITE_GEADA_LEVE):
    return df["temperature_2m_min"] <= limite


def marcar_dia_seco(df, limite_mm=1.0):
    return df["precipitation_sum"] < limite_mm


def marcar_chuva_excessiva(df, limite_mm=50.0):
    return df["precipitation_sum"] > limite_mm


def contar_sequencias_secas(df, dias_min=10, apenas_estacao_chuvosa=True):
    """Sequências de dias secos consecutivos com pelo menos `dias_min` dias (veranico)."""
    dia_seco = marcar_dia_seco(df)
    sequencia_id = (~dia_seco).cumsum()

    sequencias = (
        df[dia_seco]
        .groupby(sequencia_id[dia_seco])
        .agg(inicio=("time", "first"), fim=("time", "last"), duracao=("time", "size"))
    )
    sequencias = sequencias[sequencias["duracao"] >= dias_min]

    if apenas_estacao_chuvosa:
        sequencias = sequencias[sequencias["inicio"].dt.month.isin(MESES_ESTACAO_CHUVOSA)]

    return sequencias.reset_index(drop=True)


def resumo_anual_risco(df):
    """Contagem por ano de dias de geada leve/severa, dias de chuva excessiva e veranicos."""
    ano = df["time"].dt.year
    veranicos_por_ano = contar_sequencias_secas(df)["inicio"].dt.year.value_counts()

    resumo = pd.DataFrame({
        "geada_leve": marcar_geada(df, LIMITE_GEADA_LEVE).groupby(ano).sum(),
        "geada_severa": marcar_geada(df, LIMITE_GEADA_SEVERA).groupby(ano).sum(),
        "chuva_excessiva": marcar_chuva_excessiva(df).groupby(ano).sum(),
    })
    resumo["veranicos"] = veranicos_por_ano.reindex(resumo.index).fillna(0).astype(int)
    resumo.index.name = "ano"
    return resumo
