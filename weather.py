import requests, json
from degrees_to_direction import degrees_to_direction

api_key = open('api_key.txt').read().splitlines()

while True:
    city = input("City: ")

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key[0]}')

    if result.json()['cod'] != 200:
        print('Inputted invalid location, or api key is broken.')
        continue
    else:
        break

description = result.json()['weather'][0]['description']
temp = round(result.json()['main']['temp'])
temp_feels = round(result.json()['main']['feels_like'])
temp_min = round(result.json()['main']['temp_min'])
temp_max = round(result.json()['main']['temp_max'])
cloudiness = result.json()['clouds']['all']
wind_speed = result.json()['wind']['speed']
wind_degrees = result.json()['wind']['deg']

wind_direction = degrees_to_direction(wind_degrees)

print(f'{city.title()} is currently {temp}°C with {description}. It feels like it is {temp_feels}°C.')
print(f'The temperature will range from {temp_min}°C to {temp_max}°C throughout the day.')
print(f'It is currently {cloudiness}% cloudy. Winds are blowing {wind_direction} at {wind_speed}km/h.')
