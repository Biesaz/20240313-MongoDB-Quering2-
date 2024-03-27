# Create an income tax calculator: 

#  - Generate at least 500 documents , with fields: name, surname, date of birth , 
# age (determined from date of birth), anual salary before tax (EUR, round to 2 numbers after comma)
#  - Create a CLI application that would let us get first 10 people from database within the age bracket [min_age, max_age]
#  - Those people name surname and age should be shown as an option to choose.
#  - When one of ten options is chosen, there should be calculated tax return (it should be created a document as a tax card, 
# values taken from database). Lets say GPM tax is 20% and HealtTax is 15% from 90% of the income left after GPM deduction.
#  - The final values should be show and wrriten to database (like a generated data and taxes paid, take home pay etc.) 
# and portrayed in a web page (use flask and docker, show the url were to click )

# cli, mongoDB, flaskas

# 1. **Generate Data**:
#    - Generate at least 500 documents with fields: name, surname, date of birth, annual salary before tax 
# (rounded to 2 decimal places).
#    - Calculate age from the date of birth.

# 2. **CLI Application**:
#    - Develop a CLI application that retrieves the first 10 people from the database within a specified age bracket 
# [min_age, max_age].
#    - Display the names, surnames, and ages of these individuals as selectable options.

# 3. **Tax Calculation**:
#    - Calculate the tax return based on the provided tax rates.
#    - Assume GPM tax is 20% and Health Tax is 15% of 90% of the income left after GPM deduction.

# 4. **Database Handling**:
#    - Store the calculated tax details (e.g., tax paid, take-home pay) in a database for each individual.

# 5. **Web Interface**:
#    - Develop a web application using Flask.
#    - Display the URL where users can access the application.
#    - Show the tax details and income information for the selected individual.

# 6. **Database Choice**:
#    - Utilize MongoDB to store the generated data and tax-related information.

# To implement this project, you will need to work on data generation, CLI application development, 
# tax calculation logic, database integration, web development with Flask, and Docker setup for deployment.

import random
from pymongo import MongoClient
from faker import Faker
import datetime

####### 1 ##########
fake = Faker()

# Generate 500 individuals' data
data = []
for _ in range(500):
    name = fake.first_name()
    surname = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=65)
    annual_salary = round(random.uniform(20000, 100000), 2)
    data.append({
        'name': name,
        'surname': surname,
        'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
        'annual_salary': annual_salary
    })

# Print sample data
for person in data[:5]:  # Print first 5 individuals as a sample
    print(person)

######## 2 ############
    
import argparse
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["tax_calculator"]
collection = db["individuals"]

# Function to retrieve individuals within a specified age range
def get_individuals_in_age_range(min_age, max_age):
    individuals = collection.find({ "age": { "$gte": min_age, "$lte": max_age } }).limit(10)
    return list(individuals)

# CLI argument parsing
parser = argparse.ArgumentParser(description="Income Tax Calculator CLI Application")
parser.add_argument("--min_age", type=int, help="Minimum age for individuals")
parser.add_argument("--max_age", type=int, help="Maximum age for individuals")
args = parser.parse_args()

if args.min_age is not None and args.max_age is not None:
    individuals = get_individuals_in_age_range(args.min_age, args.max_age)
    for idx, person in enumerate(individuals, 1):
        print(f"{idx}. Name: {person['name']} {person['surname']}, Age: {person['age']}")

client.close()

####### 3 ###########

def calculate_tax_return(annual_salary):
    # Tax rates
    gpm_tax_rate = 0.20
    health_tax_rate = 0.15

    # Calculate GPM tax
    gpm_tax = annual_salary * gpm_tax_rate

    # Calculate remaining income after GPM deduction
    income_after_gpm = annual_salary - gpm_tax

    # Calculate health tax based on 90% of the income after GPM deduction
    health_tax = 0.90 * income_after_gpm * health_tax_rate

    # Calculate total tax paid
    total_tax_paid = gpm_tax + health_tax

    # Calculate take-home pay after tax deduction
    take_home_pay = annual_salary - total_tax_paid

    # Return the tax details
    return {
        'GPM Tax': gpm_tax,
        'Health Tax': health_tax,
        'Total Tax Paid': total_tax_paid,
        'Take-Home Pay': take_home_pay
    }

# Example usage:
annual_salary = 60000  # Replace with the individual's annual salary
tax_details = calculate_tax_return(annual_salary)
print(tax_details)

############# 4 ##########

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["tax_calculator"]
collection = db["individuals"]

# Sample data to insert
sample_data = {
    "name": "John",
    "surname": "Doe",
    "date_of_birth": "1990-01-01",
    "annual_salary": 50000
}

# Insert sample data into the MongoDB collection
insert_result = collection.insert_one(sample_data)
print(f"Data inserted with ID: {insert_result.inserted_id}")

client.close()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["tax_calculator"]
collection = db["individuals"]

# Retrieve all individuals from the collection
individuals = collection.find()

# Print retrieved data
for person in individuals:
    print(person)

client.close()


