#!/bin/bash   

v=$(head -n 1 initialization.txt)
cp initialization.txt centroids.txt

i=1
while [ $i -le $v ]
do
    hadoop fs -rm -r -f /Output/task2

    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -D mapred.text.key.partitioner.options=-k1,1 \
    -files ./centroids.txt,./task2_mapper.py,./task2_reducer.py \
    -mapper ./task2_mapper.py \
    -reducer ./task2_reducer.py \
    -input /Input/Trips.txt \
    -output /Output/task2 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

    rm -f task2_output.txt
    hadoop fs -getmerge /Output/task2/part* task2_output.txt

    echo "Iteration $i"
    cat task2_output.txt

    # save new centroids separately
    cut -f1,2 task2_output.txt > centroids1.txt

    seeiftrue=$(python task2_reader.py)
	
	if [ $seeiftrue = 1 ]
	then
		rm -f centroids.txt
		cp centroids1.txt centroids.txt
		break
	else
		rm -f centroids.txt
		cp centroids1.txt centroids.txt
	fi

    i=$((i+1))
done