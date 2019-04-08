# A test file for plotting temps

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

def plot_temp_A2():
    #times, temps, hums = getHistData(numSamples)
    ys = pd.DataFrame([0,1,2,3,4,5,6,7,6,5,4,3,2])#getDF()['Temperature']
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [C]".encode('utf8'))
    axis.set_xlabel("Samples")
    axis.grid(True)
    axis.set_ylim(0,40)
    #xs = range(numSamples)
    axis.plot(ys)
    fig.show()
    #axis.show()
    #canvas = FigureCanvas(fig)
   # output = io.BytesIO()
    #canvas.print_png(output)

#plot_temp_A2()

ys = pd.DataFrame([0,1,2,3,4,5,6,7,6,5,4,3,2])#getDF()['Temperature']
fig = Figure()
axis = fig.add_subplot(1, 1, 1)
axis.set_title("Temperature [C]".encode('utf8'))
axis.set_xlabel("Samples")
axis.grid(True)
axis.set_ylim(0,40)
    #xs = range(numSamples)
axis.plot(ys)
plt.show()