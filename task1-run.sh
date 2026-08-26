#!/bin/bash

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r -f /Output/task1

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=3 \
-files ./task1_mapper.py,./task1_reducer.py \
-mapper ./task1_mapper.py \
-reducer ./task1_reducer.py \
-input /Input/Trips.txt \
-output /Output/task1