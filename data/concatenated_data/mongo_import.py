import csv
import pymongo
import sys

csv.field_size_limit(2147483647)  # Set a large value as the field size limit

# Connect to the local MongoDB instance
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Create or select the database
db = client['Job-Recomendation']

# Create or select the collection
collection = db['Resume_Data']

# Open the CSV file
with open('C:\\Users\\Dell\\Desktop\\Final Year\\Job-Recomendation\\data\\concatenated_data\\updated_cv.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.DictReader(csvfile)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Create a document from the row data
        document = {
            'Unnamed: 0':int(row['Unnamed: 0']),
            'name': row['name'],
            'email': row['email'],
            'degree': row['degree'],
            'mobile_number': row['mobile_number'],
            'no_of_pages': int(float(row['no_of_pages'])),
            'skills': row['skills'],
            'All':row['All'],
            'pdf_to_base64': row['pdf_to_base64'],
            # Add any other relevant fields
        }

        # Insert the document into the collection
        collection.insert_one(document)

print("Data uploaded successfully to MongoDB")