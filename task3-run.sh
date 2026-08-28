#!/bin/bash

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r -f /Output/task3_job1
hadoop fs -rm -r -f /Output/task3_job2
hadoop fs -rm -r -f /Output/task3

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

hadoop fs -getmerge /Output/task3_job2/part* task3_job2_output.txt
python task3_job3_boundary.py < task3_job2_output.txt > boundary.txt

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=3 \
-D stream.num.map.output.key.fields=3 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options='-k1,1n -k3,3nr' \
-files ./task3_job3_mapper.py,./task3_job3_reducer.py,./boundary.txt \
-mapper ./task3_job3_mapper.py \
-reducer ./task3_job3_reducer.py \
-input /Output/task3_job2 \
-output /Output/task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner