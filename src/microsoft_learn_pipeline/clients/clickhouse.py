import clickhouse_connect
from config import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_DB,
    CLICKHOUSE_PASSWORD
)

def get_clickhouse_client():
    return clickhouse_connect.get_client(
        host=CLICKHOUSE_HOST, 
        port=CLICKHOUSE_PORT, 
        username=CLICKHOUSE_DB, 
        password=CLICKHOUSE_PASSWORD
    )