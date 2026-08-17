# Relatório

Versão em texto (fora do notebook) das conclusões da pesquisa. Serve como
resumo para compartilhar com outras pessoas sem precisar rodar código.
Análise completa, com gráficos e código, em `notebooks/04_relatorio.ipynb`.

## Resumo

Analisamos 51 anos (1974-2024) de dados climáticos diários (Open-Meteo,
mais a estação real do INMET em Lavras/UFLA para geada — ver Principais
achados) e produção cafeeira anual (IBGE/SIDRA) de Lavras-MG, calculando
índices de risco climático (geada, chuva excessiva, veranico) e
cruzando-os com produção, quantidade produzida e rendimento médio.
Ampliamos de 2000-2024 (25 anos) para 1974-2024 depois de descobrir que
o IBGE/SIDRA cobre Lavras desde 1974 — dobrar a amostra deu à geada,
pela primeira vez, um número de ocorrências grande o bastante para
comparar de verdade. Nesta fase, a correlação direta entre geada e
produtividade é positiva e contraintuitiva, mas isso tem uma explicação
concreta (não é efeito real — ver Principais achados); a correlação
defasada aponta na direção esperada pela agronomia, mas ainda é fraca
demais para provar causalidade.

## Principais achados

- **Geada: resolvemos a fonte e ampliamos a amostra**. Com o Open-Meteo
  (reanálise em grade), a série de 51 anos classifica só 4 dias de
  geada em 3 anos (1979, 1981, 1994), mínima absoluta 1,5°C — mais
  informativo que o recorte anterior de 25 anos (que não pegava
  nenhum), mas ainda uma limitação de fonte. Depois de tentar sem
  sucesso o BDMEP e a API/portal do INMET, encontramos os dados brutos
  de observação por estação usados para construir o BR-DWGD (Xavier et
  al., 2022), que incluem a estação real 83687 (Lavras/UFLA). Com esse
  dado: **10 dias de geada leve em 6 anos** (1975, 1978, 1979, 1981,
  1994, 2000) e **1 dia de geada severa** (21/07/1981, -0,2°C — a única
  vez na série inteira que a mínima ficou abaixo de 0°C). A grade capta
  os anos mais extremos, mas subestima frequência e severidade, e nunca
  detecta o único evento severo.
- **Chuva excessiva (>50 mm/dia) é rara e sem tendência**: no máximo 3
  dias por ano na série, sem padrão claro de alta ou queda ao longo dos
  51 anos.
- **Veranico tem sazonalidade dentro da estação chuvosa**: 57 veranicos
  detectados (sequências de ≥10 dias secos consecutivos entre outubro e
  março), concentrados no início (outubro, 18 ocorrências) e no fim
  (fevereiro-março, 29 ocorrências) da estação chuvosa. Novembro-janeiro
  concentra só 10 das 57 ocorrências — o mesmo padrão do recorte
  anterior de 25 anos, o que reforça que é um sinal real, não ruído de
  amostra pequena.
- **Clima x produção: a correlação direta de geada é enganosa, mas a
  defasada é mais plausível**. `geada_leve` e `geada_severa` aparecem
  com as maiores correlações diretas da tabela (rendimento: r≈+0,31 e
  r≈+0,62) — o oposto do que a agronomia prevê. A explicação: nos anos
  com geada leve a quantidade produzida é praticamente igual à dos anos
  sem (4.816t vs 4.783t em média), mas a área colhida é bem menor
  (2.568ha vs 3.515ha) — 4 dos 6 anos de geada caem entre 1975 e 1981,
  no início da série, quando a lavoura de Lavras ainda era menor. O
  tamanho da área naquele período é o fator de confusão, não a geada.
  Já a correlação **defasada** (geada do ano N x produção do ano N+1)
  vira negativa em toda a tabela de geada (rendimento: r≈-0,23 e
  r≈-0,16) — consistente com o que se esperaria agronomicamente, ainda
  que estatisticamente frágil com n=6. Fora a geada, todas as
  correlações (chuva excessiva, veranico) seguem fracas (|r| < 0,25) em
  todas as abordagens testadas (direta, defasada, por faixas).

## Limitações

- Geada: amostra real (6 anos leves, 1 severo em 51), mas a correlação
  direta é confundida pela tendência de `area_colhida_ha` — a maioria
  dos anos de geada cai no início da série, quando a área colhida era
  menor por razões econômicas, não climáticas. O sinal defasado é mais
  plausível, mas ainda estatisticamente frágil com essa amostra.
- Amostra pequena para correlação: 51 pontos anuais — melhor que os 25
  anteriores, mas ainda pouco para conclusões estatisticamente
  robustas, especialmente para geada severa (n=1).
- `area_colhida_ha` tem tendência temporal forte não relacionada a
  clima, que confunde diretamente a correlação de geada e pode afetar
  outras correlações que a envolvem.
- Produção é só municipal e anual — não há dado por propriedade/talhão
  nem em resolução sub-anual, o que impede ligar um evento climático
  específico à safra correspondente.
- Nenhum dado de preço/mercado do café, que também influencia produção
  e não foi controlado nesta análise.

## Próximos passos

- Testar uma regressão controlando por `area_colhida_ha` para isolar o
  efeito de geada da tendência de expansão da lavoura — o achado sobre
  geada sugere que isso pode revelar um sinal real hoje mascarado pela
  correlação direta.
- Buscar séries de preço do café para controlar o efeito de mercado.
- Ampliar o recorte geográfico (outros municípios da região) para
  aumentar o tamanho da amostra.
