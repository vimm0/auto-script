# Archlinux

Create Hotspot

- `sudo systemctl start ModemManager.service && sudo systemctl enable ModemManager.service`

`sudo passwd -d 'whoami'`
## zsh setup
- `sudo pacman -S zsh git zsh-completions`
- `sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`
- In bashrc,`export ZSH=$HOME/.oh-my-zsh` and `zsh`

## Ssh setup
- `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
- `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_rsa`
- `sudo pacman -S xclip`
- `xclip -sel clip < ~/.ssh/id_rsa.pub`
- paste public key to Git repositories

### Java in Archlinux
- `pacman -S jdk8-openjdk`

### Full Stack Developer
- ```plugins=(git git-extras git-flow colored-man colorize github vagrant virtualenv virtualenvwrapper pip python brew osx zsh-syntax-highlighting npm docker django bower celery node sublime sudo supervisor web-search)```
- `yaourt -S python-pip`
- ```git clone git://github.com/ndbroadbent/scm_breeze.git ~/.scm_breeze
  ~/.scm_breeze/install.sh
  source ~/.bashrc   # or source ~/.zshrc```
Reference
- [Create Wifi Gnome3](https://unix.stackexchange.com/questions/118267/create-a-wifi-hotspot-on-gnome-3-arch-linux)
