from flask import Flask, render_template, send_file, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    templateData = {
        'time': "Add time here",
        'tanks': ["A1","A2"],
         'temp': "16",
         'LightNumber'	: "Light1",
          'LightStatus'	: "Not Connected"
    #      'led'  : "what",
    #      'controlSts' : "what",
    #      'HumSts' : "what"
    }
    return render_template('index.html', **templateData)

#if __name__ == '__main__':
#    app.run()

if __name__ == "__main__":
   app.run()

