# tb_vendas.csv
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os as os
import pandas as pd
import numpy as np

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

host = os.getenv('db_host')  # Padrão é localhost
user = os.getenv('db_user')  # Padrão é root
password = os.getenv('db_password')  # Padrão é 123456
database = os.getenv('db_database')  # Padrão é aula16

# Conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query_vendedor = 'SELECT * FROM tb_vendas WHERE nome_vendedor = "Carlos Silva"'

# Buscando dados
# Leitura da tabela de vendas
df_vendas = pd.read_sql(query_vendedor, engine)
print(df_vendas.head())  # Mostra os dados

# Calcular o valor da venda - Criar a série "coluna" valor_venda
df_vendas['valor_venda'] = df_vendas['qtd'] * df_vendas['preco']

# Cria nova coluna com comissão (10%)
df_vendas['comissao'] = (df_vendas['valor_venda'] * 0.09).round(2)
# Mostra o DataFrame com a nova coluna
print(df_vendas[['nome_vendedor', 'valor_venda', 'comissao']])

# ARRAY NUMPY
# Converte para array
array_valor_vendas = np.array(df_vendas['valor_venda'])

# Calcula média e mediana
media = np.mean(array_valor_vendas)
mediana = np.median(array_valor_vendas)
distancia = (abs(media - mediana) / mediana)

# MEDIDAS DE TENDÊNCIA CENTRAL
print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
print(f"Média das comissões: R$ {media:.2f}")
print(f"Mediana das comissões: R$ {mediana:.2f}")
print(f"Distância entre média e mediana: {distancia:.2f}%")