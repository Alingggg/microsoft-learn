CREATE TABLE IF NOT EXISTS raw_data (
    snapshot_date  DATE PRIMARY KEY,
    raw_data       JSONB,
    ingested_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS modules (
    uid                  TEXT NOT NULL,
    snapshot_date        DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    summary              TEXT,
    levels               JSONB,
    roles                JSONB,
    products             JSONB,
    subjects             JSONB,
    type                 TEXT,
    title                TEXT,
    duration_in_minutes  INTEGER,
    rating               JSONB,
    popularity           DOUBLE PRECISION,
    icon_url             TEXT,
    social_image_url     TEXT,
    locale               TEXT,
    last_modified        TEXT,
    url                  TEXT,
    "firstUnitUrl"       TEXT,
    units                JSONB,
    number_of_children   INTEGER,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS units (
    uid                  TEXT NOT NULL,
    snapshot_date        DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    type                 TEXT,
    title                TEXT,
    duration_in_minutes  INTEGER,
    locale               TEXT,
    last_modified        TEXT,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS learning_paths (
    uid                  TEXT NOT NULL,
    snapshot_date        DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    summary              TEXT,
    levels               JSONB,
    roles                JSONB,
    products             JSONB,
    subjects             JSONB,
    type                 TEXT,
    title                TEXT,
    duration_in_minutes  INTEGER,
    rating               JSONB,
    popularity           DOUBLE PRECISION,
    icon_url             TEXT,
    social_image_url     TEXT,
    locale               TEXT,
    last_modified        TEXT,
    url                  TEXT,
    "firstModuleUrl"     TEXT,
    modules              JSONB,
    number_of_children   INTEGER,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS applied_skills (
    uid            TEXT NOT NULL,
    snapshot_date  DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    locale         TEXT,
    url            TEXT,
    title          TEXT,
    summary        TEXT,
    levels         JSONB,
    roles          JSONB,
    products       JSONB,
    subjects       JSONB,
    study_guide    JSONB,
    last_modified  TEXT,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS certifications (
    uid                 TEXT NOT NULL,
    snapshot_date       DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    title               TEXT,
    subtitle            TEXT,
    url                 TEXT,
    icon_url            TEXT,
    last_modified       TEXT,
    type                TEXT,
    certification_type  TEXT,
    exams               JSONB,
    levels              JSONB,
    roles               JSONB,
    study_guide         JSONB,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS merged_certifications (
    uid                        TEXT NOT NULL,
    snapshot_date              DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    title                      TEXT,
    summary                    TEXT,
    url                        TEXT,
    icon_url                   TEXT,
    last_modified              TEXT,
    type                       TEXT,
    certification_type         TEXT,
    products                   JSONB,
    levels                     JSONB,
    roles                      JSONB,
    subjects                   JSONB,
    renewal_frequency_in_days  INTEGER,
    prerequisites              JSONB,
    skills                     JSONB,
    recommendation_list        JSONB,
    study_guide                JSONB,
    exam_duration_in_minutes   INTEGER,
    locales                    JSONB,
    providers                  JSONB,
    career_paths               JSONB,
    practice_assessment_uid    TEXT,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS exams (
    uid                      TEXT NOT NULL,
    snapshot_date            DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    title                    TEXT,
    subtitle                 TEXT,
    display_name             TEXT,
    url                      TEXT,
    icon_url                 TEXT,
    pdf_download_url         TEXT,
    practice_assessment_url  TEXT,
    practice_test_url        TEXT,
    locales                  JSONB,
    last_modified            TEXT,
    type                     TEXT,
    courses                  JSONB,
    levels                   JSONB,
    roles                    JSONB,
    products                 JSONB,
    providers                JSONB,
    study_guide              JSONB,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS courses (
    uid                  TEXT NOT NULL,
    snapshot_date        DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    course_number        TEXT,
    title                TEXT,
    summary              TEXT,
    duration_in_hours    INTEGER,
    url                  TEXT,
    icon_url             TEXT,
    locales              JSONB,
    last_modified        TEXT,
    type                 TEXT,
    levels               JSONB,
    roles                JSONB,
    products             JSONB,
    study_guide          JSONB,
    recommendation_list  JSONB,
    certification        TEXT,
    exam                 TEXT,
    PRIMARY KEY (snapshot_date, uid)
);

CREATE TABLE IF NOT EXISTS levels (
    id            TEXT NOT NULL,
    snapshot_date DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    name          TEXT,
    PRIMARY KEY (snapshot_date, id)
);

CREATE TABLE IF NOT EXISTS products (
    id            TEXT NOT NULL,
    snapshot_date DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    name          TEXT,
    children      JSONB,
    PRIMARY KEY (snapshot_date, id)
);

CREATE TABLE IF NOT EXISTS roles (
    id            TEXT NOT NULL,
    snapshot_date DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    name          TEXT,
    PRIMARY KEY (snapshot_date, id)
);

CREATE TABLE IF NOT EXISTS subjects (
    id            TEXT NOT NULL,
    snapshot_date DATE NOT NULL REFERENCES raw_data(snapshot_date) ON DELETE CASCADE,
    name          TEXT,
    children      JSONB,
    PRIMARY KEY (snapshot_date, id)
);
