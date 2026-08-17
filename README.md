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

**📊 [Veja a pesquisa completa em um único notebook: `Projeto_Agroclima_Cafe.ipynb`](Projeto_Agroclima_Cafe.ipynb)**
— coleta, limpeza, análise exploratória, correlação, regressão e
conclusões, com todos os gráficos e tabelas renderizados direto no
GitHub, sem precisar rodar nada.

## Estrutura de pastas

```
agroclima-cafe/
├── README.md                        -> este arquivo
├── Projeto_Agroclima_Cafe.ipynb     -> pesquisa completa em um notebook só (comece por aqui)
├── requirements.txt                 -> lista de bibliotecas
├── LICENSE                          -> licença MIT
├── .gitignore                        -> o que o Git deve ignorar
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
3. Para ver a pesquisa inteira de uma vez, abra `Projeto_Agroclima_Cafe.ipynb`
   na raiz (é autocontido, refaz a coleta sozinho). Para o pipeline
   real passo a passo, abra os notebooks em `notebooks/` em ordem
   (01 → 04).

## Fontes de dados

- [Open-Meteo](https://open-meteo.com/) (Archive API) — temperatura máx/mín e precipitação diárias, 1974-2024, reanálise histórica.
- Estação real do INMET em Lavras/UFLA (código 83687) — usada só para geada, via os dados de observação por estação do [BR-DWGD](https://github.com/AlexandreCandidoXavier/BR-DWGD) (Xavier et al., 2022).
- [IBGE/SIDRA](https://sidra.ibge.gov.br/) (Produção Agrícola Municipal, tabela 1613) — área colhida, quantidade produzida e rendimento médio de café em Lavras-MG, 1974-2024.

Detalhes de cada fonte e por que foram escolhidas em [docs/especificacao.md](docs/especificacao.md).

## Principais achados

25 anos de dados de reanálise (Open-Meteo) nunca registravam geada em
Lavras — limitação da fonte, não ausência real do fenômeno. Trocamos
para dado de estação real e ampliamos o recorte para 51 anos, o que
revelou 6 anos com geada leve e 1 com geada severa. Uma regressão
controlando por área colhida mostrou que o efeito aparente de geada no
mesmo ano era artefato de um único ano atípico — mas o efeito
*defasado* (geada de um ano prejudicando o rendimento do ano seguinte)
se mantém, ainda que estatisticamente frágil. Análise completa em
[docs/relatorio.md](docs/relatorio.md).

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## Status

✅ Fase 1 concluída — coleta, limpeza, EDA e relatório com dados reais
(1974-2024, Lavras-MG). Ideias para uma fase futura (mais municípios,
dado de preço do café) documentadas em
[docs/relatorio.md](docs/relatorio.md#próximos-passos).
