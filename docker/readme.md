# Arch Linux Docker Tutorial

### [A] How to Install Docker on Arch Linux

1. Enable the Loop Module

```
$ lsmod | grep loop
```

```
$ tee /etc/modules-load.d/loop.conf <<< "loop"
$ modprobe loop
```

2. Install Docker

```
$ pacman -S docker
```

3. Start and Enable Docker

```
$ systemctl start docker.service

$ systemctl enable docker.service
```

4. Add docker group and add yourself

```
$ groupadd docker
 
$ gpasswd -a user docker [replace user with your username]
```
### Post-Install Configuration
```
$ systemctl stop docker.service
```
```
ExecStart=/usr/bin/dockerd --data-root=/path/to/new/location/docker -H fd://
```
For more post-install configuration options, see Docker’s official [Arch wiki](https://wiki.archlinux.org/index.php/Docker) page

### Using Docker on Arch Linux

1.First Steps
```
$ docker
$ docker version
$ docker info
```
 

2.Downloading Docker Images

```
$ docker pull base/archlinux

$ docker search [image name]

$ systemctl stop docker.service

$ mkdir /etc/systemd/system/docker.service.d
 
$ touch /etc/systemd/system/docker.service.d/docker.conf
```

```
[Service]
 
ExecStart=
 
ExecStart=/usr/bin/dockerd --graph="/mnt/new_volume" --storage-driver=devicemapper
```
```
$ docker info
$ systemctl daemon-reload
 
$ systemctl start docker.service
```

### Creating New Containers
```
$ docker run [image name] [command to run]
$ docker run [container ID]
$ docker stop [container ID]
$ docker ps
$ docker commit [container ID] [image name]
$ docker rm [container ID]
```

### Monitoring Docker Containers
```
$ docker stats
$ docker stats [container ID] [container ID] [container ID]
$ docker stats --no-steam
$ docker stats --all
```


### Networking Configuration
```
$ docker network ls
    NETWORK ID NAME DRIVER
    7fca4eb8c647 bridge bridge
    9f904ee27bf5 none   null
    cf03ee007fb4 host   host
$ docker network inspect bridge
$ docker network create --driver bridge bridge_new
$ docker network inspect bridge_new
$ docker run --network= bridge_new -itd --name=[container ID] busybox
```

```
SSH Into a Container
$ docker run -d -p 2222:22 \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -e CONTAINER=my-container -e AUTH_MECHANISM=noAuth \
 jeroenpeeters/docker-ssh
$ ssh -p 2222 localhost
$ docker exec -it < mycontainer > bash
```

### Sharing Data Between a Docker Container and the Host
```
$ mkdir ~/container-share
$ docker run -d -P --name test-container -v /home/user/container-share:/data archlinux

$ docker attach [container ID]
```
### [B] How to Install Docker Compose with pip
```
pip install docker-compose
```

If you are not using virtualenv,
```
sudo pip install docker-compose
```
INSTALL AS A CONTAINER
```
$ sudo curl -L --fail https://github.com/docker/compose/releases/download/1.21.0/run.sh -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```
### Reference

[https://linuxhint.com/arch-linux-docker-tutorial/](https://linuxhint.com/arch-linux-docker-tutorial/)
[https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)