import pandas as pd
import glob
import os

# Lista todos os ficheiros CSV na pasta
ficheiros = glob.glob("*.csv")
lista_final = []

for f in ficheiros:
    if f == 'veiculos.csv': continue # Evita ler o próprio ficheiro que vamos criar
    
    try:
        # Lê o CSV tentando encontrar cabeçalhos na linha 1 ou 2
        df = pd.read_csv(f, header=None)
        
        # O padrão dos seus ficheiros parece ser: 
        # Colunas 0,1,2 são Frota, Descrição, Placa
        # Colunas 4,5,6 também são Frota, Descrição, Placa
        
        # Pega a parte esquerda
        parte1 = df.iloc[:, 0:3]
        parte1.columns = ['FROTA', 'DESCRIÇÃO', 'PLACA']
        
        # Pega a parte direita (se existir)
        parte2 = df.iloc[:, 4:7]
        parte2.columns = ['FROTA', 'DESCRIÇÃO', 'PLACA']
        
        lista_final.append(parte1)
        lista_final.append(parte2)
    except:
        continue

# Junta tudo e limpa
df_final = pd.concat(lista_final)
df_final = df_final.dropna(subset=['FROTA'])
df_final = df_final[df_final['FROTA'] != 'FROTA'] # Remove cabeçalhos repetidos
df_final = df_final.drop_duplicates(subset=['FROTA']) # Mantém apenas um registo por frota

# Salva o CSV final
df_final.to_csv('veiculos.csv', index=False)
print("Ficheiro 'veiculos.csv' criado com todos os veículos!")