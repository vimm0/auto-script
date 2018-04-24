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