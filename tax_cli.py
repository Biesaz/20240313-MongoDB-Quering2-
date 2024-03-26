from datetime import date
import pymongo
from flask import Flask, render_template, request

def connect_to_mongo(host="localhost", port=27017, database="tax_calculator"):
  """Connects to the MongoDB database."""
  client = pymongo.MongoClient(host, port)
  db = client[database]
  return db

def get_people_by_age_range(db, min_age, max_age):
  """Retrieves people within the specified age range from the database."""
  collection = db["people"]
  query = {"age": {"$gte": min_age, "$lte": max_age}}
  return list(collection.find(query))[:10]  # Limit to top 10

def calculate_tax(person, gpm_rate=0.2, health_tax_rate=0.15):
  """Calculates the tax for a person."""
  gross_income = person["annual_salary_before_tax"]
  taxable_income = gross_income * (1 - gpm_rate)
  health_tax = taxable_income * health_tax_rate * 0.9  # 15% of 90% of taxable income
  total_tax = gpm_rate * gross_income + health_tax
  take_home_pay = gross_income - total_tax
  return {
      "name": f"{person['name']} {person['surname']}",
      "gross_income": gross_income,
      "gpm_tax": gpm_rate * gross_income,
      "health_tax": health_tax,
      "total_tax": total_tax,
      "take_home_pay": take_home_pay,
  }

app = Flask(__name__)

@app.route("/")
def list_people():
  db = connect_to_mongo()
  min_age = int(request.args.get("min_age", 25))
  max_age = int(request.args.get("max_age", 65))
