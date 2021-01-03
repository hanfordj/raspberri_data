import json 
import csv

# Opening JSON file and loading the data 
# into the variable data 
with open('pd-axpert_2020-08-06_small.json', mode='r', encoding='utf-8-sig') as f: 
	data = json.loads(f.read())

# now we will open a file for writing 
with open('data_file.csv', mode='w') as data_file:
	# create the csv writer object 
	csv_writer = csv.writer(data_file) 

	# Counter variable used for writing  
	# headers to the CSV file 
	count = 0

	for row in data: 
		if count == 0: 
			# Writing headers of CSV file 
			header = row.keys() 
			csv_writer.writerow(header) 
			count += 1

		# Writing data of CSV file 
		csv_writer.writerow(row.values()) 
