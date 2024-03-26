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
