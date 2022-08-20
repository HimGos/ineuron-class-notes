import mysql.connector as conn
import pandas as pd



mydb = conn.connect(host="localhost", user='root', passwd='*Himgos13', db='ineuron_25Jul_asgnmt')

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS ineuron_25Jul_asgnmt")

cursor.execute("CREATE TABLE IF NOT EXISTS Attribute_DataSet( "
               "Price varchar(20),"
               "Rating decimal(2,1),"
               "Size varchar(5),"
               "Season varchar(15),"
               "NeckLine varchar(25),"
               "SleeveLength varchar(25),"
               "WaiseLine varchar(25),"
               "Material varchar(25),"
               "FabricType varchar(25),"
               "Decoration varchar(25),"
               "PatternType varchar(25),"
               "Recommendation int"
               ")")


# cursor.execute("""
# LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Attribute DataSet.csv'
# INTO TABLE attribute_dataset
# FIELDS TERMINATED BY ','
# ENCLOSED BY '"'
# LINES TERMINATED BY '\r\n'
# IGNORE 1 LINES;
# """)

cursor.execute("CREATE TABLE IF NOT EXISTS dress_sales("
               "Dress_ID int,"
               "`29/8/2013` int,"
               "`31/8/2013` int,"
               "`09/02/2013` int,"
               "`09/04/2013` int,"
               "`09/06/2013` int,"
               "`09/08/2013` int,"
               "`09/10/2013` int,"
               "`09/12/2013` int,"
               "`14/09/2013` int,"
               "`16/09/2013` int,"
               "`18/09/2013` int,"
               "`20/09/2013` int,"
               "`22/09/2013` int,"
               "`24/09/2013` int,"
               "`26/09/2013` int,"
               "`28/09/2013` int,"
               "`30/09/2013` int,"
               "`10/02/2013` int,"
               "`10/04/2013` int,"
               "`10/06/2013` int,"
               "`10/08/2010` int,"
               "`10/10/2013` int,"
               "`10/12/2013` int"
               ")")


# cursor.execute("""
# LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Dress Sales.csv'
# INTO TABLE dress_sales
# FIELDS TERMINATED BY ','
# ENCLOSED BY '"'
# LINES TERMINATED BY '\r\n'
# IGNORE 1 LINES;
# """)

cursor.execute("SELECT *"
               "FROM attribute_dataset")

for i in cursor.fetchall():
    print(i)


