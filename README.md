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
- `$ makepkg -sri`

Make sure to install `virtualbox-host-dkms`
- `$ sudo pacman -S linux-headers`
- `$ sudo vboxreload`

### Android Installation
- `$ bash <(curl -s archibold.io/install/android)`
Put in .bashrc or .zshrc
- `$ export ANDROID_HOME="/opt/android-sdk"`  
- `$ export JAVA_HOME="/usr/lib/jvm/java-8-openjdk/"`

- `$ sudo $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools" "build-tools;25.0.3" "extras;android;m2repository" "extras;google;m2repository"`
- `$ npm install -g nativescript --unsafe-perm`

- [more](https://medium.com/@WebReflection/testing-nativescript-on-arch-linux-a19511cd9521)

### Android Studio
- ` yaourt -S android-studio`
- `yaourt -S android-tools android-udev`
- `sudo gpasswd -a awecode adbusers`
- `yaourt -S genymotion`
- `uname -r`
- `yaourt linux-headers`
- `restart`
- `open android studio`

To increase size of tmp/ (in case No space left on device warning came up)
- `mount -o remount,size=5G /tmp/`

### Weex build
- `git clone https://github.com/tralves/weex-todo-list 204`
- `yarn (or npm install)`
- `yarn build (or npm run build)`
- `yarn copy:android (or npm run copy:android)`
- `open android folder in Android Studio`
- `Either run app or build apk!`

### Dependency installer for ruby:
For installing bundler system-wide. To do this, you need to pass --no-user-install flag to gem and execute it with sudo:
`sudo gem install bundler --no-user-install`
[Stack Overflow](https://stackoverflow.com/questions/28072128/zsh-command-not-found-bundle-after-gem-install-bundle)


### Nested Grid Vuetify
```
 <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-layout>
        <v-flex xs6>
          <v-layout row>
            <v-layout justify-center>
              <v-flex xs6>
                <v-card dark color="secondary">
                  <v-card-text class="px-0">6</v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout justify-end>
              <v-flex xs6>
                <v-card dark color="secondary">
                  <v-card-text class="px-0">6</v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-layout>
        </v-flex>
        <v-layout justify-center>
          <v-flex xs6>
            <v-card dark color="secondary">
              <v-card-text class="px-0">6</v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-layout>
    </v-layout>
  </v-container>

```
### ngrok http host-header
`ngrok http 8080 -host-header="localhost:8080"`

### Package Manager
- `yarn upgrade-interactive --latest`
- `yarn upgrade --latest`

### Devnagiri fonts in archlinux
`sudo yaourt -S ttf-indic-otf`

### Daemonize
- `redis-server --daemonize yes`
- `ps aux | grep redis-server`

### Dockerize
- `sudo usermod -a -G docker $USER`


### VSCODE
When commenting a line, move the cursor to the next line
Use geddski.macros extension:
- `Add macro to settings.json -- "macros": { "commentLine": ["editor.action.commentLine","cursorDown"] }`

- `Map a key in keybindings.json (use you own favorite key combo) -- { "key": "ctrl+/", "command": "macros.commentLine", "when": "editorTextFocus && !editorReadonly" }`

### Reference
* [How to configure](https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
* [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-a-gunicorn-systemd-service-file)
