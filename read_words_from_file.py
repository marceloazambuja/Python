#from aylienapiclient import textapi
import csv, io

## Initialize a new client of AYLIEN Text API
#client = textapi.Client("your_app_ID", "your_app_key")

with io.open('Text_sample.csv', 'w', encoding='utf8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Tweet", "Sentiment"])
	csv_writer.write("teste teste")
    with io.open("Text.txt", 'r', encoding='utf8') as f:
        for tweet in f.readlines():
        	## Remove extra spaces or newlines around the text
        	tweet = tweet.strip()

        	## Reject tweets which are empty so you don’t waste your API credits
        	if len(tweet) == 0:
        		print('skipped')
        		continue
        	
        	print(tweet)
			#csv_writer.writerow(["Tweet", "Sentiment"])



        	## Make call to AYLIEN Text API
        	#sentiment = client.Sentiment({'text': tweet})

        	## Write the sentiment result into csv file
        	#csv_writer.writerow([sentiment['text'], sentiment['polarity']])