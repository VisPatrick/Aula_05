from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = 'localhost'
user = 'root'
password = ''
database = 'bd_loja'

enginre = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df_estoque = pd.read_sql('tb_vendas', enginre)
print('\n', df_estoque.head())

df_estoque['arrecadamento'] = df_estoque['qtd'] * df_estoque['preco']

print('\n', df_estoque[['id_venda', 'arrecadamento']])

#   ARRAY NUMPY
array_estoque = np.array(df_estoque['arrecadamento'])

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = (abs(media - mediana) / mediana) * 100

print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
print(f"Média das comissões: R$ {media:.2f}")
print(f"Mediana das comissões: R$ {mediana:.2f}")