from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    #return 'Hello World!'
    # templateData = {
    #      'time': "what",
    #      'temp': "what",
    #      'hum'	: "what",
    #      'numSamples'	: "what",
    #      'led'  : "what",
    #      'controlSts' : "what",
    #      'HumSts' : "what"}
    return render_template('newIndex.html',title = 'home')

#if __name__ == '__main__':
#    app.run()

if __name__ == "__main__":
    app.run()

