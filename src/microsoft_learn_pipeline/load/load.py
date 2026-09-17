import datetime
import json
import pandas as pd
from sqlalchemy import create_engine

source_file = f"microsoft_learn_catalog_{datetime.datetime.now():%Y%m%d}.json"

with open(source_file, "r", encoding="utf-8") as f:
    data = json.load(f)

def flatten_record(record: dict) -> dict:
    for key, value in record.items():
        if isinstance(value, (dict, list)):
            record[key] = json.dumps(value)

    record["source_file"] = source_file
    return record

top_level_keys = ["levels", "roles", "subjects"]

catalogs_pd = {
    key: pd.DataFrame([flatten_record(r) for r in data[key]]) for key in top_level_keys
}

# for catalog in catalogs_pd:
#     print(f"{catalog}: {catalogs_pd[catalog].head()}")

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/case_study")

for catalog, df in catalogs_pd.items():
    df.to_sql(catalog, engine, if_exists="replace", index=False)
    print(f"Saved records to {catalog} table.")
