# Especificação do projeto

Documento vivo com o escopo, perguntas de pesquisa e decisões do projeto
Agroclima Café. É o "documento do projeto": para onde estamos indo e por quê.

## Contexto

Pesquisa sobre eventos climáticos na região de Lavras-MG e sua relação com a
produção cafeeira, com o objetivo futuro de embasar um SaaS para cooperativas
de café identificarem as melhores janelas de colheita e plantio.

## Perguntas de pesquisa

- Quais eventos climáticos (geada, seca, excesso de chuva, veranico) mais
  afetam a produção de café na região de Lavras?
- Existe correlação histórica entre variáveis climáticas e produtividade
  (sacas/hectare)?
- É possível identificar janelas de colheita/plantio com menor risco
  climático a partir de dados históricos?

## Fontes de dados

- Dados climáticos: **Open-Meteo** (Archive API, reanálise diária em
  grade, 2000-2024) para temperatura máx/mín e precipitação. Para
  **geada** especificamente, usamos a estação convencional real do
  INMET em Lavras/UFLA (83687), via os dados brutos de observação por
  estação usados para construir o **BR-DWGD** (Xavier et al., 2022,
  https://github.com/AlexandreCandidoXavier/BR-DWGD) — acesso público,
  sem conta/login. Chegamos a essa fonte depois de tentar sem sucesso o
  BDMEP (pedido de exportação sem resposta) e a API/portal público do
  INMET (bloqueou requisições automatizadas). Ver achado e limitação
  (amostra de geada pequena) em `docs/relatorio.md`.
- Dados de produção cafeeira: **IBGE/SIDRA** (Produção Agrícola
  Municipal, tabela 1613, produto "Café (em grão) Total"), granularidade
  municipal e anual. CONAB foi avaliada e descartada por só ter série em
  nível regional, não municipal.

## Escopo inicial

- Foco geográfico: região de Lavras-MG.
- Recorte temporal: 2000-2024 (25 anos), limitado pela série anual de
  produção do IBGE/SIDRA disponível para o município.

## Fora de escopo (por enquanto)

- Construção do produto SaaS em si (fica para uma fase futura, após validar
  a pesquisa).

## Referências

- XAVIER, A. C.; SCANLON, B. R.; KING, C. W.; ALVES, A. I. New Improved
  Brazilian Daily Weather Gridded Data (1961-2020). **International
  Journal of Climatology**, v. 42, n. 16, p. 8390-8404, 2022.
  https://doi.org/10.1002/joc.7731 — fonte da série de geada (estação
  83687, dado de observação, não a grade interpolada) usada em
  `src/coleta.py::coletar_geada_estacao_83687`.
- DANTAS, A. A. A.; CARVALHO, L. G. de; FERREIRA, E. Classificação e
  tendências climáticas em Lavras, MG. **Ciência e Agrotecnologia**,
  Lavras, v. 31, n. 6, p. 1862-1866, nov./dez. 2007. Usa dados da mesma
  Estação Climatológica Principal de Lavras (convênio UFLA/INMET,
  estação 83687) para balanço hídrico e classificação climática
  (Köppen: Cwa) — referência de contexto/legitimidade da estação, não
  fonte de dado diário (só traz médias mensais 1961-1990 e 1991-2004).
