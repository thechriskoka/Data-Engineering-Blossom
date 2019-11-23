#Importing Modules.
import boto3
import csv
import json
import time

#Creating One(1) Shard Kinesis Stream with AWS Bucket

#Preparing stream source.
region = 'us-east-2'
streamName = 'blossom-data-eng-richmond'

#Initialize kinesis client
kinesis = boto3.client('kinesis', region_name = region)

#Creating a new stream and confirming that the stream is active.
response = kinesis.create_stream(StreamName = streamName, ShardCount = 1)

kinesis.list_streams()
stream_description = kinesis.describe_stream(StreamName = streamName)
stream_description.keys()

stream_description['StreamDescription']['Shards']
stream_description['StreamDescription']['Shards'][0]


#A Producer to scrape the first page of loopghana real estates' listings into the initialized kinesis every 30 seconds.
def get_data(criteria):
    data = scrape_looper(1, add_gps=True) #Indicating we need only the first page.
    data = data.head(2) #Our assumption; first 2 listigns are new.
    
    #We may have some criteria to filter our data. eg 'address = Tema'
    if criteria:
        data = data.query(criteria)
        
    #For this project we would use the following columns
    data = data[['description', 'category', 'beds','baths', 'price','url', 'area(mxm)', 'broker', 'listing_time','amenities', 'latitude', 'longitude', 'point_of_interest', 'point_of_interestcategory', 'distance_to_point_of_interest']]
    
    return data


def listings_producer(stream_name, data):
    response = kinesis.put_record(
        StreamName = streamName,
        Data = data,
        PartitionKey = 'blossom'
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("fRecords pushed to {streamName} within kinesis")
    else:
        print("Records failed to be pushed to kinesis")


#Time to run the scraping and pushing every 30 seconds
if __name__ == '__main__':
    try:
        while True:
            data = get_data(None)
            data = data.to_csv()
            listings_producer('blossom-data-eng-richmond', data)
            time.sleep(10)
    
    except Exception as e:
        print(f"Writing Failed! Exiting Fantastically due to {e}")
