import requests, datetime
from microsoft_learn_pipeline.config import MICROSOFT_LEARN_API_BASE_URL
from microsoft_learn_pipeline.clients.postgres import get_connection
from psycopg.types.json import Jsonb

def extract_microsoft_learn_catalog(date_today):
    res = requests.get(MICROSOFT_LEARN_API_BASE_URL, timeout=60)
    res.raise_for_status()

    bronze_row = {
        "snapshot_date": date_today,
        "raw_data": Jsonb(res.json()),
        "ingested_at": datetime.datetime.now().isoformat()
    } 

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM raw_data 
                WHERE snapshot_date = %s
                """,
                (date_today,)
            )

            cur.execute(
                """
                INSERT INTO raw_data (snapshot_date, raw_data, ingested_at)
                VALUES (%(snapshot_date)s, %(raw_data)s, %(ingested_at)s)
                """,
                bronze_row
            )