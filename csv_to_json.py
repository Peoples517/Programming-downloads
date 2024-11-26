import csv
import json
import os

if not os.path.exists('student_data.csv'):
    print("Error: student_data.csv file does not exist")
else:
    with open('student_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = []

        for row in csv_reader:
            data.append(row)

    with open('student_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)