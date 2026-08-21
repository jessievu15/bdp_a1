#!/bin/bash

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -mkdir /Input
hadoop fs -rm -r /Input
hadoop fs -mkdir /Output/task3
hadoop fs -rm -r /Output/task3
hadoop fs -mkdir /Input
hadoop fs -put ./Trips.txt /Input/Taxis.txt
hadoop fs -put ./Trips.txt /Input/Trips.txt

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D stream.num.map.output.key.fields=1 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapreduce.job.reduces=3 \
-files ./task3-job1-mapper.py,./task3-job1-reducer.py \
-mapper ./task3-job1-mapper.py \
-reducer ./task3-job1-reducer.py \
-input /Input/Taxis.txt \
-input /Input/Trips.txt \
-output /Output/task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
