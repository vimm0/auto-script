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
- `top`
- `htop`
- `mpstat 1`

## Navigations
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
