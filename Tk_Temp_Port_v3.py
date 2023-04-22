import serial
import serial.tools.list_ports
import tkinter as tk
from PIL import Image, ImageTk
import random
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl.workbook import Workbook
import sys
import os


window = tk.Tk()
window.title("Temperature Monitor")
#sun_image = Image.open("sun.png")
sun_icon = ImageTk.PhotoImage("sun.png")
#cloud_image = Image.open("cloud.png")
cloud_icon = ImageTk.PhotoImage("cloud.png")
#rain_image = Image.open("rain.png")
rain_icon = ImageTk.PhotoImage("rain.png")
temperature_label = tk.Label(window, text="0°C", font=("Arial", 24))
weather_icon_label = tk.Label(window, image=sun_icon)
temperature_label.pack(pady=20)
weather_icon_label.pack(pady=20)
serial_ports = list(serial.tools.list_ports.comports())
serial_port_var = tk.StringVar()
serial_port_var.set(serial_ports[0].device)
serial_port_menu = tk.OptionMenu(window, serial_port_var, *list(map(lambda p: p.device, serial_ports)))
serial_port_menu.pack(pady=20)
ser = serial.Serial(serial_port_var.get(), 9600)
temperatures_2 = []
def update_temperature():
    global temperatures_2
    temperature_str = ser.readline().decode('utf-8').strip()
    temperature = float(temperature_str)
    for i in range(10):
        temperatures_2.append(float(temperature_str))
    for i, temperature_str in enumerate(temperatures_2):
        print(f"Temperature {i+1}: {temperature_str:.2f} °C")
    plt.plot(range(1, 11), temperatures_2)
    plt.title('Temperature Data')
    plt.xlabel('Measurement Number')
    plt.ylabel('Temperature (°C)')
    plt.show()
    """
    
    # Set serial connection Replace 'COM3' with the appropriate serial port for # your device
    ser = serial.Serial('COM3', 9600) 

    data = []
    timestamps = []

    for i in range(10):
        temperature = float(ser.readline().strip())
        
        data.append(temperature)
        timestamps.append(datetime.datetime.now())

        time.sleep(1)

    plt.plot(timestamps, data)
    plt.xlabel('Time')
    plt.ylabel('Temperature (Celsius)')
    plt.show()

    df = pd.DataFrame({'Temperature': data, 'Timestamp': timestamps})
    df.to_excel('temperature_data.xlsx', index=False)
    """
    
    df = pd.DataFrame({'Temperature (°C)': temperatures_2})
    df.to_excel('temperatures.xlsx', index=False)
    
    temperature_label.config(text=f"{temperature}°C")

    
    if temperature > 23:
        weather_icon_label.config(image=sun_icon)
    elif temperature > 20:
        weather_icon_label.config(image=cloud_icon)
    else:
        weather_icon_label.config(image=rain_icon)

    
    window.after(1000, update_temperature)


update_temperature()


def update_serial_port(*args):
    ser.port = serial_port_var.get()

    # if you modifie cette scripte make sure fix timming to get your file work even without insert Arduino board

serial_port_var.trace("w", update_serial_port)


window.mainloop()

"""

import serial.tools.list_ports
import serial
import time
import tkinter as tk



ser = None


root = tk.Tk()

ports = serial.tools.list_ports.comports()


temperature = tk.StringVar()
temperature.set("")


temp_label = tk.Label(root, textvariable=temperature)
temp_label.pack()


weather_icon = tk.Label(root)
weather_icon.pack()


def read_from_port():
    global ser
    while True:
        data = ser.readline().decode().strip()

        if data.startswith("T:"):
            temp_str = data.split(":")[1].replace("C", "")
            temperature.set(f"{temp_str} C")

            temp = float(temp_str)
            if temp < 10:
                img = Image.open("rain.png")
            elif temp > 30:
                img = Image.open("sun.png")
            else:
                img = Image.open("cloud.png")
            img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            weather_icon.config(image=photo)
            weather_icon.image = photo

def connect_to_port(port):
    global ser

    if ser is not None:
        ser.close()

    ser = serial.Serial(port, 9600)

    time.sleep(2)

    import threading
    thread = threading.Thread(target=read_from_port)
    thread.start()

port_var = tk.StringVar()
port_menu = tk.OptionMenu(root, port_var, *ports, command=connect_to_port)
port_menu.pack()

root.mainloop()

if ser is not None:
    ser.close()
    
    
    

"""