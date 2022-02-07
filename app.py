import tkinter as tk
import requests
import time



def getWeather(canvas):
    city = textField.get()
    #api_key = "b295acb4463364204f22469997e78aeb"
    #api = requests.get(
        #f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&APPID=b295acb4463364204f22469997e78aeb"
        #print("***********************")
        #print("Welcome to Weather App")
        #print("***********************")
    #user_input = input("Enter city: ")

        

        #if weather_data.json()['cod'] == '404':
            #print("No City Found")
        #else:
    weather_data = requests.get(api).json()       
    weather = weather_data.json()['weather'][0]['main']
    weather_des = weather_data.json()['weather'][0]['description']
            
    temp = round(weather_data.json()['main']['temp'])
    temp_mi = round(weather_data.json()['main']['temp_min'])
    feels_like = round(weather_data.json()['main']['feels_like'])
    temp_ma = round(weather_data.json()['main']['temp_max'])
    humidity = round(weather_data.json()['main']['humidity'])
    sunrise = time.strftime('%I:%M:%S', time.gmtime(weather_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(weather_data['sys']['sunset'] - 21600))
            
            
    final_info = "Weather:" + weather + "with" + weather_des
    final_data = "Temperature:" + temp + "ºC" + "\n" + "feels like:" + feels_like + "ºC" + "\n" + "Min Temp: " + temp_mi + "ºC" + "\n" + "Max Temp:" + temp_ma + "ºC" + "\n" + "Humidity: " + humidity + "%"
             
        
            
            

    label1.config(text = final_info)
    label2.config(text = final_data)
            
            
           
            
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop() 