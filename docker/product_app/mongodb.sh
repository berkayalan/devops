#!/bin/bash

start_mongo() {
    docker run --name mongodb \
            -e MONGO_INITDB_ROOT_USERNAME=mongodb \
            -e MONGO_INITDB_ROOT_PASSWORD=mongodb \
            -v "/Users/berkayalan/Desktop/Data Science/16 - Dev-MLOps/devops/docker/product_app/data:/data/db" \
            -p 27017:27017 \
            -d mongo:latest
    echo "MongoDB starting..."
    sleep 3 
}

stop_mongo() {
    echo "Stopping MongoDB container..."
    docker stop mongodb
    docker rm mongodb
    echo "MongoDB stopped and removed!"
}

create_table() {
    mongosh "mongodb://localhost:27017" \
        --username mongodb \
        --password mongodb \
        --authenticationDatabase admin <<EOF
show dbs
use clients
db.createCollection('test')   # Creating a collection in the 'clients' database
use products
db.createCollection('test')   # Creating a collection in the 'products' database
show dbs
exit
EOF
}


usage () {
  echo "Usage: $0  <action>"
  echo "    action = start|stop|create_table"
  exit 1
}

ACTION=$1

case $ACTION in 
  start) 
    start_mongo;;
  stop) 
    stop_mongo;;
  create_table)  
    create_table;;
  *) usage;;
esac
 