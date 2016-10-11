Install
=========

sudo apt install postgresql-server-dev-all postgresql postgresql-contrib

psql -U postgres

CREATE ROLE system_user WITH LOGIN ENCRYPTED PASSWORD 'password' CREATEDB;

createdb project_slug

