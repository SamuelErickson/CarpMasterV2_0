from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import io
#app.import RPi.GPIO as GPIO



app = Flask(__name__)


@app.route('/')
def index():
    global df_thermo1
    df_thermo1 = pd.read_csv("thermo1.csv")

    global df_tempData
    df_tempData = pd.read_csv("tempData.csv")


    temp = 5
    #temp = df_thermo1.loc[df_thermo1.shape[0] - 1, "Temp"]


    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #light1Pin= 17
    #GPIO.setup(light1Pin, GPIO.OUT)

    #if GPIO.input(light1Pin) == GPIO.LOW:
    #    lightStatus = "OFF"
    #elif GPIO.input(light1Pin) == GPIO.HIGH:
    #    lightStatus = "HIGH"
    #else:
    #    lightStatus = "ERROR"

    lightStatus = "not configured for PC test version"

    # Pandas to HTML https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html
    # Return to above to format/style tables

    df_config = pd.read_csv("tankSettings.csv")
    #df_config.index.name=None
    df_status = pd.read_csv("tankStatus.csv")

    ConfigTables = [df_config.to_html(index=False,columns=["TankName","Status","TempSetPoint","TempSensor","Photoperiod (h)","LightsOnTime","LightsOffTime","Lights"])]
    StatusTables = [df_status.to_html(index=False)]

    templateData = {
        'time': "Add time here",
        'tanks': ["A1","A2"],
         'temp': temp,
         'LightNumber'	: "Light1",
          'Light1Status'	: lightStatus,
        'ConfigTables': ConfigTables,
        'StatusTables': StatusTables
    #      'led'  : "what",
    #      'controlSts' : "what",
    #      'HumSts' : "what"
    }
    return render_template('index.html', **templateData)




@app.route('/plot/temp')
def plot_temp():
    ys = df_tempData["Temp"] #.groupby("Sensor")
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
    app.run(host='0.0.0.0', port=80, debug=False)

#if __name__ == "__main__":
#   app.run()

