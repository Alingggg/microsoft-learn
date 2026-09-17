import requests, datetime, json
from microsoft_learn_pipeline.config import MICROSOFT_LEARN_API_BASE_URL

def extract_microsoft_learn_catalog():
    file_name = f"microsoft_learn_catalog_{datetime.datetime.now():%Y%m%d}.json"

    try:
        res = requests.get(MICROSOFT_LEARN_API_BASE_URL, timeout=60)
        res.raise_for_status()

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(res.json(), f, ensure_ascii=False)

        print("Saved:", file_name)
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")

extract_microsoft_learn_catalog()