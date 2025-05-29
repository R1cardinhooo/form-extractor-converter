import os
import pandas as pd
import sqlite3
import random
import logging
from logs_config import setup_logging

setup_logging()

base_dir = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(base_dir, '..', 'csv_file', 'dados.csv'))
db_path = os.path.abspath(os.path.join(base_dir, '..', 'DataBase', 'database.db'))

def informations_config_db():
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV não encontrado: {csv_path}")
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Banco de dados não encontrado: {db_path}")

    df = pd.read_csv(csv_path, header=0)

    df = df[["Data", "Nome", "Telefone", "Tipo", "Endereco", "CEP", "Email"]]
    df.columns = ["data", "nome", "telefone", "tipo", "endereco", "cep", "email"]

    df["protocolo"] = [str(random.randint(10000, 99999)) for _ in range(len(df))]
    df["status"] = "Pendente"

    conn = sqlite3.connect(db_path)
    df.to_sql("FormsEntrada", conn, if_exists="append", index=False)
    conn.close()

    logging.info('Dados inseridos com sucesso!')
