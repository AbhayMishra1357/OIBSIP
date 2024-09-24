#Create a command-line weather app in Python that fetches and displays current weather data for a user-specified location (e.g., city or ZIP code) using a weather API.
#Show basic information such as temperature, humidity, and weather conditions.
import requests

def get_weather(api_key, location):
    # URL to fetch weather data from OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send a GET request to the API and store the response
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response to JSON format
        weather_data = response.json()

        # Extract basic information from the JSON data
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_condition = weather_data['weather'][0]['description']

        # Display the weather information
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_condition.capitalize()}")
    else:
        # If the request was not successful, display an error message
        print("Error: Unable to fetch weather data. Please check the location or API key.")

def main():
    # Your OpenWeatherMap API key
    api_key = "7e44fcb68b13c314dfd86152a51d1b3b"

    # Ask the user for the location (city name or ZIP code)
    location = input("Enter the city name or ZIP code: ")

    # Call the function to get and display the weather data
    get_weather(api_key, location)

# Call the main function to run the program
if __name__ == "__main__":
    main()