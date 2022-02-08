from distutils import text_file
from tkinter import *
from turtle import color
import requests
from tkinter import messagebox

api_key = "b295acb4463364204f22469997e78aeb"
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        # we want the condition : (City, Country, icon, temperature, weather, humidity, wind)
        city = json['name']
        country = json['sys']['country']
        icon = json['weather'][0]['icon'] # it is a list
        temperature = round(json['main']['temp'])
        weather = json['weather'][0]['main'] # it is a list
        humidity = round(json['main']['humidity'])
        wind = json['wind']['speed']

        final = (city, country, icon, temperature, weather, humidity, wind)
        return final
    else:
        return None
    
def search():
    global read_image
    #city = city_text.get()
    city = textfield.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        icon = weather[2]
        read_image = PhotoImage(file=r"images/"+ icon +".png")
        image['image'] = read_image
        temp_lbl['text'] = '{temp}ºC'.format(temp=weather[3])
        weather_lbl['text'] = weather[4] #cloudy
        humidity_lbl['text'] = 'Humidity: {humidity}%'.format(humidity=weather[5])
        wind_lbl['text'] = 'Wind: {wind} meter/sec'.format(wind=weather[6])
        
    else:
        messagebox.showerror('Error', 'City {} Not Found'.format(city))
        

app = Tk()
app.title("Weather App")
app.geometry('500x430')
app.config(bg="#88c1ef")
h1 = ("Arial", 20, "bold")
h2 = ("Arial", 18, "bold")
h3 = ("Arial", 12)
textfield = Entry(app, font = h2)
textfield.pack(pady = 20)
textfield.focus()


read_image = PhotoImage(file=r"images/01d.png")



# search bar
search_btn = Button(app, text='Search', font = h3, width=12, command=search)
search_btn.pack()


# city name and city code 
location_lbl = Label(app, text='', font = h1, bg="#88c1ef")
location_lbl.pack()

image = Label(app, image='', bg="#88c1ef")
image.pack()


temp_lbl = Label(app, text='', font = h2, bg="#88c1ef")
temp_lbl.pack()


weather_lbl = Label(app, text='', font = h2, bg="#88c1ef")
weather_lbl.pack()

humidity_lbl = Label(app, text='', font = h2, bg="#88c1ef")
humidity_lbl.pack()

wind_lbl = Label(app, text='', font = h2, bg="#88c1ef")
wind_lbl.pack()

app.mainloop()
