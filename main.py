import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    HUBSPOT_TOKEN = os.environ["HUBSPOT_TOKEN"]
    logger.info("Token available!")
except KeyError:
    HUBSPOT_TOKEN = "Token not available!"
    logger.info("Token not available!")
    raise


if __name__ == "__main__":
    logger.info(f"Starting Script")

    headers = {
    'accept': "application/json",
    'authorization': f"Bearer {HUBSPOT_TOKEN}"
    }

    r = requests.get('https://api.hubapi.com/crm/v3/objects/users/', headers=headers)
    if r.status_code == 200:
        data = r.json()
        user_id = data["results"][0]["id"]
        logger.info(f'ID do primeiro usuário: {user_id}')

    else :
        logger.error(f"Erro ao acessar a API: {r.status_code}")
