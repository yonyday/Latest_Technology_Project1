## How to Import Json Code ?
#### 1. Run Zeppelin Server


#### 2. Browse localhost:8080 / Set your own port


#### 3. Click **Import Note**

![step1](/captures/importjson/1.png)


#### 4. Select .json Files included in this folder

![step1](/captures/importjson/2.png)

## Code 

### prepare
#### Import library
![step1](/captures/CodeCapture/1_importLib.JPG)


#### CSV to pyspark dataframe
![step1](/captures/CodeCapture/2_dataload.jpg)

### DashBoard 1 : Population Map
#### Select options (Gender, Ages)
![step1](/captures/CodeCapture/3_selectForm.JPG)

#### Spark processing
* Get User Selected Options ( Gender, Ages )
* Create Location information For Circls in the Map 
* Join Gender/Age - Population with LatLang Information
![step2](/captures/CodeCapture/jmCapture_angular.JPG)

#### Angular Visualization
* Get Joined Rows from Spark Coded above
* Drawing maps with Population Data On Maps
* Leaflet, D3 is Used to implement
![step3](/captures/CodeCapture/jmCapture_spark.png)



### DashBoard 2 : Orders Comparison to Other regions
#### Select options (region, store_type, age, gender)
![step1](/captures/CodeCapture/4_selectForm.JPG)


#### Spark processing 
* get five region list in which selected region is median value from df_people dataframe <br>
* compute average of Orders in five regions <br>
* make dataframe which has (Date, Average Order of other regions, Order of selected region) Column <br>
![step1](/captures/CodeCapture/8_daily_hydashboard.JPG)



#### Select Specific options (start date, end date, Daily/Monthly view)
![step1](/captures/CodeCapture/5_selectForm.JPG)

#### Show Chart by Zeppelin
![step1](/captures/CodeCapture/7_daily_hydashboard.JPG)


### DashBoard 3 : Orders by day_of_week, gender, age
#### Select options (region, store_type, start date, end date)
![step1](/captures/CodeCapture/10(1).JPG)

#### Spark Processing
* get dataframe and choose concatenation of data by selecting
* make day order by SMTWTFS for visualization of bar chart
* calculate the sum of the orders by day of the week, gender, age group during the period

* this is same code but with pyspark SQL 
![step1](/captures/CodeCapture/24.png)

#### draw bar chart - day of week / age group / gender
![step1](/captures/CodeCapture/11_dayOfWeek.JPG)
![step1](/captures/CodeCapture/12_age.JPG)
![step1](/captures/CodeCapture/12_gender.JPG)

#### make sentence by using key point
* sort result by sum of order
* extract keyword (the most sold day, the sex to buy more, and the age to purchase more)
![step1](/captures/CodeCapture/13_keypointSentence.JPG)

### DashBoard 4 : BlockMap showing how hot competition is
#### Select options (store_type)
![step1](/captures/CodeCapture/15_yy_selectForm.JPG)

#### Spark Processing
* get dataframe
* get total Orders and number of Store region by region
* compute total Orders divided by number of store 
* join with coordinate information data
![step1](/captures/CodeCapture/14_yy.JPG)
![step1](/captures/CodeCapture/16_yy.JPG)

* this is same code but with pyspark SQL 
![step1](/captures/CodeCapture/25.png)

#### draw blockmap 
![step1](/captures/CodeCapture/17_yy.JPG)
![step1](/captures/CodeCapture/19blockmap.PNG)


### DashBoard 5 : Orders of selected age and gender by day_of_week
#### Select options (region, store_type, age)
![step1](/captures/CodeCapture/20.PNG)

#### Spark Processing
* filter rows using selected options
* sort by day of week
![step1](/captures/CodeCapture/21.PNG)
![step1](/captures/CodeCapture/22.PNG)

#### Show Chart by Zeppelin
![step1](/captures/CodeCapture/23.PNG)
