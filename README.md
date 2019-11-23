# Data-Engineering-Blossom
This repository contains all projects pertaining to the Data Engineering Fellowship program with Blossom Academy.

## Project 1: Downloading, Reading and Filtering Data
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
This project investigates top keywords companies within various cities in the USA require data science candidates to have in their resume.
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
 -Follow Project 2 instructions on [Project2Instructions](https://docs.google.com/document/d/1aUlsbUtUIbaZpLa_ZNVSWg49U7A7GhEPQTPoA7KzyqQ/edit)
 
 
 ## Project 3: Basic End-To-End Extract Transform Load (ETL) Pipeline
 This project seeks to implement a basic Extract Load Transform (ETL) pipeline using *Spark* and *PostgreSQL.*
 
 ### Congfiguration 
 - Install Postgres (either Mac or All other OS) [EnterpiseDB](https://postgresapp.com/)
 - Install Postgres Client [DBeaver](https://dbeaver.io/download/)
 - Conntect to Postgres using the CLI (```psql --host locahost --username postgres --password```)
 -Create a copy of the **Jars** folder on your computer.
 - Follow lab project instruction on [Project3Instructions](https://docs.google.com/document/d/1NwEB-1kaSUmJoL4U6B6qO4zddkciJYmP_DMqpN-HNak/edit)


## Project 4: Scraping Real Estates Listings From Meqasa
This project seeks to implement the concept of web scraping which is simply to automatically mine data or collect information from a specific source (website) using certain tools.

### Configuration 
- Install Requests (```pip install requests ``` )
- Install BeautifulSoup (``` pip install beautifulsoup4```)
- Install LXML (```pip install lxml```)
- Follow project instructions on [Project4Instructions](https://docs.google.com/document/d/1YKv4hwi1igESx0hmdd7gOLURngOQINNdFOMSIcZesDk/edit)
