# Add the global configurations
if [ -e /etc/bashrc ] ; then
   source /etc/bashrc
fi


# Add the alias configurations
if [ -f ~/.bash_aliases ] ; then
   source ~/.bash_aliases
fi

export TERM=xterm-256color

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi


# ECMA-48 Set Graphics Rendition (SGR) Sequences
# See: man console_codes for further reference
# Define the ANSI graphics colors to use with the console
   lightred="\[\033[1;31m\]"
 lightgreen="\[\033[1;32m\]"
lightyellow="\[\033[1;33m\]"
  lightblue="\[\033[1;34m\]"
    magenta="\[\033[1;35m\]"
       cyan="\[\033[1;36m\]"
      white="\[\033[1;37m\]"

    darkred="\[\033[0;31m\]"
  darkgreen="\[\033[0;32m\]"
     violet="\[\033[0;35m\]"
 aquamarine="\[\033[0;36m\]"
  darkwhite="\[\033[0;37m\]"

    nocolor="\[\033[0m\]"

# See: man bash, search for PROMPTING for parameter reference
PS1="${lightgreen}[${cyan}\u${white}@${magenta}\h${lightblue}:\W${lightgreen}]${nocolor}$ "

# Set background color
printf %b '\e]11;#000000\a'

# Add user bin and user script to path
export PATH="${PATH}":/home/${USER}/bin:/data/scripts

# Configure the default editor
export EDITOR=vi

# Configure the shell windows not to timeout
export TMOUT=0

# ======================================================
# ---------- BEGIN: Less Colors For Man Pages ----------
# ======================================================
# Begin Blinking
export LESS_TERMCAP_mb=$'\E[01;31m'

# Begin Bold
export LESS_TERMCAP_md=$'\E[01;38;5;74m'

# End Mode
export LESS_TERMCAP_me=$'\E[0m'

# End Standout-Mode
export LESS_TERMCAP_se=$'\E[0m'

# Begin Standout-Mode - Info Box
export LESS_TERMCAP_so=$'\E[38;5;246m'

# End Underline
export LESS_TERMCAP_ue=$'\E[0m'

# Begin Underline
export LESS_TERMCAP_us=$'\E[04;38;5;146m'

# ====================================================
# ---------- END: Less Colors For Man Pages ----------
# ====================================================
