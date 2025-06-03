#   numpy = trabalhar com dados numericos arrays e matrizes
#   pandas = trabalhar com dados tabulares DataFrame e Series

from sqlalchemy import create_engine    # para conectar ao banco de dados
import pandas as pd  # para trabalhar com DataFrames

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