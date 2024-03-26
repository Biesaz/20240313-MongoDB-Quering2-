import random
from datetime import date, timedelta
import pymongo

def generate_random_person(min_age, max_age):
  """Generates a random person with name, surname, date of birth, and annual salary."""
  first_names = ["John", "Alice", "David", "Emily", "Michael", "Sarah", "Robert", "Jennifer", "William", "Margaret"]
  last_names = ["Smith", "Johnson", Williams, Brown, Jones, Miller, Davis, Garcia, Hernandez, Lopez"]
  birth_year = random.randint(date.today().year - max_age, date.today().year - min_age)
  birth_date = date(birth_year, random.randint(1, 12), random.randint(1, 28))
  age = date.today().year - birth_year
  salary = round(random.uniform(20000, 80000), 2)  # Annual salary in EUR
  return {"name": random.choice(first_names), "surname": random.choice(last_names), "date_of_birth": birth_date.isoformat(), "age": age, "annual_salary_before_tax": salary}

def connect_to_mongo(host="localhost", port=27017, database="tax_calculator"):
  """Connects to the MongoDB database."""
  client = pymongo.MongoClient(host, port)
  db = client[database]
  return db

def generate_and_insert_data(db, num_documents, min_age=25, max_age=65):
  """Generates and inserts random people data into the database."""
  collection = db["people"]
  for _ in range(num_documents):
    person = generate_random_person(min_age, max_age)
    collection.insert_one(person)

if __name__ == "__main__":
  # Replace with your MongoDB connection details if needed
  db = connect_to_mongo()
  generate_and_insert_data(db, 500)
  print(f"Generated and inserted {500} people data into the database.")
