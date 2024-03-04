#check anna server
file_path="$HOME/anna/pids"
if [ ! -e "$file_path" ]; then
    cd ~/anna
    ./scripts/start-anna-local.sh n n
fi

#check cloudburst server
file_path="$HOME/cloudburst/pids"
if [ ! -e "$file_path" ]; then
    cd ~/cloudburst
    ./scripts/start-cloudburst-local.sh n n
fi