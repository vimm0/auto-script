# Auto-script

Initiative for creating easy auto scripts

Configs are reusable with little or no changes . If you are new to programming or simply interested in learning different scripts, here are some resources you can use.

### Archlinux
* [Read Me](./archlinux/ArchLinux.md)

### Aws
* [Upload File in Aws](./aws/upload_file_aws.py)

### Commandline
* [Zsh config](./commandline/zsh/.zshrc)
* [Unix Command](./commandline/unix-command/readme.md)
* [Read Me](./commandline/readme.md)

### Docker
* [Read Me](./docker/readme.md)

### Python
* [Thread](./python/thread.py)
* [Read Me](./python/readme.md)

### Server
* [nginx config](./server_setup/nginx_setup/nginx.conf)
* [gunicorn config](./server_setup/nginx_setup/gunicorn.service)

### Handy Commands
[Handy Commnads](./HandyCommands)

### Open Source Projects

- export SECRET_KEY = 'secret-key'   # Make sure to not include $ in secret key
- create user and database in psql (also provide login, superuser permissison)

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

```./manage.py migrate```

- And npm install [more](https://saleor.readthedocs.io/en/latest/gettingstarted/installation-linux.html#installation-for-linux)

### Genymotion Installation
In Archlinux, copy url of snapshot from AUR `https://aur.archlinux.org/cgit/aur.git/snapshot/genymotion.tar.gz`
- `wget https://aur.archlinux.org/cgit/aur.git/snapshot/genymotion.tar.gz`
- `$ cd genymotion.tar.gz`
- `$ make -sri`

Make sure to install `virtualbox-host-dkms`
- `$ sudo pacman -S linux-headers`
- `$ sudo vboxreload`

### Android Installation
- `$ bash <(curl -s archibold.io/install/android)`
Put in .bashrc or .zshrc
- `$ export ANDROID_HOME="/opt/android-sdk"`  
- `$ export JAVA_HOME="/usr/lib/jvm/java-8-openjdk/"`

- `$ sudo $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools" "build-tools;25.0.3" "extras;android;m2repository" "extras;google;m2repository"`
- `$ npm install -g nativescript --unsafe-perm

- [more](https://medium.com/@WebReflection/testing-nativescript-on-arch-linux-a19511cd9521)`

### Reference
* [How to configure](https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
* [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-a-gunicorn-systemd-service-file)
