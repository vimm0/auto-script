`youtube-dl --extract-audio --audio-format mp3 <video URL>`

`youtube-dl --extract-audio -i --audio-format mp3 --audio-quality 0 --no-part --no-mtime --embed-thumbnail --add-metadata <video URL>`

##### No space left on device archlinux
`mount -o remount,size=4G,noatime /tmp`

##### Remove rood password (use sudo without password) 
`sudo passwd -u root`

##### start guake at start
`cp /usr/share/applications/guake.desktop /etc/xdg/autostart/`

After you copied fonts it's very important to call the command  `sudo fc-cache -fv` otherwise wine will not see these fonts (of will see, but after restarting of your system)
