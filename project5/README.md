# Project 5: Stream Processing. 
This project seeks to implement the concept of web scraping which is simply to automatically mine data or collect information from a specific source (website) using certain tools.
The project implements the following:
- Creating a shard kinesis stream
- Creating a producer that generates data from a given website into the created kinesis every 30 seconds
- Creating a consumer to collect data from the producer.
- Enriching the data.
- Finally, appending the results to a CSV file.

### Configuration
- Connect to boto3 client
- Import pandas, requests and beautifulsoup packages.
