# Simple Commands
- `date`: print or set the system date and time
- `cal`: display a calendar
- `df`: report file system disk space usage
- `free`: Display amount of free and used memory in the system
- `cd` : change the working directory
- `ls` : list directory contents
- `gdb` : The GNU Debugger
- `file` : determine file type
- `less` : view file content (opposite of more)

## System Information
- `uname` : print system information
    - #### shortcuts
        - `uname -a`
        - `uname -r`
- `cat /etc/<system>-release` :Show which version of system installed
- `uptime` : Tell how long the system has been running.
- `hostname` : show or set system host name
    - #### shortcuts
        - `hostname -i`
- `last reboot` : Show system reboot history
- `date`: print or set the system date and time
- `cal`: display a calendar
- `w` : Show who is logged on and what they are doing.
- `whoami` : print effective userid

## Hardware Information
- `dmesg` : print or control the kernel ring buffer
- `cat /proc/cpuinfo`: Display CPU information
- `cat /proc/meminfo` : Display memory information
- `free -h` : Display free and used memory ( -h for human readable, -m for MB, -g for GB.)
- `lspci -tv`: Display PCI devices
- `lsusb -tv` : Display USB devices
- `dmidecode` : Display DMI/SMBIOS (hardware info) from the BIOS
- `hdparm -i /dev/sda` : Show info about disk sda
- `hdparm -tT /dev/sda` : Perform a read speed test on disk sda
- `badblocks -s /dev/sda` : Test for unreadable blocks on disk sda

## PERFORMANCE MONITORING AND STATISTICS
- `top` : display Linux processes
- `htop` :  interactive process viewer
- `mpstat 1` : Display processor related statistics
- `vmstat 1` : Display virtual memory statistics
- `iostat 1` : Display I/O statistics
- `tail 100 /var/log/messages` : Display the last 100 syslog messages  (Use /var/log/syslog for Debian based systems.)
- `tcpdump -i eth0` : Capture and display all packets on interface eth0
- `tcpdump -i eth0 'port 80'` : Monitor all traffic on port 80 ( HTTP )
- `lsof` : List all open files on the system
    - #### shortcuts
        - `lsof -u user` : List files opened by user
- `watch df -h` : Execute "df -h", showing periodic updates

## USER INFORMATION AND MANAGEMENT
- `id` : print real and effective user and group IDs
- `last` or `lastb` : show a listing of last logged in users
- `who` : show who is logged on
- `w` : Show who is logged on and what they are doing.
- `groupadd` : create a new group
- `useradd` : create a new user or update default new user information
- `userdel` : delete a user account and related files
- `usermod` : modify a user account

## FILE AND DIRECTORY COMMANDS
- `mkdir` :  make directories
- `rm` : remove files or directories
- `cp` : copy files and directories
- `mv` : move (rename) files
- `ln` : make links between files
- `touch` : change file timestamps
- `cat` : concatenate files and print on the standard output
- `less` : opposite of more (Browse through a text file)
- `head` : output the first part of files
- `tail`: output the last part of files
- `pwd` : print name of current/working directory
- `ls` : list directory contents
	- #### shortcuts
		- `ls <directory-1> <directory-2>` : list content in multiple direcotry `directory-1` and `directory-2`
- `cd` : change the working directory
	- cd `<absolute-path>|<relative-path>`
	- absolute-path: path starts from root directory
	- relative-path: path starts from working directory
	- #### shortcuts
		- `cd -` : changes the working direcotry to the previous working directory
		- `cd ~username` : changes the working directory to the home direcotry of username. For example, cd ~vimm changes the directory to the home directory of user vimm.
		- 

## PROCESS MANAGEMENT
- `ps` : report a snapshot of the current processes.
	- #### shortcuts
	    - `ps -ef` : Display all the currently running processes on the system.
        - `ps -ef | grep <processname>` : Display process information for processname
- `kill` : terminate a process
	- #### shortcuts
        - `kill pid` : Kill process with process ID of pid
        - `killall <processname>` : Kill all processes named processname
- `<program> &` : Start program in the background
- `bg` : Display stopped or background jobs
- `fg` : Brings the most recent background job to foreground
	- #### shortcuts
        - `fg n` : Brings job n to the foreground

## NETWORKING
- `ifconfig` : configure a network interface
	- #### shortcuts
        - `ifconfig -a` :  Display all network interfaces and ip address
        - `ifconfig eth0` : Display eth0 address and details
- `ethtool eth0` : Query or control network driver and hardware settings
- `ping host` : Send ICMP echo request to host
- `whois domain` : Display whois information for domain
- `dig domain` : Display DNS information for domain
- `dig -x IP_ADDRESS` : Reverse lookup of IP_ADDRESS
- `host domain`
- `wget http://domain.com/file` : Download http://domain.com/file
- `netstat -tulnp` : Display listening tcp and udp ports and corresponding programs

## ARCHIVES
- `tar`: an archiving utility
	- #### shortcuts
        - `tar cf archive.tar directory` : Create tar named archive.tar containing directory.
        - `tar xf archive.tar` : Extract the contents from archive.tar.
        - `tar czf archive.tar.gz directory` : Create a gzip compressed tar file name archive.tar.gz.
        - `tar xzf archive.tar.gz` : Extract a gzip compressed tar file.
        - `tar cjf archive.tar.bz2 directory` : Create a tar file with bzip2 compression
        - `tar xjf archive.tar.bz2` : Extract a bzip2 compressed tar file.

## SEARCH
- `grep`, `egrep`, `fgrep` - print lines that match patterns
	- #### shortcuts
        - `grep pattern file` : Search for pattern in file
        - `grep -r pattern directory` : Search recursively for pattern in directory
- `locate` : find files by name
	- #### shortcuts
        - `locate name` : Find files and directories by name
- `find` : search for files in a directory hierarchy
	- #### shortcuts
    - `find /home/john -name 'prefix*'` : Find files in /home/john that start with "prefix".
    - `find /home -size +100M` : Find files larger than 100MB in /home

## SSH LOGINS
- `ssh` : OpenSSH SSH client (remote login program)
	- #### shortcuts
        - `ssh host` : Connect to host as your local username.
        - `ssh user@host` : Connect to host as user
        - `ssh -p port user@host` : Connect to host using port

## FILE TRANSFERS
- `scp` : secure copy (remote file copy program)
	- #### shortcuts
        - `scp file.txt server:/tmp` : Secure copy file.txt to the /tmp folder on server
        - `scp server:/var/www/*.html /tmp` : Copy *.html files from server to the local /tmp folder.
        - `scp -r server:/var/www /tmp` : Copy all files and directories recursively from server to the current system's /tmp folder.
- `rsync` : a fast, versatile, remote (and local) file-copying tool
	- #### shortcuts
        - `rsync -a /home /backups/` : Synchronize /home to /backups/home
        - `rsync -avz /home server:/backups/` : Synchronize files/directories between the local and remote system with compression enabled

## DISK USAGE
- `df`: report file system disk space usage
	- #### shortcuts
        - `df -h` : Show free and used space on mounted filesystems
        - `df -i` : Show free and used inodes on mounted filesystems
- `fdisk` : manipulate disk partition table
	- #### shortcuts
        - `fdisk -l` : Display disks partitions sizes and types
- `du` : estimate file space usage
	- #### shortcuts
        - `du -ah` : Display disk usage for all files and directories in human readable format
        - `du -sh`: Display total disk usage off the current directory
