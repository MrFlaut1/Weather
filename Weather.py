import requests

# Define the coordinates (latitude and longitude)
latitude = 45.0376  # Example: Stavropol
longitude = 41.9810  # Example: Stavropol

# Open-Meteo API URL for current weather
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    
    # Extract current weather information
    if "current_weather" in data:
        current_temperature = data["current_weather"]["temperature"]  # Temperature in °C
        print(f"Current temperature: {current_temperature}°C")
    else:
        print("No current weather data available.")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
