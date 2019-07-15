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
