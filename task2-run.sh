'''#!/bin/bash   

v=$(head -n 1 initialization.txt)
cp initialization.txt centroids.txt

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r /Input
hadoop fs -mkdir /Input
hadoop fs -put ./Trips.txt /Input/Trips.txt

i=1
while [ $i -le $v ]
do
    hadoop fs -rm -r -f /Output/task2

    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -D stream.num.map.output.key.fields=2 \
    -D mapred.text.key.partitioner.options=-k1,1 \
    -files ./centroids.txt,./task2-mapper.py,./task2-reducer.py \
    -mapper ./task2-mapper.py \
    -reducer ./task2-reducer.py \
    -input /Input/Trips.txt \
    -output /Output/task2 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

    rm -f task2_output.txt
    hadoop fs -ls /Output/task2
    hadoop fs -getmerge /Output/task2/part* task2_output.txt

    echo "Iterration $i"
    cat task2_output.txt
    cut -f1,2 task2_output.txt > centroids.txt

    i=$((i+1))
done'''

#!/bin/bash   

v=$(head -n 1 initialization.txt)
cp initialization.txt centroids.txt

# remove the input and output directories every time before running the job to avoid errors
hadoop fs -rm -r /Input
hadoop fs -mkdir /Input
hadoop fs -put ./Trips.txt /Input/Trips.txt

i=1
while [ $i -le $v ]
do
    hadoop fs -rm -r -f /Output/task2

    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -D mapreduce.job.reduces=3 \
    -files ./centroids.txt,./task2-mapper.py,./task2-reducer.py \
    -mapper ./task2-mapper.py \
    -reducer ./task2-reducer.py \
    -input /Input/Trips.txt \
    -output /Output/task2

    rm -f task2_output.txt
    hadoop fs -ls /Output/task2
    hadoop fs -getmerge /Output/task2/part* task2_output.txt

    echo "Iterration $i"
    cat task2_output.txt
    cut -f1,2 task2_output.txt > centroids.txt

    i=$((i+1))
done