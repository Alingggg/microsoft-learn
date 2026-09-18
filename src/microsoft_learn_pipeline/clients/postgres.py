import psycopg
from microsoft_learn_pipeline.config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,    
    POSTGRES_USER,
    POSTGRES_PASSWORD,  
)

def get_connection():
    return psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
    )
