#check anna server
file_path="$HOME/anna/pids"
if [ -e "$file_path" ]; then
    cd ~/anna
    ./scripts/stop-anna-local.sh n n
fi

#check cloudburst server
file_path="$HOME/cloudburst/pids"
if [ -e "$file_path" ]; then
    cd ~/cloudburst
    ./scripts/stop-cloudburst-local.sh n n
fi