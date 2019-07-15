#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
# use os.environ['DJANGO_SECRET_KEY'] in django project
export DJANGO_SECRET_KEY="ix5r-2$77vh&kfze(v8!tk^m+25nvsrn=!xq^v+_%q+fo7)8c7"
export SCHOOL_NAME="Nepex Group School"
export ZSH=$HOME/.oh-my-zsh
zsh
#export DJANGO_SECRET_KEY='ix5r-2$77vh&kfze(v8!tk^m+25nvsrn=!xq^v+_%q+fo7)8c7'

[ -s "/home/vimm/.scm_breeze/scm_breeze.sh" ] && source "/home/vimm/.scm_breeze/scm_breeze.sh"
