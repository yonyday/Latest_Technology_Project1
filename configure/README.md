### Configurations 
  - [Spark](#Spark)
  - [Zeppelin](#Zeppelin)
  - [Hadoop](#Hadoop)
  
#### Spark
  1. Move File into $SPARK_HOME/conf/
  2. if you need SPARK_MASTER_WEBUI
  
  uncomment 
  ```
  SPARK_MASTER_WEBUI_PORT=50099
  ```
#### Zeppelin
  1. Move File into $ZEPPELIN_HOME/conf/
  2. Change Valuse depens of your local Settings.
  in [ zeppelin-env.sh ]
  ```
  export SPARK_HOME=/home/hadoop/spark
  export HADOOP_CONF_DIR=/home/hadoop/hadoop/etc/hadoop
  export JAVA_HOME=/usr/lib/jvm/java-8-oracle
  ```
  
#### Hadoop
  1. Move Files into $Hadoop_HOME/etc/hadoop
  2. Should Set Hadoop Paths depends on you Local Settings.
  >> those settings are for 1 Master - 3 Slaves.
