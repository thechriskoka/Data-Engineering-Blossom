#This script implements a consumer for streamed data scraped from LoopGhana
import pandas as pd
import datetime as dt

#Intitiate the kinesis 
kinesis = boto3.client('kinesis', region_name = 'us-east-2')

#Utility function to get the shard ids
def get_shard_iterator(stream_name, shard_id, iterator_type, date):
    shard_response = kinesis.get_shard_iterator(
        StreamName = stream_name,
        ShardId = shard_id,
        ShardIteratorType = iterator_type,
        Timestamp = date
    )
    
    return shard_response['ShardIterator']
    
    
#Connecting our listings to consumer to connect to kinesis and then periodically check for new data
def listings_consumer(next_shard_iterator):
    start = dt.datetime.now()
    finish = start + dt.timedelta(seconds=60)
    
    #We will only consume for 60 seconds.
    while start < finish:
        response = kinesis.get_records(
            ShardIterator = next_shard_iterator,
            Limit = 20
        )
        
        try:
            data = response['Records'][0]['Data']
            data = csv.loads(data)
            
            df = pd.DataFrame(data)
        
        except IndexError:
            #This error only occurs when all records have been consumed.
            print("No new records have arrived")
            
        next_shard_iterator = response['NextShardIterator']
        
        #pause checking for data every 10 seconds...
        time.sleep(10)
        
        
if __name__ == '__main__':
    stream_name = 'blossom-data-eng-richmond'
    shard_id = 'shardId-000000000001'
    iterator_type = 'AT_TIMESTAMP'
    date = dt.datetime.today().date().__str__()
    
    next_shard_iterator = get_shard_iterator(stream_name, shard_id, iterator_type, date)
    listings_consumer(next_shard_iterator)
    
