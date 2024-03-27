################### 5 ##################

from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["tax_calculator"]
collection = db["individuals"]

# Route to display individuals within a specified age range
@app.route('/')
def index():
    return "Welcome to the Income Tax Calculator!"

# Route to show individual details and tax information
@app.route('/individual/<id>')
def show_individual(id):
    individual = collection.find_one({"_id": id})
    # Perform tax calculation here if needed
    return render_template('individual.html', individual=individual)

if __name__ == '__main__':
    app.run(debug=True)