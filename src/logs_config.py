import logging
import os

def setup_logging():

    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório do script
    log_dir = os.path.join(base_dir, "logs")  # Garante que está dentro do diretório correto
    os.makedirs(log_dir, exist_ok=True)  # Cria a pasta se não existir

    log_file = os.path.join(log_dir, "logs.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),  # Log no arquivo
            logging.StreamHandler()  # Log no console
        ]
    )

    logging.info("Configuração de logging carregada!")