# Auto-script

## Always be curious, always read the source material, and always try it yourself.

"learn the basics/roots first" principle applies to pretty much everything in life. From learning a new programming language to starting a new sport. It requires a lot of practice, but once you master it, the only thing left to do is to get creative with it. And that's where the real fun begins.

> Initiative for creating easy auto scripts
> Snippets are reusable with little or no changes . If you are new to programming or simply interested in learning different scripts, here are some resources you can use.

:blush: Feel free to contribute, fork, star

## Table of Content

- [Markdown Cheatsheet](./tipsandtricks/markdown)
- [Secret of Javascript Ninja](./tipsandtricks/js/secretofjavascriptninja)
- [Graphviz](tech/lang/python/README.md)

#### Android development Roadmap 2019
- https://github.com/MindorksOpenSource/android-developer-roadmap
- https://medium.com/mindorks/learning-android-development-in-2019-a-practical-guide-ddc71e008696

Wipe out all the data from pendrive
`sudo dd if=/dev/zero of=/dev/sdb1 bs=1k count=2048`

VanillaJS is the same as pure Javascript.

Vanilla in slang means:

unexciting, normal, conventional, boring

##### Vim configuration
- create ~/.vimrc
	- set mouse=a # helps in mouse action

##### Vim useful shortcuts
- copy from vim to outside vim
	- make sure `set mouse=a` is enabled in `.vimrc`
	- while copying make sure to press shift and then `ctrl+shift+c` to copy
- Split screen
	- Open file
		- :Sex /path/to/file
		- :Vex /path/to/file
	- navigate between screen
		- ctrl+w+v
		- ctrl+w+l
		- ctrl+w+h
		- ctrl+w+s
		- ctrl+w+j
		- ctrl+w+k
	- Change screen size
		- ctrl+w+">" 
		- ctrl+w+"<"
		- ctrl+w+"+"
		- ctrl+w+"="

- Copy/Paste 
	- enter to visual mode with ctrl+v
	- select the block up to which you want to copy and move cursor with h,j,k,l
	- cut (with d) or copy (with y)
	- paste with either p or P
- Editing
	- undo/redo
		- u: undo last change
		- ctrl+r
- reference
	- https://linuxhint.com/how-to-use-vim-split-screen/

##### Video

[Network Penetration Testing for Beginner](https://www.youtube.com/watch?v=3Kq1MIfTWCE)
https://www.youtube.com/watch?v=L6SlXzk3Efo

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

```

##### Types of Application development
- Standalone business application: This is your typical application, and is like applications like Word, Excel, Outlook and more. Anything that can be used by someone to make their work more efficient would fall into this category.
- Client-Server Application: This is an application that runs on the computer but accesses information from a remote server.
- Collaborative Application: This is an application that is designed to help people involved in a common task. This is a way for people to work together at once, using the same application on each of their computers.
- Utilities and Plug-Ins: Anything that can help a computer or browser run more efficiently would fall into this category.
- System Apps and Services: Anything that allows the computer to run various other applications would fall into this category.
- Multimedia Applications: This is an application that plays podcasts, movies, video, music and more. iTunes is a good example of this.
- Network Applications: Anything that runs over a network falls into this category.

##### ssh with two linux computer
- connect with lan cable between two computer
- install, enable, start ssh service
- also compulsary to add password in linux machine
- ping ssh with `ping ipaddress`
- ssh remote linux with `ssh ipaddress`
- `scp -r /file path/to/copy user@ipaddress:/path/to/paste`
- `ls -lh`  //list path with human readable file size

##### Google's Webp Conversion (2019-05-21)

- https://www.archlinux.org/packages/extra/x86_64/libwebp/ (archlinux)
- command to convert webp to png:

  `cwebp -q 80 image.png -o image.webp`

- command to convert png to webp:

  `dwebp image.webp -o image.png`

### Git

Use aliases. Though there aren't any native Git one-liners, you can define your own as

```
git config --global alias.clone-branches '! git branch -a | sed -n "/\/HEAD /d; /\/master$/d; /remotes/p;" | xargs -L1 git checkout -t'
```

and then use it as

git clone-branches

### Arch linux

- [Read Me](tech/linux/archlinux/ArchLinux.md)

### Aws

- [Upload File in Aws](tech/cloudcomputing/aws/upload_file_aws.py)

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

- [Zsh config](tech/linux/commandline/zsh/.zshrc)
- [Unix Command](tech/linux/commandline/unix-command/readme.md)
- [Read Me](tech/linux/commandline/readme.md)

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

- [Read Me](tech/web/fullstack/Backend/docker/readme.md)

### Python

- [Thread](tech/lang/python/thread.py)
- [Read Me](tech/lang/python/readme.md)

### Server

- [nginx config](tech/web/fullstack/Backend/server_setup/nginx_setup/nginx.conf)
- [gunicorn config](tech/web/fullstack/Backend/server_setup/nginx_setup/gunicorn.service)

### Handy Commands

[Handy Commnads](./HandyCommands)

### Dependency installer for ruby:

For installing bundler system-wide. To do this, you need to pass --no-user-install flag to gem and execute it with sudo:
`sudo gem install bundler --no-user-install`
[Stack Overflow](https://stackoverflow.com/questions/28072128/zsh-command-not-found-bundle-after-gem-install-bundle)

### Jekyll

- `bundle install`
- `bundle exec jekyll serve`

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

- [How to configure](https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-a-gunicorn-systemd-service-file)
