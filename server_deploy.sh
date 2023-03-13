echo "Deploying application ..."
    git stash save
    git pull origin try
    # pip install --upgrade pip
    # pip install -r requirements.txt
    # sudo systemctl restart nginx
    # sudo systemctl restart uwsgi
    # sudo supervisorctl stop all
    # sudo supervisorctl start all
    chmod +x entrypoint.sh
    docker restart $(docker ps -a -q)
    chmod +x server_deploy.sh
echo "Application deployed!"
