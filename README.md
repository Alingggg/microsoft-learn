# Microsoft Learn Pipeline

An ETL pipeline that loads the public Microsoft Learn catalog into PostgreSQL
for exploration and analysis.

It stores the original API response and creates queryable tables for modules,
units, learning paths, applied skills, certifications, exams, courses, and
their related metadata. Each run is stored as a dated snapshot.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)
- Docker

## Run locally

Create the environment file and start PostgreSQL:

```powershell
Copy-Item .env.example .env
docker compose up -d
```

Create the database tables:

```powershell
Get-Content src/microsoft_learn_pipeline/sql/create_tables.sql |
    docker compose exec -T warehouse-postgres psql -U postgres -d microsoft_learn
```

Install the dependencies and run the pipeline:

```powershell
uv sync
uv run pipeline
```
