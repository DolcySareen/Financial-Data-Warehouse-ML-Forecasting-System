# Define variables
KEY="cosc471vm_key.pem"
USER="azureuser"
HOST="20.121.50.159"
REMOTE_DIR="/data"
LOCAL_TAR="file.lst"

# Change private key permissions
chmod 600 $KEY

# SSH into the remote server and execute commands
ssh -o StrictHostKeyChecking=no -i $KEY $USER@$HOST << EOF
echo 'Stopping containers'
if docker-compose ps -q | grep -q .; then
    docker-compose down
    echo 'Docker Compose application stopped and removed.'
else
    echo 'No Docker Compose application is running.'
fi

echo 'Purging current deployment'
sudo rm -rvf $REMOTE_DIR
echo 'Creating new app root'
sudo mkdir -vp $REMOTE_DIR
sudo chown -Rfv $USER:$USER $REMOTE_DIR
EOF

# Create a tarball and transfer it to the remote server
tar -cvzf - -T $LOCAL_TAR | ssh -i $KEY $USER@$HOST "cd $REMOTE_DIR && tar -xvzf -"

# SSH into the remote server to start the Docker containers
ssh -o StrictHostKeyChecking=no -i $KEY $USER@$HOST << EOF
cd $REMOTE_DIR
sudo docker-compose build
sudo docker-compose up -d --wait
EOF

echo "Deployment completed successfully."
