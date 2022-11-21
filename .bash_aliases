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
