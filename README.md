# Agroclima Café

Previsão de risco climático para a cafeicultura na região de Lavras/MG, a
partir de dados históricos reais de clima e produção.

## Objetivo

Entender como eventos climáticos (geada, seca, excesso de chuva, veranico)
afetam a produção de café em Lavras/MG e, a partir disso, construir uma base
de dados e análises que sirvam de fundação para um futuro SaaS: uma
ferramenta que ajude cooperativas de café a identificar as melhores janelas
de colheita e plantio com base em dados históricos e locais.

Este é também um projeto de estudo — o código e as análises evoluem à medida
que aprendo.

## Estrutura de pastas

```
agroclima-cafe/
├── README.md              -> este arquivo
├── requirements.txt       -> lista de bibliotecas
├── LICENSE                -> licença MIT
├── .gitignore              -> o que o Git deve ignorar
├── data/
│   ├── raw/                -> dados crus, como vieram da fonte (NUNCA edite)
│   └── processed/          -> dados limpos, prontos pra análise
├── notebooks/
│   ├── 01_coleta.ipynb
│   ├── 02_limpeza.ipynb
│   ├── 03_eda.ipynb
│   └── 04_relatorio.ipynb  -> notebook principal com narrativa
├── src/                     -> funções reutilizáveis (.py)
│   ├── coleta.py
│   └── risco.py
├── figuras/                 -> gráficos exportados
└── docs/
    ├── especificacao.md    -> documento de escopo do projeto
    └── relatorio.md        -> versão texto das conclusões
```

## Como rodar

1. Clone o repositório e entre na pasta.
2. Crie um ambiente virtual e instale as dependências:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Abra os notebooks na pasta `notebooks/` em ordem (01 → 04).

## Fontes de dados

- [INMET - Instituto Nacional de Meteorologia](https://portal.inmet.gov.br/dadoshistoricos) — dados históricos de estações meteorológicas.
- [NASA POWER](https://power.larc.nasa.gov/) — dados climáticos históricos via API, cobertura global.
- [CONAB - Companhia Nacional de Abastecimento](https://www.conab.gov.br/info-agro/safras/cafe) — séries históricas de safra e produtividade do café.
- [EPAMIG - Empresa de Pesquisa Agropecuária de Minas Gerais](http://www.epamig.br/) — pesquisa e dados agropecuários regionais.

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## Status

🚧 Em desenvolvimento.
