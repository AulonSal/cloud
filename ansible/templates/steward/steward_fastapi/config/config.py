"""Some vars"""
from os import environ

IS_TEST = bool(environ.get("API_TEST"))

POSTGRES_CREDENTIALS = {
                    'user': '{{ steward_db_user }}',
                    'password': '{{ steward_db_password }}',
                    'host': '{{ steward_db_host }}',
                    'database': '{{ steward_db_database }}',
                    'port': {{ steward_db_port }},
                }

JWT_SECRET_KEY = "{{ steward_jwt_secret_key }}"

