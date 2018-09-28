# Archlinux

Create Hotspot

`sudo systemctl start ModemManager.service && sudo systemctl enable ModemManager.service`

`sudo passwd -d 'whoami'`
## zsh setup
`sudo pacman -S zsh git`
`sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`

## Ssh setup
- `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
- `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_rsa`
- `sudo pacman -S xclip`
- `xclip -sel clip < ~/.ssh/id_rsa.pub`
- paste public key to Git repositories

Reference
- [Create Wifi Gnome3](https://unix.stackexchange.com/questions/118267/create-a-wifi-hotspot-on-gnome-3-arch-linux)
