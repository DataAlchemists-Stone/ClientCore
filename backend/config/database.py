import psycopg2
from psycopg2 import pool

# Configurações da conexão
DATABASE_CONFIG = {
    'dbname': 'nome_do_banco',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'port': '5432'
}

# Cria um pool de conexões
def create_connection_pool():
    return psycopg2.pool.SimpleConnectionPool(
        1,  # Min connections
        10,  # Max connections
        **DATABASE_CONFIG
    )

connection_pool = create_connection_pool()
