import csv
import faker
import random
import sys
import os

# Function to generate random email addresses
def generate_email(name):
    return name.lower().replace(" ", "") + "@test.com"

# Function to generate random names
def generate_name():
    return fake.name()

# Check if command-line argument is provided for number of rows
if len(sys.argv) < 2:
    print("Usage: python script_name.py <number_of_rows>")
    sys.exit(1)

try:
    num_rows = int(sys.argv[1])
except ValueError:
    print("Please provide a valid number for the number of rows.")
    sys.exit(1)

# Initialize faker library
fake = faker.Faker()

# Generate data
data = [("Name", "Email")]
for _ in range(num_rows):
    name = generate_name()
    email = generate_email(name)
    data.append((name, email))

# Save data to CSV file
filename = "random_data.csv"
with open(filename, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

print(f"{num_rows} random rows generated and saved to {os.path.abspath(filename)}")
