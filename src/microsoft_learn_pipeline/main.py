from datetime import datetime
from microsoft_learn_pipeline.extract.catalogs import (
    extract_microsoft_learn_catalog,
)
from microsoft_learn_pipeline.gold.catalogs import (
    load_tables as transform_microsoft_learn_catalog,
)

def main():
    date_today = f"{datetime.now().date().isoformat()}"

    try:
        extract_microsoft_learn_catalog(date_today)
        transform_microsoft_learn_catalog(date_today)

        print("Data extraction and transformation completed successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()  