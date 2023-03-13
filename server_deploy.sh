echo "Deploying application ..."
    git stash save
    git pull origin master
    # pip install --upgrade pip
    # pip install -r requirements.txt
    # sudo systemctl restart nginx
    # sudo systemctl restart uwsgi
    # sudo supervisorctl stop all
    # sudo supervisorctl start all
    cp .env.dev .env
    chmod +x entrypoint.sh
    docker restart $(docker ps -a -q)
    docker stop frontend
    chmod +x backup_database.sh
    chmod +x server_deploy.sh
echo "Application deployed!"
