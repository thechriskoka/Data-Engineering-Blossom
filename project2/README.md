# Project 2 : Batch Processing For Data Mining.
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
