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
comparar de verdade. Uma regressão controlando por área colhida mostrou
que o efeito positivo de geada no mesmo ano é artefato de um único ano
atípico (não é real), enquanto o efeito negativo defasado (geada
prejudicando a safra seguinte) é mais robusto e consistente com a
agronomia, ainda que estatisticamente frágil com a amostra atual.

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
- **Correlação direta de geada é enganosa; regressão confirma o porquê**.
  `geada_leve` e `geada_severa` aparecem com as maiores correlações
  diretas da tabela (rendimento: r≈+0,31 e r≈+0,62) — o oposto do que a
  agronomia prevê. Uma regressão múltipla (rendimento em função de
  geada **e** área colhida) mostrou que esse efeito positivo depende
  inteiramente de um único ano: **1981**, que teve o maior rendimento
  da série (3.757 kg/ha, mais que o dobro do segundo colocado) *e*
  geada leve no mesmo ano. Removendo só esse ano, o coeficiente de
  geada cai de +270 para +50 kg/ha e deixa de ser estatisticamente
  significativo (p≈0,04 → p≈0,67) — o efeito direto é artefato, não
  real.
- **O sinal defasado é mais robusto**: geada do ano N associada a
  rendimento *menor* no ano N+1 (r≈-0,23 leve, r≈-0,16 severa na
  correlação simples; coeficiente ≈ -322 kg/ha, p≈0,03 na regressão
  controlando por área colhida). Diferente do efeito direto, esse sinal
  **sobrevive** à remoção do ano mais influente (cai para -228 kg/ha,
  p≈0,05 — ainda na borda da significância, mas não desaparece). É a
  evidência mais consistente com a agronomia encontrada na pesquisa,
  embora o R² de ambos os modelos seja baixo (~0,10) — geada explica só
  uma fração pequena da variação de rendimento, não é o fator
  principal. Fora a geada, chuva excessiva e veranico seguem sem
  relação clara com produção em qualquer abordagem testada (direta,
  defasada, por faixas).

## Limitações

- Geada: efeito direto é artefato de um único ano (1981); o efeito
  defasado é mais robusto mas ainda estatisticamente frágil — baseado
  em só 6 anos de geada leve e 1 de geada severa, com significância na
  borda (p≈0,05) depois de remover o ano mais influente.
- Amostra pequena para correlação: 51 pontos anuais — melhor que os 25
  anteriores, mas ainda pouco para conclusões estatisticamente
  robustas. R² dos modelos de regressão é baixo (~0,10) mesmo no melhor
  caso.
- `area_colhida_ha` tem tendência temporal forte não relacionada a
  clima, que confunde diretamente a correlação de geada e pode afetar
  outras correlações que a envolvem.
- Produção é só municipal e anual — não há dado por propriedade/talhão
  nem em resolução sub-anual, o que impede ligar um evento climático
  específico à safra correspondente.
- Nenhum dado de preço/mercado do café, que também influencia produção
  e não foi controlado nesta análise.

## Próximos passos

Esta fase é considerada completa com o escopo definido em
`docs/especificacao.md` (só Lavras-MG, sem dado de preço/mercado — nunca
fez parte do plano inicial). As ideias abaixo ficam registradas como
possíveis direções para uma fase futura, não como pendências:

- Ampliar o recorte geográfico (outros municípios da região) para
  aumentar o número de anos-com-geada e dar mais robustez estatística
  ao sinal defasado encontrado na regressão.
- Buscar séries de preço do café para controlar o efeito de mercado.
