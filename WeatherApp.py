import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is entry: ", entry)

# 97cf16681ccd0e94343a08c14b2ab17d
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City:  %s \nConditions:  %s \nTemperature (°C):  %s' % (name, desc, temp)
    except:
        final_str = "There was a problem retrieving the information "

    return final_str

def get_weather(city):
    weather_key = '97cf16681ccd0e94343a08c14b2ab17d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = "#80c1ff", bd=5)
frame.place(relx = 0.5, rely =0.1, relheight = 0.1, relwidth = 0.75, anchor='n')

entry = tk.Entry(frame, font=('calibri', 18))
entry.place(relwidth=0.65, relheight=1)

button  = tk.Button(frame, text="Get Weather", font=('calibri', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1 , relwidth=0.3 )

lower_frame = tk.Frame(root, bg = "#80c1ff", bd=10)
lower_frame.place(relx = 0.5, rely =0.25, relheight = 0.6, relwidth = 0.75, anchor='n')

label = tk.Label(lower_frame, font=('calibri', 18), anchor = 'nw', justify='left')
label.place(relwidth=1, relheight=1)

root.mainloop()
