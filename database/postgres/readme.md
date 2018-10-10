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
