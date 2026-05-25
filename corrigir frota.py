import pandas as pd

# Lê o ficheiro (ajuste o nome se for necessário)
df = pd.read_csv('FROTA ALESSANDRO.xlsx - PLANILHA FROTA.csv', header=None)

# Extrai a parte da esquerda (Colunas 0, 1, 2)
lado_esquerdo = df.iloc[3:, 0:3]
lado_esquerdo.columns = ['FROTA', 'DESCRIÇÃO', 'PLACA']

# Extrai a parte da direita (Colunas 4, 5, 6)
lado_direito = df.iloc[3:, 4:7]
lado_direito.columns = ['FROTA', 'DESCRIÇÃO', 'PLACA']

# Junta tudo numa lista só
df_final = pd.concat([lado_esquerdo, lado_direito])

# Remove linhas vazias e limpa espaços
df_final = df_final.dropna(subset=['FROTA'])
df_final = df_final.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Salva o resultado final
df_final.to_csv('veiculos.csv', index=False)
print("Ficheiro 'veiculos.csv' criado com sucesso!")