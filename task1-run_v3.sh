#!/bin/bash   

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r /Input
hadoop fs -rm -r /Output/task1
hadoop fs -mkdir /Input
hadoop fs -put ./Trips.txt /Input/Trips.txt

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,2 \
-D mapreduce.job.reduces=3 \
-files ./mapper_v2.py,./reducer_v2.py \
-mapper ./mapper_v2.py \
-reducer ./reducer_v2.py \
-input /Input/Trips.txt \
-output /Output/task1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner








