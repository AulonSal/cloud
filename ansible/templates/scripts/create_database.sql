-- Do not question the quotes in this file
CREATE DATABASE "{{ steward_db_database }}";
DO $$
BEGIN
	CREATE USER "{{ steward_db_user }}" WITH PASSWORD '{{ steward_db_password }}';
	EXCEPTION WHEN DUPLICATE_OBJECT THEN
	RAISE NOTICE 'not creating role {{ steward_db_user }} -- it already exists';
END
$$;
ALTER ROLE "{{ steward_db_user }}" SET client_encoding TO 'utf8';
ALTER ROLE "{{ steward_db_user }}" SET default_transaction_isolation TO 'read committed';
ALTER ROLE "{{ steward_db_user }}" SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE "{{ steward_db_database }}" TO "{{ steward_db_user }}";

