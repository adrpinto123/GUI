from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")

    #weather
    

    

    
    
    
#Creating Display Window
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

#create and place search box frame
Search_image=PhotoImage(file="C:\\Users\\adria\\OneDrive\\Desktop\\Weather App\\search (1).png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

#create and place search box + user input
textfield=tk.Entry(root,justify="center",width=19,font=("Helvetica",25,"bold"), bg="#404040",border=1,fg="yellow")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="C:\\Users\\adria\\OneDrive\\Desktop\\Weather App\\search_icon.png")
myimage_icon=Button(image=search_icon, borderwidth=0,cursor="hand1",bg="#404040", command=getWeather)
myimage_icon.place(x=400,y=34)

#time
name=Label(root,font=("Helvetica",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#Create and place logo
logo_image=PhotoImage(file="C:\\Users\\adria\\OneDrive\\Desktop\\Weather App\\logo.png")
myimage_logo=Label(image=logo_image)
myimage_logo.place(x=200, y=100)

#create and place bottom display box
frame_image=PhotoImage(file="C:\\Users\\adria\\OneDrive\\Desktop\\Weather App\\Copy of box.png")
myframe_image=Label(image=frame_image)
myframe_image.pack(padx=5,pady=5,side=BOTTOM)

#create amd place headers + '...' within bottom display box
label1=Label(root,text="Wind",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="Humidity",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label2.place(x=250,y=400)
label3=Label(root,text="Description",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label3.place(x=430,y=400)
label4=Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("Helvetica",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("Helvetica",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()
