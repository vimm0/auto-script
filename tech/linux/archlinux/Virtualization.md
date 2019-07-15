
###### https://unix.stackexchange.com/questions/202396/manjaro-module-vboxdrv-not-found

```
pacman -S linux-headers
pacman -S virtualbox virtualbox-guest-iso

vim /etc/modules-load.d/virtualbox.conf
add `vboxdrv vboxnetadp vboxnetflt`

sudo modprobe --verbose --force-vermagic vboxdrv vboxnetadp vboxnetflt
```
