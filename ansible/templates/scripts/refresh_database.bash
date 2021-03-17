export PGPASSWORD="{{ postgres_safe_password }}"

psql \
	--host="{{ steward_db_host }}" \
	--username="{{ postgres_user }}" \
	--dbname="{{ postgres_database }}" \
	-f refresh_database.sql

