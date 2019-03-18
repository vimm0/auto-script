#### Server Setup
```
EC2 (python project):
    jus/
    - app/ --> django project
    - conf/ --> nginx, circusctl. gunicorn
    - logs/ --> all log files
    - index.html <-- use rsync

    use:
    - boto3 in place of os in python
    - fabfile {gps, rsync --> index.html}

    S3:
    - media/
    - static/
    use:
    - django-storage to upload static and media files
```

##### server
```
mkdir repo.git app conf logs media static
cd repo.git
git init --bare
git --bare update-server-info
git config core.bare false
git config receive.denycurrentbranch ignore
git config core.worktree /home/{user}/app/
cat > hooks/post-receive
#!/bin/sh
git checkout -f
cd ../app
./deploy.sh
$ chmod +x hooks/post-receive
```

ssh username@domainname.com -p portnum

ssh-copy-id username@domainname.com
##### Create link between local repo and remote:
```
git remote add server ssh://username@domainname.com:portnum/home/jus/repo.git/
```

To push into remote
```
git push server --all
```

```
sudo apt-get update
sudo apt-get install virtualenv python-pip python-dev libpq-dev postgresql postgresql-contrib nginx
```

create virtualenv
install production requirement dependency via pip
Note: You have to install django and gunicorn in the same environment.

Change database setting for postgres, static, media, migrate and createsuperuser

```
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . .]
```

##### Create the PostgreSQL Database and User
```
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```


##### sudo nano /etc/systemd/system/gunicorn.service
```

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User={user-name}
Group=www-data
WorkingDirectory=/home/path/to/app
ExecStart=/home/path/to/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/path/to/sock/{project-name}.sock {project-name}.wsgi:application

[Install]
WantedBy=multi-user.target

```

##### Configure Nginx to Proxy Pass to Gunicorn
sudo nano /etc/nginx/sites-available/{project-name}
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/path/to/static;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/path/to/sock/{project-name}.sock;
    }
}
```

sudo ln -s /etc/nginx/sites-available/{project-name} /etc/nginx/sites-enabled
sudo ufw allow 'Nginx Full'

##### Handy command
```
sudo systemctl stop gunicorn
sudo systemctl stop ngnix
sudo systemctl start gunicorn
sudo systemctl start ngnix

sudo systemctl enable gunicorn
sudo systemctl status gunicorn

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo service nginx restart

sudo journalctl -u gunicorn
```



sudo fuser -k 443/tcp

circus --> systemctl

chaussette --> gunicorn

#### Reference

- [GIST 9691385](https://gist.github.com/thomasfr/9691385)

- [Django, nginx, gunicorn setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
