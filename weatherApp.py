import requests


api_key = "b295acb4463364204f22469997e78aeb"

while True:
    
    print("***********************")
    print("Welcome to Weather App")
    print("***********************")
    user_input = input("Enter city: ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        weather_des = weather_data.json()['weather'][0]['description']
        
        temp = round(weather_data.json()['main']['temp'])
        temp_mi = round(weather_data.json()['main']['temp_min'])
        feels_like = round(weather_data.json()['main']['feels_like'])
        temp_ma = round(weather_data.json()['main']['temp_max'])
        humidity = round(weather_data.json()['main']['humidity'])
        
        print("-----------------------------------------------")
        print(f"Weather: {weather} with {weather_des}")
        print(f"Temperature: {temp}ºC , feels like: {feels_like}ºC")
        print(f"Min Temp : {temp_mi}ºC")
        print(f"Max Temp: {temp_ma}ºC")
        print(f"Humidity: {humidity}%")
        print("-----------------------------------------------")
    
        again = input("Do you want to check another city? Type y/n : ")
        if again == "n":
            print("Good bye!")
            break