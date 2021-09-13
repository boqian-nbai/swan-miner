import sys
import time

sys.path.append("../")
from common.config import read_config
from common.swan_client import SwanClient
from common.logging import get_logger

heartbeat_interval = 300

def heartbeat():
    logger = get_logger('storage_provider_heartbeat')

    config = read_config()

    api_url = config['main']['api_url']
    api_key = config['main']['api_key']
    access_token = config['main']['access_token']
    miner_fid = config['main']['miner_fid']

    while True:
        client = SwanClient(api_url, api_key, access_token)

        try:
            client.send_heartbeat_request(miner_fid)
            logger.info("Heartbeat request sent")
        except Exception as e:
            logger.error("Failed to send heartbeat request")
            logger.error(str(e))

        logger.info("Sleeping...")
        time.sleep(heartbeat_interval)



