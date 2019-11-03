# Who will eat Pizza In Do-Bong Gu ?

![Main UI](/captures/CommonUI/main_1.png)
### PROJECT DESCRIPTION
 - We're trying to find out how to attract customer for each (Chicken, Pizza, Chinese Food) Using [Data](https://github.com/philjjoon/2019-1-GROUP-2/tree/master/storage)(Order Information, Populations of each Location, Store population ) - see Also [Acquisition](https://github.com/philjjoon/2019-1-GROUP-2/tree/master/acquisition)  

 - this Project is implemented with Spark, Hadoop(HDFS), Zeppeline

### System :  
- Ubuntu16.04
- Hadoop-2.7.6
- spark-2.2.2
- zeppelin-0.8.0

### Installation
1. Get Spark 2.2.2
2. Get Hadoop 2.7.6
3. Get Zeppelin 0.8.0

After 1,2,3 Steps, set Configurations for each Application using [Configure](https://github.com/philjjoon/2019-1-GROUP-2/tree/master/configure) depends on your Local System


### Running
1. Start Hadoop File System 
```
In Master Position -> Running Hadoop File System Master, Slave1,2,3

$ cd $SPARK_HOME/sbin
$ ./start-all.sh

```
2. Start Spark System
```
In Master Position  -> Running NameNode.
$ cd $SPARK_HOME/sbin/
$ ./start-master.sh


In Slave Position  -> Running DataNode.
$ cd $SPARK_HOME/sbin/
$ ./start-slave.sh spark://master:7077

```
3. Run Zeppelin Server - [Details](https://github.com/philjjoon/2019-1-GROUP-2/issues/5)
>> default Port for Zeppelin is 8080

```
$ cd $ZEPPELIN_HOME/bin/
$ ./zeppelin-daemon.sh start
```
Please Let me know If you have Any Questions.
