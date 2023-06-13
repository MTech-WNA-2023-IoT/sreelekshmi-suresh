import requests
import mysql.connector

# Weather API endpoint and API key
api_url = "http://api.weatherapi.com/v1/current.json?key=809f318cf0b74cb5a6860658231306&q=London&aqi=no"
api_key = "809f318cf0b74cb5a6860658231306"

# MySQL database connection
connection = mysql.connector.connect(
    host="localhost",
    user="user",
    password="Pass",
    database="weatherdata"
)

# Extract weather data from the API response
def extract_weather_data(response):
    data = response["current"]
    city = response["location"]["name"]
    temperature = data["temp_c"]
    humidity = data["humidity"]
    description = data["condition"]["text"]
    timestamp = data["last_updated"]

    return city, temperature, humidity, description, timestamp

# Make a request to the weather API
params = {
    "key": api_key,
    "q": "London"  # Replace with the desired location or city
}
response = requests.get(api_url, params=params).json()

# Extract weather data from the API response
city, temperature, humidity, description, timestamp = extract_weather_data(response)

# Create the SQL INSERT statement
sql = "INSERT INTO weather_data (city, temperature, humidity, description, timestamp) VALUES (%s, %s, %s, %s, %s)"

# Execute the INSERT statement with the data
cursor = connection.cursor()
cursor.execute(sql, (city, temperature, humidity, description, timestamp))
connection.commit()
cursor.close()
connection.close()
