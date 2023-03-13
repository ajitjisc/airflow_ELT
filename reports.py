import csv
import os

def generate_report1(file_path):
    # Define the field names for the TSV file
    fieldnames = ['title', 'year', 'book']

    # Generate some dummy data
    data = [
        {'title': 'xxxx', 'year': 2009, 'book': 'xxx'},
        {'title': 'xxxx', 'year': 2008, 'book': 'xxx'},
    ]


    # Write the data to the TSV file
    with open(file_path, 'w', newline='') as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return os.path.abspath(file_path)

def generate_report2(file_path):
    # Define the field names for the TSV file
    fieldnames = ['course', 'code', 'batch']

    # Generate some dummy data
    data = [
        {'course': 'xxxx', 'code': 352, 'batch': 'dgs'},
        {'course': 'xxxx', 'code': 282, 'batch': 'sbdsb'},
        {'course': 'xxxx', 'code': 4222, 'batch': 'sbfbs'},
        {'course': 'xxxx', 'code': 1922, 'batch': 'sbbs'},
        {'course': 'xxxx', 'code': 5566, 'batch': 'sdbb'}
    ]


    # Write the data to the TSV file
    with open(file_path, 'w', newline='') as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return os.path.abspath(file_path)

def generate_report3(file_path):
    # Define the field names for the TSV file
    fieldnames = ['Name', 'Age', 'category']

    # Generate some dummy data
    data = [
        {'Name': 'xxxx', 'Age': 35, 'category': '0'},
        {'Name': 'xxxx', 'Age': 28, 'category': '1'},
        {'Name': 'xxxx', 'Age': 42, 'category': '1'},
        {'Name': 'xxxx', 'Age': 19, 'category': '1'},
        {'Name': 'xxxx', 'Age': 55, 'category': '1'},
        {'Name': 'xxxx', 'Age': 35, 'category': '1'},
        {'Name': 'xxxx', 'Age': 28, 'category': '1'},
        {'Name': 'xxxx', 'Age': 42, 'category': '1'},
        {'Name': 'xxxx', 'Age': 19, 'category': '1'},
        {'Name': 'xxxx', 'Age': 55, 'category': '1'},
        {'Name': 'xxxx', 'Age': 35, 'category': '1'},
        {'Name': 'xxxx', 'Age': 28, 'category': '1'},
        {'Name': 'xxxx', 'Age': 42, 'category': '1'},
        {'Name': 'xxxx', 'Age': 19, 'category': '0'},
        {'Name': 'xxxx', 'Age': 55, 'category': '0'},
        {'Name': 'xxxx', 'Age': 35, 'category': '0'},
        {'Name': 'xxxx', 'Age': 28, 'category': '0'},
        {'Name': 'xxxx', 'Age': 42, 'category': '0'},
        {'Name': 'xxxx', 'Age': 19, 'category': '0'},
        {'Name': 'xxxx', 'Age': 55, 'category': '0'},
        
    ]


    # Write the data to the TSV file
    with open(file_path, 'w', newline='') as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return os.path.abspath(file_path)

