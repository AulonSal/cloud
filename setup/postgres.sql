CREATE DATABASE "steward";
CREATE USER "steward" WITH PASSWORD 'thestewardpassword$blue';
ALTER ROLE "steward" SET client_encoding TO 'utf8';
ALTER ROLE "steward" SET default_transaction_isolation TO 'read committed';
ALTER ROLE "steward" SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE "steward" TO "steward";

