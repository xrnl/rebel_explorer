# Rebel Explorer

Sign-up statistics & contact details of Extinction Rebellion members.

## prerequisites

Python 3.6

PostgreSQL. If you are on MacOS you can install it with [Homebrew](https://brew.sh/)

```bash
brew update
brew install postgresql
```


## installation

Clone or download repository onto local computer

```bash
git clone https://github.com/xrnl/rebel_explorer.git
```

install necessary requirements with pip (preferably in a virtualenv, to avoid conflicts with existing packages in your computer)

```bash
cd rebel_explorer
pip install -r requirements.txt
```

## running

### create database

start postgres

```bash
brew services start postgresql
```
create database

```bash
psql postgres
postgres=# create database "rebel_explorer";
```
run migrations to create tables in the database

```bash
python manage.py db upgrade
```
## development

### database migrations

If you make changes to the database schema you can apply the changes to the database using `flask-migrate`

```bash
python manage.py db migrate
python manage.py db upgrade
```

It is recommended to review the migrations file created at `migrations/versions` after running `db migrate` to make sure that the right migrations have been created and make any changes that are necessary. Once the migrations are in the correct state you can run `db upgrade` to apply the migrations to the databse. An example when this may be necessary is when you rename tables or columns, in which case flask-migrate will not notice the changes.

## testing

run unit tests with the following command

```bash
python run_tests.py
```
