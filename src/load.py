import polars as pl
import logging
from io import BytesIO

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def load(clean_file):
    try:
        buffer = BytesIO()
        clean_file.write_csv(buffer)
        buffer.seek(0)

        logger.info('Successfully written csv to buffer')

        return {
            'status': 'Success',
            'buffer': buffer
        }

    except Exception as e:
        logger.error(f'Unable to create BytesIO buffer: {e}')
        return {
            'status': 'Failure',
            'error': e
        }