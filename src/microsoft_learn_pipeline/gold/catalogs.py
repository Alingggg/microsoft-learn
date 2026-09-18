import datetime
from psycopg.types.json import Jsonb
from microsoft_learn_pipeline.clients.postgres import get_connection

SECTION_LOADS = {
    "modules": {
        "delete": "DELETE FROM modules WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO modules (
                snapshot_date,
                uid,
                summary,
                levels,
                roles,
                products,
                subjects,
                type,
                title,
                duration_in_minutes,
                rating,
                popularity,
                icon_url,
                social_image_url,
                locale,
                last_modified,
                url,
                "firstUnitUrl",
                units,
                number_of_children
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(summary)s,
                %(levels)s,
                %(roles)s,
                %(products)s,
                %(subjects)s,
                %(type)s,
                %(title)s,
                %(duration_in_minutes)s,
                %(rating)s,
                %(popularity)s,
                %(icon_url)s,
                %(social_image_url)s,
                %(locale)s,
                %(last_modified)s,
                %(url)s,
                %(firstUnitUrl)s,
                %(units)s,
                %(number_of_children)s
            )
        """,
        "columns": (
            "uid",
            "summary",
            "levels",
            "roles",
            "products",
            "subjects",
            "type",
            "title",
            "duration_in_minutes",
            "rating",
            "popularity",
            "icon_url",
            "social_image_url",
            "locale",
            "last_modified",
            "url",
            "firstUnitUrl",
            "units",
            "number_of_children",
        ),
    },
    "units": {
        "delete": "DELETE FROM units WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO units (
                snapshot_date,
                uid,
                type,
                title,
                duration_in_minutes,
                locale,
                last_modified
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(type)s,
                %(title)s,
                %(duration_in_minutes)s,
                %(locale)s,
                %(last_modified)s
            )
        """,
        "columns": (
            "uid",
            "type",
            "title",
            "duration_in_minutes",
            "locale",
            "last_modified",
        ),
    },
    "learningPaths": {
        "delete": "DELETE FROM learning_paths WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO learning_paths (
                snapshot_date,
                uid,
                summary,
                levels,
                roles,
                products,
                subjects,
                type,
                title,
                duration_in_minutes,
                rating,
                popularity,
                icon_url,
                social_image_url,
                locale,
                last_modified,
                url,
                "firstModuleUrl",
                modules,
                number_of_children
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(summary)s,
                %(levels)s,
                %(roles)s,
                %(products)s,
                %(subjects)s,
                %(type)s,
                %(title)s,
                %(duration_in_minutes)s,
                %(rating)s,
                %(popularity)s,
                %(icon_url)s,
                %(social_image_url)s,
                %(locale)s,
                %(last_modified)s,
                %(url)s,
                %(firstModuleUrl)s,
                %(modules)s,
                %(number_of_children)s
            )
        """,
        "columns": (
            "uid",
            "summary",
            "levels",
            "roles",
            "products",
            "subjects",
            "type",
            "title",
            "duration_in_minutes",
            "rating",
            "popularity",
            "icon_url",
            "social_image_url",
            "locale",
            "last_modified",
            "url",
            "firstModuleUrl",
            "modules",
            "number_of_children",
        ),
    },
    "appliedSkills": {
        "delete": "DELETE FROM applied_skills WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO applied_skills (
                snapshot_date,
                uid,
                locale,
                url,
                title,
                summary,
                levels,
                roles,
                products,
                subjects,
                study_guide,
                last_modified
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(locale)s,
                %(url)s,
                %(title)s,
                %(summary)s,
                %(levels)s,
                %(roles)s,
                %(products)s,
                %(subjects)s,
                %(study_guide)s,
                %(last_modified)s
            )
        """,
        "columns": (
            "uid",
            "locale",
            "url",
            "title",
            "summary",
            "levels",
            "roles",
            "products",
            "subjects",
            "study_guide",
            "last_modified",
        ),
    },
    "certifications": {
        "delete": "DELETE FROM certifications WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO certifications (
                snapshot_date,
                uid,
                title,
                subtitle,
                url,
                icon_url,
                last_modified,
                type,
                certification_type,
                exams,
                levels,
                roles,
                study_guide
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(title)s,
                %(subtitle)s,
                %(url)s,
                %(icon_url)s,
                %(last_modified)s,
                %(type)s,
                %(certification_type)s,
                %(exams)s,
                %(levels)s,
                %(roles)s,
                %(study_guide)s
            )
        """,
        "columns": (
            "uid",
            "title",
            "subtitle",
            "url",
            "icon_url",
            "last_modified",
            "type",
            "certification_type",
            "exams",
            "levels",
            "roles",
            "study_guide",
        ),
    },
    "mergedCertifications": {
        "delete": "DELETE FROM merged_certifications WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO merged_certifications (
                snapshot_date,
                uid,
                title,
                summary,
                url,
                icon_url,
                last_modified,
                type,
                certification_type,
                products,
                levels,
                roles,
                subjects,
                renewal_frequency_in_days,
                prerequisites,
                skills,
                recommendation_list,
                study_guide,
                exam_duration_in_minutes,
                locales,
                providers,
                career_paths,
                practice_assessment_uid
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(title)s,
                %(summary)s,
                %(url)s,
                %(icon_url)s,
                %(last_modified)s,
                %(type)s,
                %(certification_type)s,
                %(products)s,
                %(levels)s,
                %(roles)s,
                %(subjects)s,
                %(renewal_frequency_in_days)s,
                %(prerequisites)s,
                %(skills)s,
                %(recommendation_list)s,
                %(study_guide)s,
                %(exam_duration_in_minutes)s,
                %(locales)s,
                %(providers)s,
                %(career_paths)s,
                %(practice_assessment_uid)s
            )
        """,
        "columns": (
            "uid",
            "title",
            "summary",
            "url",
            "icon_url",
            "last_modified",
            "type",
            "certification_type",
            "products",
            "levels",
            "roles",
            "subjects",
            "renewal_frequency_in_days",
            "prerequisites",
            "skills",
            "recommendation_list",
            "study_guide",
            "exam_duration_in_minutes",
            "locales",
            "providers",
            "career_paths",
            "practice_assessment_uid",
        ),
    },
    "exams": {
        "delete": "DELETE FROM exams WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO exams (
                snapshot_date,
                uid,
                title,
                subtitle,
                display_name,
                url,
                icon_url,
                pdf_download_url,
                practice_assessment_url,
                practice_test_url,
                locales,
                last_modified,
                type,
                courses,
                levels,
                roles,
                products,
                providers,
                study_guide
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(title)s,
                %(subtitle)s,
                %(display_name)s,
                %(url)s,
                %(icon_url)s,
                %(pdf_download_url)s,
                %(practice_assessment_url)s,
                %(practice_test_url)s,
                %(locales)s,
                %(last_modified)s,
                %(type)s,
                %(courses)s,
                %(levels)s,
                %(roles)s,
                %(products)s,
                %(providers)s,
                %(study_guide)s
            )
        """,
        "columns": (
            "uid",
            "title",
            "subtitle",
            "display_name",
            "url",
            "icon_url",
            "pdf_download_url",
            "practice_assessment_url",
            "practice_test_url",
            "locales",
            "last_modified",
            "type",
            "courses",
            "levels",
            "roles",
            "products",
            "providers",
            "study_guide",
        ),
    },
    "courses": {
        "delete": "DELETE FROM courses WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO courses (
                snapshot_date,
                uid,
                course_number,
                title,
                summary,
                duration_in_hours,
                url,
                icon_url,
                locales,
                last_modified,
                type,
                levels,
                roles,
                products,
                study_guide,
                recommendation_list,
                certification,
                exam
            ) VALUES (
                %(snapshot_date)s,
                %(uid)s,
                %(course_number)s,
                %(title)s,
                %(summary)s,
                %(duration_in_hours)s,
                %(url)s,
                %(icon_url)s,
                %(locales)s,
                %(last_modified)s,
                %(type)s,
                %(levels)s,
                %(roles)s,
                %(products)s,
                %(study_guide)s,
                %(recommendation_list)s,
                %(certification)s,
                %(exam)s
            )
        """,
        "columns": (
            "uid",
            "course_number",
            "title",
            "summary",
            "duration_in_hours",
            "url",
            "icon_url",
            "locales",
            "last_modified",
            "type",
            "levels",
            "roles",
            "products",
            "study_guide",
            "recommendation_list",
            "certification",
            "exam",
        ),
    },
    "levels": {
        "delete": "DELETE FROM levels WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO levels (
                snapshot_date,
                id,
                name
            ) VALUES (
                %(snapshot_date)s,
                %(id)s,
                %(name)s
            )
        """,
        "columns": (
            "id",
            "name",
        ),
    },
    "products": {
        "delete": "DELETE FROM products WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO products (
                snapshot_date,
                id,
                name,
                children
            ) VALUES (
                %(snapshot_date)s,
                %(id)s,
                %(name)s,
                %(children)s
            )
        """,
        "columns": (
            "id",
            "name",
            "children",
        ),
    },
    "roles": {
        "delete": "DELETE FROM roles WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO roles (
                snapshot_date,
                id,
                name
            ) VALUES (
                %(snapshot_date)s,
                %(id)s,
                %(name)s
            )
        """,
        "columns": (
            "id",
            "name",
        ),
    },
    "subjects": {
        "delete": "DELETE FROM subjects WHERE snapshot_date = %s",
        "insert": """
            INSERT INTO subjects (
                snapshot_date,
                id,
                name,
                children
            ) VALUES (
                %(snapshot_date)s,
                %(id)s,
                %(name)s,
                %(children)s
            )
        """,
        "columns": (
            "id",
            "name",
            "children",
        ),
    },
}

def _to_postgres_value(value):
    if isinstance(value, (dict, list)):
        return Jsonb(value)
    return value

def _prepare_row(item, columns, snapshot_date):
    row = {
        column: _to_postgres_value(item.get(column))
        for column in columns
    }
    row["snapshot_date"] = snapshot_date
    return row

def load_tables(date_today):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT raw_data FROM raw_data
                WHERE snapshot_date = %s
                """,
                (date_today,),
            )

            raw_data = cur.fetchone()["raw_data"]

            for section, load in SECTION_LOADS.items():
                cur.execute(load["delete"], (date_today,))
                cur.executemany(
                    load["insert"],
                    [
                        _prepare_row(item, load["columns"], date_today)
                        for item in raw_data[section]
                    ],
                )