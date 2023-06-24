# Weather_Api_Project

Overview:
------------
The Weather Forecasting Tool is a command line application that provides users with the current weather forecast for a given city. It leverages the OpenWeatherMap API to fetch weather data and parse it using Python. This tool demonstrates the usage of the OpenWeatherMap API, data parsing, and error handling.

https://github.com/Fastest-Coder-First/my_weather_app/assets/111697664/2b77a965-0d12-44a9-827a-e8c2f126c436



Web Application:
--------------------
The web application for the Weather Forecasting Tool can be accessed at http://rudra26.pythonanywhere.com/    .
It provides a user-friendly interface to enter the city name and fetch the weather forecast. The web page displays the weather information for the specified city, including weather description, temperature, minimum temperature, maximum temperature, and humidity.



Architectural Flow:
---------------------
The Weather Forecasting Tool follows a simple architectural flow to fetch and display weather data. The main components of the application are as follows:

1. User Input:
   - The user is prompted to enter the name of the city for which they want to fetch the weather forecast.

2. API Request:
   - The user's input is used to construct a URL with the OpenWeatherMap API endpoint and the API key.
   - A GET request is sent to the API endpoint using the constructed URL.
   - The API response is received and processed.

3. Response Handling:
   - The response is checked for errors and appropriate error handling is performed.
   - If the response is successful, the JSON data is extracted from the response.

4. Data Parsing:
   - The JSON data is parsed to extract the required weather information such as temperature, humidity, pressure, etc.

5. Display:
   - The extracted weather information is displayed to the user on the command line.

Error Handling:
----------------
The Weather Forecasting Tool incorporates error handling to handle potential issues during the API request, response handling, and data parsing stages. The following errors are specifically handled:
- Connection errors: Handles cases where there is no internet connection or connection timeouts.
- Invalid API key: Detects and informs the user if the API key used is invalid.
- City not found: Handles cases when the provided city name is not found in the API response.
- JSON decoding errors: Catches errors that may occur during JSON decoding of the API response.

Dependencies:
--------------
The Weather Forecasting Tool requires the following dependencies:
- Python 3.8
- requests library: Used for making HTTP requests to the OpenWeatherMap API.
- json library: Used for JSON parsing and decoding.

Usage:
--------
To use the Weather Forecasting Tool, follow these steps:
1. Install Python 3.x if not already installed.
2. Install the requests library by running the command: `pip install requests`.
3. Clone the repository and navigate to the project directory.
4. Run the `weather.py` file.
5. Enter the name of the city for which you want to fetch the weather forecast.
6. The tool will display the current weather information for the specified city.

Note: Ensure you have a valid API key from OpenWeatherMap and replace the placeholder API key in the code with your own key.

Contributing:
----------------
Contributions to the Weather Forecasting Tool are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the project repository.

License:
----------
The Weather Forecasting Tool is released under the MIT License. See the `LICENSE` file for more details.
