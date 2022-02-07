import requests
#import time
#from datetime import datetime

api_key = "b295acb4463364204f22469997e78aeb"

while True:
    
    print("***********************")
    print("Welcome to Weather App")
    print("***********************")
    user_input = input("Enter city: ").upper()

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found! Try again.")
    else:
        weather = weather_data.json()['weather'][0]['main']
        weather_des = weather_data.json()['weather'][0]['description']
        
        temp = round(weather_data.json()['main']['temp'])
        temp_mi = round(weather_data.json()['main']['temp_min'])
        feels_like = round(weather_data.json()['main']['feels_like'])
        temp_ma = round(weather_data.json()['main']['temp_max'])
        humidity = round(weather_data.json()['main']['humidity'])
        wind = weather_data.json()['wind']['speed']
        #sunrise = time.strftime('%I:%M:%S', time.gmtime(weather_data.json()['sys']['sunrise'] + 39600))
        #sunset = time.strftime('%I:%M:%S', time.gmtime(weather_data.json()['sys']['sunset'] + 39600))
        #date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S")
        
        print("")
        print(f"========= Weather in {user_input} ==========")
        print(f"Satus: {weather} with {weather_des}")
        print(f"Temperature: {temp}ºC , feels like: {feels_like}ºC")
        print(f"Min Temp : {temp_mi}ºC")
        print(f"Max Temp: {temp_ma}ºC")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} meter/sec")
        #print(f"Sunrise: {sunrise}")
        #print(f"Sunset: {sunset}")
        print("====================== END ====================")
    
        again = input("Do you want to check another city? Type y/n : ")
        if again == "n":
            print("Good bye!")
            break