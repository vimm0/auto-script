```
sudo -i -u postgres
~$ createuser saleor
~$ createdb saleor
OR
~$ createdb -O saleor saleor
~$ psql
ALTER ROLE "asunotest" WITH LOGIN;
ALTER USER saleor WITH NOSUPERUSER
```