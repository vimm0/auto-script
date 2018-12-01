Install the `postgresql` package.

Following step solved your problem

step 1: create the data directory (acordingly with the PGROOT variable set before in the config file)

`sudo mkdir /var/lib/postgres/data`

Step 2: set /var/lib/postgres/data ownership to user 'postgres'

`chown postgres /var/lib/postgres/data`

Step 3: As user 'postgres' start the database.

```sudo -i -u postgres
initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgres/data'
```

Step 4: Finally, start and enable the postgresql.service

Select database and query table in postgres:
```
\l - list database
\c <database> - connect to database
\dt - list data table
```

#### Tips
```
sudo -i -u postgres
~$ createuser <username>
~$ createdb <projectname>
OR
~$ createdb -O <username> <projectname>
~$ psql
ALTER ROLE "asunotest" WITH LOGIN;
ALTER USER <username> WITH NOSUPERUSER
```

https://lobotuerto.com/blog/how-to-install-postgresql-in-manjaro-linux/
https://wiki.archlinux.org/index.php/PostgreSQL
