# Auto-script

>Initiative for creating easy auto scripts
Snippets are reusable with little or no changes . If you are new to programming or simply interested in learning different scripts, here are some resources you can use.

:blush: Feel free to contribute, fork, star

Table of Content
--
* [Markdown Cheatsheet](./tipsandtricks/markdown)
* [Secret of Javascript Ninja](./tipsandtricks/js/secretofjavascriptninja)
* [Graphviz](programminglang/python/README.md)

##### Google's Webp Conversion (2019-05-21)
- https://www.archlinux.org/packages/extra/x86_64/libwebp/ (archlinux)
- command to convert webp to png: 

    `cwebp -q 80 image.png -o image.webp`
- command to convert png to webp: 

    `dwebp image.webp -o image.png`


Design Tools
============

- Pencil/quickMockup/Balsamiq (design prototyping tool (wireframe))
- Gimp (raster image) Adobe Photoshop
- Inkscape (vector image) Adobe Illustrator
- Darktable/LightZone (Photographer for manage files) Adobe LightRoom
- Scribus (Page Layou Program) Adobe Indesign
- Ardour/Audacity(Audio mix) Adobe Audition
- Synfig Studio (2D Animation Software) Adobe Animate
- Fusion/Natron  (visual effects, 3D, VR and motion graphics solution) Adobe After Effects 
- Kdenlive/DaVinci Resolve/OpenShot ((filming)professional 8K editing, color correction, visual effects and audio post production) Adobe Premiere
- Aptana Studio/Brackets  (IDE for web application) Adobe DreamWeaver
- Blender (modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game creation) 3D Studio / Maya
- FreeCad/LibreCad ((build machine cars)3D modeler made primarily to design real-life objects of any size.) AutoCad
- Sweet Home 3D (interior design application that helps you draw the plan of your house) Sketchup 3D

- ##### Extra design Prototyping tools
    - Online:
        - InVision
        - Figma
        - Marvel
    - Offline:
        - Gravit Designer(best)
        - Alva
        - Akira
    
- https://uxplanet.org/open-design-freeware-tools-for-designers-f7bdde99f2e0

### Delete Migration files
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```
## django-tenant-schemas
```
# DUMP DATA
./manage.py tenant_command dumpdata --schema="schema-name" app_name.model_name --indent 4 > fixtures/dump.json
# LOAD DATA
./manage.py tenant_command loaddata --schema=schema_name dump.json 
# with out foreignkey and natural key
python manage.py tenant_command dumpdata --natural-foreign --natural-primary --schema="schema_name" app.modelname
./manage.py tenant_command dumpdata --schema="gvn" app.modelname --natural-foreign --natural-primary --indent 4 > dump.json
```

### Git
Use aliases. Though there aren't any native Git one-liners, you can define your own as

git config --global alias.clone-branches '! git branch -a | sed -n "/\/HEAD /d; /\/master$/d; /remotes/p;" | xargs -L1 git checkout -t'
and then use it as

git clone-branches
### Archlinux
* [Read Me](./archlinux/ArchLinux.md)

### Aws
* [Upload File in Aws](./aws/upload_file_aws.py)

### OAuth Google
```
Authorized JavaScript origins = http://localhost:8000
Authorized redirect URIs = http://localhost:8000/complete/google-oauth2/
```

### Serve frontend locally
```
   npm install -g serve
   serve -s dist
```

### OhoDomain in netlify
- manage nameserver default is,
```
ns1: ohodomain.earth.orderbox-dns.com
ns2: ohodomain.mars.orderbox-dns.com
ns3: ohodomain.mercury.orderbox-dns.com
ns4: ohodomain.venus.orderbox-dns.com

with
dns1.p04.nsone.net
dns2.p04.nsone.net
dns3.p04.nsone.net
dns4.p04.nsone.net
```

- manage dns with type A record ip: 104.198.14.52
- domain forward with destination nepex.netlify.com


### Commandline
* [Zsh config](./commandline/zsh/.zshrc)
* [Unix Command](./commandline/unix-command/readme.md)
* [Read Me](./commandline/readme.md)

### Django tenant

- Migrate `./manage.py migrate_schemas --shared  # migrate database to public schema`
- Open Shell `./manage.py shell`
```
from apps.customer.models import Client 
   ...: # create your public tenant 
   ...: tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here 
   ...:                 schema_name='website', # change to app name or suitable schema name otherwise tenant doesnot migrate
   ...:                 name='Schemas Inc.', # organization name
   ...:                 paid_until='2016-12-05', 
   ...:                 on_trial=False) # for later use: billing purpose
   ...: tenant.save()      
   create client now
```
- create superuser`./manage.py createsuperuser --schema=website`


### Add frontend dist to gh-pages(automated)
```
npm install push-dir --save-dev
In package.json, "deploy": "push-dir --dir=dist --branch=gh-pages --cleanup",
npm run generate
npm run deploy
```

### Error (Archlinux)
- while update, unable to lock database
    - sudo rm /var/lib/pacman/db.lck
    
### Responsive Breakpoints

For optimal user experience, material design user interfaces should adapt layouts for the following breakpoint widths: 480, 600, 840, 960, 1280, 1440, and 1600dp.

### Docker
* [Read Me](./docker/readme.md)

### Python
* [Thread](programminglang/python/thread.py)
* [Read Me](programminglang/python/readme.md)

### Server
* [nginx config](./server_setup/nginx_setup/nginx.conf)
* [gunicorn config](./server_setup/nginx_setup/gunicorn.service)

### Handy Commands
[Handy Commnads](./HandyCommands)

### Genymotion Installation
In Archlinux, copy url of snapshot from AUR 

- `https://aur.archlinux.org/cgit/aur.git/snapshot/genymotion.tar.gz`
- `wget https://aur.archlinux.org/cgit/aur.git/snapshot/genymotion.tar.gz`
- `$ cd genymotion.tar.gz`
- `$ makepkg -sri`

Make sure to install 

- `virtualbox-host-dkms`
- `$ sudo pacman -S linux-headers`
- `$ sudo vboxreload`

### Android Installation
- `bash <(curl -s archibold.io/install/android)`
- Put in .bashrc or .zshrc

- `export ANDROID_HOME="/opt/android-sdk"`  
- `export JAVA_HOME="/usr/lib/jvm/java-8-openjdk/"`

- `sudo $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools" "build-tools;25.0.3" "extras;android;m2repository" "extras;google;m2repository"`
- `npm install -g nativescript --unsafe-perm`

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

### Jekyll 
- `bundle install`
- `bundle exec jekyll serve`

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

### Frontend locally run
- `npm install -g serve`
- `serve -s dist`

### VSCODE
When commenting a line, move the cursor to the next line
Use geddski.macros extension:
- `Add macro to settings.json -- "macros": { "commentLine": ["editor.action.commentLine","cursorDown"] }`

- `Map a key in keybindings.json (use you own favorite key combo) -- { "key": "ctrl+/", "command": "macros.commentLine", "when": "editorTextFocus && !editorReadonly" }`

### Reference
* [How to configure](https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
* [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-a-gunicorn-systemd-service-file)
