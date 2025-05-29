import logging
from database_config import informations_config_db
from logs_config import setup_logging

setup_logging()

def main():

    logging.info('Iniciando captura de dados')
    informations_config_db()

if __name__ == "__main__":
    main()