import os

from data_test_ci.utils.db import DBconnction

def get_warehouse_creds() -> DBconnction:
    return DBconnction(
        db = os.getenv('WAREHOUSE_DB', ''),
        user = os.getenv('WAREHOUSE_USER', ''),
        password = os.getenv('WAREHOUSE_PASSWORD', ''),
        host = os.getenv('WAREHOUSE_HOST', ''),
        port = int(os.getenv('WAREHOUSE_PORT', 5433))
    )