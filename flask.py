from flask import Flask, jsonify
import json
from urllib.request import urlopen
import mysql.connector

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    url = "http://api.weatherapi.com/v1/current.json?key=46789d6a59a24422956181619231506&q=london&aqi=no"
    api_page = urlopen(url)
    api = api_page.read()
    json_api = json.loads(api)

    city = json_api['location']['name']
    temperature = json_api['current']['temp_c']
    humidity = json_api['current']['humidity']
    description = json_api['current']['condition']['text']
    timestamp = json_api['current']['last_updated']

    weather_data = {
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'description': description,
        'timestamp': timestamp
    }

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
