#!/bin/bash

v=$(head -n 1 initialization.txt)
cp initialization.txt current_medoids.txt

hadoop fs -rm -r /Input
hadoop fs -mkdir -p /Input
hadoop fs -put -f ./Trips.txt /Input/Trips.txt

i=1
while [ $i -le $v ]
do
    hadoop fs -rm -r -f /Output/task2

    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -files ./current_medoids.txt,./task2-mapper.py,./task2-reducer.py,./pam.py \
    -mapper ./task2-mapper.py \
    -reducer ./task2-reducer.py \
    -input /Input/Trips.txt \
    -output /Output/task2

    rm -f task2_output.txt
    hadoop fs -ls /Output/task2
    hadoop fs -getmerge /Output/task2/part* task2_output.txt

    echo "Iteration $i"
    cat task2_output.txt
    cut -f1,2 task2_output.txt > current_medoids.txt

    i=$((i+1))
done