# ===============================
# ---------- Locations ----------
# ===============================
export DATA_ROOT="/data"
export WORKSPACE_ROOT="${DATA_ROOT}/dataworkspace"

# =====================================
# ---------- Command Aliases ----------
# =====================================
alias cda='conda activate'
alias cde='conda deactivate'
alias doy='date +"%j"'

# 1. Echo the data that was input
# 2. Format the bytes to display as uppercase with a leading 0x and a trailing comma
# 3. Add the opening and closing braces to the data and remove the last trailing comma
# 4. Add a newline after each 16 bytes of data and indent the next line
alias formhex='h(){ echo $1 | sed -re s"/([a-z0-9]{2})/0x\U\1, /g" | sed -re s"/(.*),/{\n   \1\n};/" | sed -re s"/./&\n  /98;s/./&\n  /197"; unset -f h; }; h'
alias genhex='f(){ formhex $(hexdump -C -s $1 -n $2 $3 | sed -nre s"/([a-f0-9]{8}  )(.*).*  \|.*\|/\2/p" | awk "{ORS=\"\"}{gsub(\" \", \"\", \$0); print}"); unset -f f; }; f'
alias gensha='f(){ formhex $(sha256sum $1 | awk "{print \$1}"); unset -f f; }; f'


# ONLY USED IN CENTOS/RHEL
#alias repoq-all='repoquery -a --qf "%-30{ui_from_repo} %-105{nevra} %{name}"'
#alias repoq-inst='repoquery -a --installed --qf "%-30{ui_from_repo} %-105{nevra} %{name}"'
#alias repoq-pkg-lst='repoquery -l'


# =======================================
# ---------- Directory Aliases ----------
# =======================================
alias cn='cd ${DATA_ROOT}/code-notes'
alias cs='cd ${DATA_ROOT}/code-snips'
alias data='cd ${DATA_ROOT}'
alias reference='cd ${DATA_ROOT}/reference'
alias scripts='cd ${DATA_ROOT}/scripts'
alias wks='cd ${WORKSPACE_ROOT}'

