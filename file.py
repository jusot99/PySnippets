# This program demonstrates different file I/O operations in Python.

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("File I/O operations are important in Python.\n")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# Reading file line by line
with open('example.txt', 'r') as file:
    print("\nReading file line by line:")
    for line in file:
        print(line.strip())  # strip() removes leading and trailing whitespaces

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("This line is appended to the file.\n")

# Reading updated content
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)

# Using the 'with' statement for file I/O (automatically closes the file)
# Writing to a CSV file
import csv

data = [['Name', 'Age', 'City'],
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'San Francisco'],
        ['Charlie', 22, 'Los Angeles']]

csv_file_path = 'data.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in data:
        csv_writer.writerow(row)

# Reading from a CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print("\nReading from CSV file:")
    for row in csv_reader:
        print(row)

# Pickling and Unpickling (serialization)
import pickle

# Writing to a pickle file
data_to_pickle = {'name': 'John', 'age': 28, 'city': 'Chicago'}

pickle_file_path = 'data.pkl'

with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(data_to_pickle, pickle_file)

# Reading from a pickle file
with open(pickle_file_path, 'rb') as pickle_file:
    loaded_data = pickle.load(pickle_file)
    print("\nLoaded data from pickle file:")
    print(loaded_data)
