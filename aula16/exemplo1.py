#   numpy = trabalhar com dados numericos arrays e matrizes
#   pandas = trabalhar com dados tabulares DataFrame e Series
#   abaixo de 20% de distância entre média e mediana é aceitável, passar de 25% é necessário investigar os dados

from sqlalchemy import create_engine    # para conectar ao banco de dados
import pandas as pd  # para trabalhar com DataFrames
import numpy as np  # PARA TRABALHAR COM DADOS NUMERICOS


# Configurações do banco
host = 'localhost'
user = 'root'
password = ''
database = 'bd_loja'

enginre = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#   obtenção de dados do banco de dados
df_estoque = pd.read_sql('tb_produtos', enginre)
print('\n', df_estoque)
#   manipulação de dados
df_estoque['TotalEstoque'] = df_estoque['qtd'] * df_estoque['preco']
# print('\n', df_estoque.head(10))

print('\n', df_estoque[['produto', 'TotalEstoque']])
print(f'\nTotal Geral de Produtos: {df_estoque["TotalEstoque"].sum()}')

# NUMPY
array_estoque = np.array(df_estoque['TotalEstoque'])
# print('\n', array_estoque)

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = (abs(media - mediana) / mediana) * 100

print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Distância Média e Mediana: {distancia}')