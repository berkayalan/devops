#!/bin/bash

file_number=$1
folder=$2
asset_name=$3

for (( i=0; i<=$1; i++ ))
 do
   if [ "$2" = file ];then
     touch ${3}-$i
   else
     mkdir ${3}-$i
  fi
 done

