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
We will be using PySpark as our data processing frame work in this priject.

### Configuration
