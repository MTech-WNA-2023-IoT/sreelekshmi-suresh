import json
from urllib.request import urlopen
import pymysql

# Create a connection to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='user',
    password='Pass',
    database='Weatherdata'
)

# Obtain API key from https://www.weatherapi.com
url = "http://api.weatherapi.com/v1/current.json?key=46789d6a59a24422956181619231506&q=London&aqi=no"

api_page = urlopen(url)
api = api_page.read()
json_api = json.loads(api)

print("Raw Data:")
print(json_api)

# Extract the desired data from the API response
city = json_api['location']['name']
temperature = json_api['current']['temp_c']
humidity = json_api['current']['humidity']
description = json_api['current']['condition']['text']
timestamp = json_api['current']['last_updated']

# Create the SQL INSERT statement
sql = "INSERT INTO data (city, temperature, humidity, description, timestamp) VALUES (%s, %s, %s, %s, %s)"
values = (city, temperature, humidity, description, timestamp)

# Execute the SQL statement and commit the changes
try:
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    print("Data inserted successfully.")
except Exception as e:
    print(f"Error inserting data: {str(e)}")

# Close the database connection
connection.close()
