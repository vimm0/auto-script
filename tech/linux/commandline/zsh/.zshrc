# Custom zsh command.
# Below .zshrc paste the following script. 

# Temporary Python Virtual Environment
SRC_DIRECTORY="$HOME/envs"
RED='\033[0;31m'
env(){
if [ $1 ]
  then
    virtualenv $SRC_DIRECTORY/$1
    source $SRC_DIRECTORY/$1/bin/activate;
  else
	echo "${RED}Warning: Please, provide new directory name as parameter!"
fi
}

go(){
if [ $1 ]
  then
    source $SRC_DIRECTORY/$1/bin/activate;
  else
	echo "${RED}Warning: Please, provide destination name for source!"
fi
}

nogo(){
	deactivate
	cd ~
}

# Django Aliases
alias d='django-admin.py'
alias dsa='django-admin.py startapp'
alias dsp='django-admin.py startproject'
alias runserver='python manage.py runserver'
alias makemigrations='python manage.py makemigrations'
alias migrate='python manage.py migrate'

