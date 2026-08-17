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
  grade, 2000-2024). Avaliamos usar dado de estação real do INMET
  (estação convencional 83687, Lavras/UFLA) para captar geada com mais
  fidelidade, mas o acesso é só via BDMEP com conta e exportação por
  e-mail — pedido feito e sem resposta, e a API/portal público do INMET
  não respondeu a requisições diretas nas tentativas feitas. Fica como
  possível fonte para trabalho futuro; ver limitação de geada em
  `docs/relatorio.md`.
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
