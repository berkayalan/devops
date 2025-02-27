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

create_spesific_table() {
    local table_name="$1"
    mongosh "mongodb://localhost:27017" \
        --username mongodb \
        --password mongodb \
        --authenticationDatabase admin <<EOF
show dbs
use ${table_name}
db.${table_name}.insertOne(
  {
    title: "The Favourite",
    genres: [ "Drama", "History" ],
    runtime: 121,
    rated: "R"
  }
)
show dbs
exit
EOF
}

delete_spesific_table() {
    local table_name="$1"
    mongosh "mongodb://localhost:27017" \
        --username mongodb \
        --password mongodb \
        --authenticationDatabase admin <<EOF
show dbs
use ${table_name}
db.dropDatabase("${table_name}")
show dbs
exit
EOF
}


usage () {
  echo "Usage: $0  <action><table_name>"
  echo "    action = start|stop|create_table|create_spesific_table|delete_spesific_table"
  echo "    table_name (optional) = <table name you want to create or delete>"
  exit 1
}

ACTION=$1
TABLE_NAME=$2

case $ACTION in 
  start) 
    start_mongo;;
  stop) 
    stop_mongo;;
  create_table)  
    create_table;;
  create_spesific_table)
    if [ -z "$TABLE_NAME" ]; then
      echo "Error: You must provide a table name for create_spesific_table."
      usage
    else
      create_spesific_table "$TABLE_NAME"
    fi
    ;;
  delete_spesific_table)
    if [ -z "$TABLE_NAME" ]; then
      echo "Error: You must provide a table name for delete_spesific_table."
      usage
    else
      delete_spesific_table "$TABLE_NAME"
    fi
    ;;
  *) usage;;
esac