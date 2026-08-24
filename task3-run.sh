#!/bin/bash

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -mkdir /Input
hadoop fs -put ./Taxis.txt /Input/Taxis.txt
hadoop fs -put ./Trips.txt /Input/Trips.txt

hadoop fs -rm -r -f /Output/task3-job1
hadoop fs -rm -r -f /Output/task3-job2
hadoop fs -rm -r -f /Output/task3

# Job 1: Join
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -files ./task3-job1-mapper.py,./task3-job1-reducer.py \
    -mapper ./task3-job1-mapper.py \
    -reducer ./task3-job1-reducer.py \
    -input /Input/Taxis.txt,/Input/Trips.txt \
    -output /Output/task3-job1

echo "-- Job 1 Done --"
hadoop fs -ls /Output/task3-job1

# Job 2: Aggregation
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -files ./task3-job2-mapper.py,./task3-job2-reducer.py \
    -mapper ./task3-job2-mapper.py \
    -reducer ./task3-job2-reducer.py \
    -input /Output/task3-job1 \
    -output /Output/task3-job2

echo "-- Job 2 Done --"
hadoop fs -ls /Output/task3-job2
hadoop fs -getmerge /Output/task3-job2/part* job2_check.txt
cat job2_check.txt

# Job 3: Sorting
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options='-k1,1n -k2,2nr' \
    -D mapreduce.job.reduces=3 \
    -files ./task3-job3-mapper.py,./task3-job3-reducer.py \
    -mapper ./task3-job3-mapper.py \
    -reducer ./task3-job3-reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /Output/task3-job2 \
    -output /Output/task3

echo "-- Job 3 Done --"
hadoop fs -ls /Output/task3
hadoop fs -getmerge /Output/task3/part* task3_final_output.txt
cat task3_final_output.txt

hadoop fs -rm -r -f /Output/task3-job1

