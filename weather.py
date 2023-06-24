import requests
import json
API_KEY = "b0695f743a9a0b2f34399f78fbf3ccd6"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()  
        return response

    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print("Connection timeout")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except KeyError:
        print("City not found")
    except json.decoder.JSONDecodeError as e:
        print("Error:", e)

    return None

if __name__ == "__main__":
    city = input("Enter city: ")
    weather = get_weather(city)
    if weather:
       weather_description = weather["weather"][0]["main"]
       weather_temp = weather["main"]["temp"]
       weather_temp_min = weather["main"]["temp_min"]
       weather_temp_max = weather["main"]["temp_max"]
       weather_humidity = weather["main"]["humidity"]

       print(f"Weather=: {weather_description}")
       print(f"Temperature: {weather_temp}°C")
       print(f"Min Temperature: {weather_temp_min}°C")
       print(f"Max Temperature: {weather_temp_max}°C")
       print(f"Humidity: {weather_humidity}%")
    
    else:
        print("No weather data")