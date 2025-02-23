#!/bin/bash

docker run --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 6432:5432 -d postgres:latest
echo "Postgressql starting..."
sleep 3 

docker exec -it postgres psql -U postgres -d postgres -c "CREATE DATABASE productapp"
sleep 3
echo "productapp database created"

docker exec -it postgres psql -U postgres -d postgres -c "
create table if not exist products
(
    id bigserials not null primary key,
    name varchar(255) not null,
    price double precision not null,
    discount double precision,
    store varchar(255) not null,
    brand varchar(255) not null,
    category varchar(255) not null,
    subcategory varchar(255) not null,
    sku bigserials not null
);
"
sleep 3
echo "Table products created"
