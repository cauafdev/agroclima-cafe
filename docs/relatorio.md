# Relatório

Versão em texto (fora do notebook) das conclusões da pesquisa. Serve como
resumo para compartilhar com outras pessoas sem precisar rodar código.
Análise completa, com gráficos e código, em `notebooks/04_relatorio.ipynb`.

## Resumo

Analisamos 25 anos (2000-2024) de dados climáticos diários (Open-Meteo) e
produção cafeeira anual (IBGE/SIDRA) de Lavras-MG, calculando índices de
risco climático (geada, chuva excessiva, veranico) e cruzando-os com
produção, quantidade produzida e rendimento médio. Nesta fase, não
encontramos evidência de correlação linear forte entre os riscos
climáticos medidos e a produtividade do café — um resultado tão
informativo quanto uma correlação forte teria sido, já que aponta para
onde a próxima etapa de investigação precisa ir (ver Próximos passos).

## Principais achados

- **Geada não é mensurável com a fonte atual**: com o limiar de geada
  leve (≤3°C), nenhum dos 9.132 dias da série é classificado — a mínima
  absoluta observada é 3,1°C. É uma limitação da fonte (Open-Meteo é
  reanálise em grade, que suaviza extremos locais), não evidência de
  ausência de geada em Lavras.
- **Chuva excessiva (>50 mm/dia) é rara e sem tendência**: no máximo 2
  dias por ano na série, sem padrão claro de alta ou queda ao longo dos
  25 anos.
- **Veranico tem sazonalidade dentro da estação chuvosa**: 30 veranicos
  detectados (sequências de ≥10 dias secos consecutivos entre outubro e
  março), concentrados no início (outubro, 9 ocorrências) e no fim
  (fevereiro-março, 16 ocorrências) da estação chuvosa. Novembro-janeiro
  concentra só 5 das 30 ocorrências — um primeiro indício de janela
  historicamente mais estável, ainda exploratório dado o tamanho da
  amostra.
- **Clima x produção: correlações fracas em todos os pares testados**
  (Pearson, |r| < 0,25, n=25 anos). A correlação mais forte é veranico x
  área colhida (r ≈ -0,23), mas a área colhida cresce quase
  monotonicamente no período (expansão econômica, não sinal climático),
  o que pode confundir essa leitura. No rendimento médio por hectare —
  a métrica de produtividade menos afetada por essa expansão — as
  correlações ficam praticamente em zero (-0,05 a -0,06).

## Limitações

- Geada subestimada pela fonte climática atual (Open-Meteo).
- Amostra pequena (25 pontos anuais) para conclusões estatisticamente
  robustas sobre correlação clima-produção.
- `area_colhida_ha` tem tendência temporal forte não relacionada a
  clima, que pode confundir correlações que a envolvem.
- Produção é só municipal e anual — não há dado por propriedade/talhão
  nem em resolução sub-anual, o que impede ligar um evento climático
  específico à safra correspondente.
- Nenhum dado de preço/mercado do café, que também influencia produção
  e não foi controlado nesta análise.

## Próximos passos

- Buscar fonte de geada mais confiável (ex. BDMEP/INMET) para validar
  o achado sobre geada.
- Testar correlação com defasagem (clima do ano N x produção do ano
  N+1), já que efeitos climáticos podem só aparecer na safra seguinte.
- Testar relações não lineares ou por faixas (ex. anos com veranico
  longo vs. sem) em vez de só correlação linear.
- Buscar séries de preço do café para controlar o efeito de mercado.
- Ampliar o recorte geográfico (outros municípios da região) para
  aumentar o tamanho da amostra.
