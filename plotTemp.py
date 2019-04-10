from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import io
#app.import RPi.GPIO as GPIO

global df_tempData
df_tempData = pd.read_csv("tempData.csv")

def plot_temp():
    #ys = pd.DataFrame([16,15,14,13,10,0,1,2,3,4,5,6,7,6,5])#getDF()['Temperature']
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [C]".encode('utf8'))
    axis.set_xlabel("Samples")
    axis.grid(True)
    axis.set_ylim(0,40)
   # xs = range(len(ys))

    #group by sensor!
    #https://stackoverflow.com/questions/46717359/pandas-plot-multiple-category-lines

   # ys = df_tempData[df_tempData['Sensor']=='Thermo1']["Temp"].values
    #axis.plot(ys)
    for label, grp in df_tempData.groupby('Sensor'):
        grp.plot(x='Time',y = 'Temp',ax=axis, label=label)

    canvas = FigureCanvas(fig)
    #canvas.print_png(output)

plot_temp()