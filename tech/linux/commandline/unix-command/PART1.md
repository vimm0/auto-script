# Process

### List All Processes
- `ps`
- `ps -A`
- `ps au`

### Print Process Tree
- `ps -e --forest`
- `ps -f --forest -C sshd`

### Specify Custom Output Format
- ` ps -eo pid,ppid,user,cmd`

### Troubleshoot Linux System Performance
- `ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head`

### Print Security Information
- `ps --context`
- `ps -eo  euser,ruser,suser,fuser,f,comm,label`

### Perform Real-time Process Monitoring Using Watch Utility

- `watch -n 1 'ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head'`
# Users and Group

Add user
```bash
$ useradd [options] username
$ sudo passwd olivia

$ sudo useradd -m olivia -p PASSWORD
```
Create Group and add user to that group
```bash
$ groupadd [docker] 
$ gpasswd -a [user] [docker] 
```
equivalent to
```bash
$ sudo usermod -a -G [docker] [user]
```
Re-login after executing command
- [replace docker group with your group]
- [replace user with your username]

How to know user in a group
```bash
$ grep [docker] /etc/group
```
