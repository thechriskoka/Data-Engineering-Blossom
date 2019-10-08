import pandas as pd
import boto3

def main():
	#Loading our dataset into a dataframe
	#Loading first one million rows due the nature of the large filesize of the dataset.
	comp_data = pd.read_csv("companies_sorted.csv", nrows=1000000, index_col=0)
	
	#Checking th shape of our dataframe
	comp_data.shape
	
	#Checking out the number companies that do not have domain names.
	empty_comp = comp_data['domain'].isna().values.flattern.sum()
	
	#Print total number of companies that do not have domain names.
	print(empty_comp)
	
	#Time to drop all companies that do not have domain names from our dataset
	comp_data.dropna(subset = ['domain'], inplace = True)
	print(comp_data.shape)
	
	#After dropping irrelevant rows, we write output to a file in JSON format.
	comp_data.to_json('free-7-million-company-dataset-json.gzip', compression = 'gzip')
	
	#Now writing same file but this time in parquet format.
	comp_data.to_parquet('free-7-million-company_dataset.parquet')
	
	#Uploading files to bucket.
	s3 = boto3.client('s3')
	filename1 = 'free-7-million-company-dataset-json.gzip'
	filename2 = 'free-7million-company-dataset.parquet')
	bucket_name = 'blossom-data-eng-richmond'
	
	s3.upload_file(filename1, bucket_name, filename1) #Upload JSON file
	s3.upload_file(filename2, bucket_name, filename2) #Upload PARQUET file

	
if __name__ == "__main__":
	main()
