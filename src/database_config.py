import sqlite3
import pandas as pd
import os

database_path = "database"
path_db = os.path.join(database_path, "DataBase.db")

teste = 'valor unitário'

conn = sqlite3.connect('DataBase.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Formularios(
    nome varchar(80),
    email varchar(80),
    data varchar(80),
    processamento varchar(80)
    )                              
    ''')

cursor.execute(f'''
    INSERT INTO Formularios
    VALUES {teste}
               ''')

conn.commit()
conn.close()