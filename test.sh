#! /bin/bash
PYRO_SERIALIZERS_ACCEPTED=serpent,json,marshal,pickle
for i in {1..8}
do
  echo "Testing $i servers"
  for j in {1..10}
  do
    ./client.py $i 1000000 >> out/test$i
  done
done