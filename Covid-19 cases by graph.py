import requests
from pandas import DataFrame #pip install pandas in your terminal
import matplotlib.pyplot as plt #pip install matplotlib in your terminal
import numpy as np #pip install numpy in your terminal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tkwindow #pip install tkinter in your terminal
from tkinter import ttk


r = requests.get('https://pomber.github.io/covid19/timeseries.json')
#The above link form where we are collecting data it may be seems somedays old you can use other api
data = r.json()

def getChart():

    country = name.get() #We are Calling name entered here...!
    if country == '':
        return
    df = DataFrame(data[country]) #Graph starts from here

    figure = plt.figure()
    subplot = figure.add_subplot(111) #Added subplots
    subplot.plot(df['date'], df['confirmed'], label='confirmed', color='blue') #You can change the colors
    subplot.plot(df['date'], df['deaths'], label='deaths', color='red')
    subplot.plot(df['date'], df['recovered'], label='recovered', color='green')
    subplot.legend(loc='upper left')

    start, end = subplot.get_xlim()
    subplot.xaxis.set_ticks(np.arange(start, end, 10))

    for tick in subplot.get_xticklabels():
        tick.set_rotation(45)

    canvas = FigureCanvasTkAgg(figure)
    canvas.get_tk_widget().grid(row=1, column=4, columnspan=3, rowspan=20)
    plt.show()


window = tkwindow.Tk()

name = tkwindow.StringVar()
CountrynameEntered = ttk.Entry(window, width=15, textvariable = name)
CountrynameEntered.grid(column=0, row=1)

button = ttk.Button(window, text = "Show trend for country", command = getChart)
button.grid(column=0, row = 2)

window.mainloop()