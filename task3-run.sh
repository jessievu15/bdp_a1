#!/bin/bash

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r /Input
hadoop fs -rm -r /Output/task3_job1
hadoop fs -rm -r /Output/task3_job2
hadoop fs -rm -r /Output/task3
hadoop fs -mkdir /Input
hadoop fs -put ./Taxis.txt /Input/Taxis.txt
hadoop fs -put ./Trips.txt /Input/Trips.txt

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options='-k1,1 -k2,2' \
-D mapreduce.job.reduces=3 \
-files ./task3_job1_mapper.py,./task3_job1_reducer.py \
-mapper ./task3_job1_mapper.py \
-reducer ./task3_job1_reducer.py \
-input /Input/Taxis.txt \
-input /Input/Trips.txt \
-output /Output/task3_job1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=3 \
-files ./task3_job2_mapper.py,./task3_job2_reducer.py \
-mapper ./task3_job2_mapper.py \
-reducer ./task3_job2_reducer.py \
-input /Output/task3_job1 \
-output /Output/task3_job2

hadoop fs -getmerge /Output/task3_job2 job2_output.txt

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=3 \
-D stream.num.map.output.key.fields=3 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options='-k3,3nr' \
-files ./task3_job3_mapper.py,./task3_job3_reducer.py,./job2_output.txt \
-mapper ./task3_job3_mapper.py \
-reducer ./task3_job3_reducer.py \
-input /Output/task3_job2 \
-output /Output/task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

# remove any intermediate output
hadoop fs -rm -r /Output/task3_job1
hadoop fs -rm -r /Output/task3_job2

hadoop fs -ls /Output/task3
hadoop fs -getmerge /Output/task3/part* task3_output.txt
cat task3_output.txt