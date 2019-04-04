from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import io


app = Flask(__name__)


@app.route('/')
def index():
    global df_thermo1
    df_thermo1 = pd.read_csv("thermo1.csv")
    templateData = {
        'time': "Add time here",
        'tanks': ["A1","A2"],
         'temp': df_thermo1.loc[df_thermo1.shape[0]-1,"Temp"],
         'LightNumber'	: "Light1",
          'Light1Status'	: "Not Connected"
    #      'led'  : "what",
    #      'controlSts' : "what",
    #      'HumSts' : "what"
    }
    return render_template('index.html', **templateData)

@app.route('/plot/temp/A1')
def plot_temp_A1():
    ys = df_thermo1["Temp"]
    #ys = pd.DataFrame([16,15,14,13,10,0,1,2,3,4,5,6,7,6,5])#getDF()['Temperature']
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [C]".encode('utf8'))
    axis.set_xlabel("Samples")
    axis.grid(True)
    axis.set_ylim(0,40)
   # xs = range(len(ys))
    axis.plot(ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/temp/A2')
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
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=False)

#if __name__ == "__main__":
#   app.run()

