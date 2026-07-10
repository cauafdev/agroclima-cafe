# data/raw

Dados crus, exatamente como vieram da fonte (API, download, etc.).

NUNCA edite os arquivos desta pasta manualmente. Se um dado estiver errado ou
precisar de tratamento, faça isso em código (nos notebooks de limpeza ou em
`src/`) e salve o resultado em `data/processed/`. Assim mantemos sempre a
possibilidade de refazer a limpeza do zero sem perder a fonte original.
