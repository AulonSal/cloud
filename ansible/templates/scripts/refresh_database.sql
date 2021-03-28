-- first drop all connections to the database
select pg_terminate_backend(pid) from pg_stat_activity where datname="{{ steward_db_database }}";

\i drop_database.sql
\i create_database.sql

