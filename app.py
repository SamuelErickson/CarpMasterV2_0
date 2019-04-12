from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import io



app = Flask(__name__)


@app.route('/')
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    light1Pin= 17
    GPIO.setup(light1Pin, GPIO.OUT)

    if GPIO.input(light1Pin) == GPIO.LOW:
        lightStatus = "OFF"
    elif GPIO.input(light1Pin) == GPIO.HIGH:
        lightStatus = "HIGH"
    else:
        lightStatus = "ERROR"


    df_config = pd.read_csv("tankConfig.csv")
    df_config.set_index(['TankName'], inplace=True)
    df_config.index.name=None
    tables = [df_config.to_html()]

    templateData = {
        'time': "Add time here",
        'tanks': ["A1","A2"],
         'temp': temp,
         'LightNumber'	: "Light1",
          'Light1Status'	: lightStatus,
        'tables': tables
    #      'led'  : "what",
    #      'controlSts' : "what",
    #      'HumSts' : "what"
    }
    return render_template('index.html', **templateData)

@app.route("/tables")
def show_tables():
    df_config = pd.read_csv("tankConfig.csv")
    df_config.set_index(['TankName'], inplace=True)
    df_config.index.name=None
    #return render_template('view.html',tables=[df_config.to_html()])
    #titles = ['na', 'Female surfers', 'Male surfers'])




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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)

#if __name__ == "__main__":
#   app.run()

