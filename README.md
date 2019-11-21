# Data-Engineering-Blossom
This repository contains all projects pertaining to the Data Engineering Fellowship program with Blossom Academy.

## Project 1: This projects main aim is to implement the following
- Downloading data from s3 bucket. 
- Reading CSV file into a pandas dataframe
- Filtering certain columns 
- Converting after filtering to JSON and Parquet file formats.
- Uploading the files to s3 bucket on AWS.

### Configuration
This project used the following packages.
- boto3 ( ```pip install boto3```)
- fastparquet (```pip install fastparquet```)
- pyarrow (```pip install pyarrow```)
- pandas (```pip install pandas```)

### Results
The results were files converted into JSON and PARQUET formats and then loaded directly into the specified s3 bucket.


## Project 2 : Batch Processing For Data Mining.
This projects investigates top keywords companies within various cities in the USA require data science candidates to have in their resume.
We will be using PySpark as our data processing frame work in this project. 
The project demonstrates the following. 
- Loading data from s3 bucket.
- Reading and joining datasets with pyspark.
- Writing a function to generate ```n-grams``` (unigram and bigram) from a given text description 
- Writing a function to check frequency count of a given ngram in a column.

### Configuration
This project used PySpark packages which is found in ```requirements2.txt```
 - Install packages in requirements2.txt file ( ```pip install -r requirements2.txt```)
 - Load the ```data scientist job market dataset``` and ```us stocks``` datasets from s3 bucket onto your computer.
 -Follow Project 2 instructions on [Project-2-Instructions](https://docs.google.com/document/d/1aUlsbUtUIbaZpLa_ZNVSWg49U7A7GhEPQTPoA7KzyqQ/edit)
 
 
 ## Project 3: Basic End-To-End EXTRACT TRANSFORM LOAD (ETL) Pipeline
 This projects seeks to implement a basic Extract Load Transform (ETL) pipeline using *Spark* and *PostgreSQL.*
 
 ### Congfiguration 
 - Install Postgres (either Mac or All other OS) [EnterpiseDB](https://postgresapp.com/)
 - Install Postgres Client [DBeaver](https://dbeaver.io/download/)
 - Conntect to Postgres using the CLI (```psql --host locahost --username postgres --password```)
 -Create a copy of the **Jars** folder on your computer.
 - Follow lab project instruction on [Project3 Instructions](https://docs.google.com/document/d/1NwEB-1kaSUmJoL4U6B6qO4zddkciJYmP_DMqpN-HNak/edit)
