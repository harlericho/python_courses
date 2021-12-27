from tkinter import *
import requests
# 0f29428662026b5e9bd47140e703469f
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Function weather
def weather(town):
    try:
        API_KEY = "0f29428662026b5e9bd47140e703469f"
        URL = "http://api.openweathermap.org/data/2.5/weather"
        parameters = {'q':town,'appid':API_KEY,'units':'metric','lang':'es'}
        response = requests.get(URL, params = parameters)
        print(response.json())
        valueWeather = response.json()
        show_request(valueWeather)
    except:
        print("Error")

# Function show request
def show_request(town):
    try:
        name_town = town['name']
        description_town = town['weather'][0]['description']
        temp_town = town['main']['temp']
        showTown['text'] = name_town
        showDescription['text'] = description_town
        showTemp['text'] = str(int(temp_town)) + "°C"
    except:
        showTown['text'] = "Loading..."
        showDescription['text'] = "Try again"
        showTemp['text'] = ""


    
# Configure the window
window = Tk()
window.title("Weather App")
window.geometry("300x300")
window.resizable(0, 0)
window.configure(background="white")

# Create the entry box
eTown = Entry(window, font=("Arial", 19), justify=CENTER)
eTown.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
eTown.focus()

# Buttons
buttonRequest = Button(window, text="Weather", width=33, height=2, bg="green", fg="white", justify=CENTER, command=lambda: weather(eTown.get()))
buttonRequest.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Label
showTown = Label(window, font=("Arial", 19))
showTown.grid(row=2, column=0, columnspan=4, padx=20, pady=20)

showTemp = Label(window, font=("Arial", 25), fg="blue" )
showTemp.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

showDescription = Label(window, font=("Arial", 12), fg="gray")
showDescription.grid(row=4, column=0, columnspan=4, padx=10, pady=10)



# Run the app
window.mainloop()