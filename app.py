# Demonstrates Bootstrap version 3.3 Starter Template
# available here: https://getbootstrap.com/docs/3.3/getting-started/#examples

from flask import Flask, render_template, send_file
from filepaths import Root


paths = Root(__file__).paths()

app = Flask(__name__)

# home page: about
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/projects')
def about():
    return render_template('projects.html')


@app.route('/lda')
def lda():
    return render_template('LDAvis.html')


@app.route('/AW')
def aw():
    return render_template('AW.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/recgov')
def recgov():
    return render_template('recgov.html')


@app.route('/sendresume')
def sendresume():
    try:
        return send_file('static/images/HunterFeissDataScientist.pdf',
                         attachment_filename='HunterFeissDataScientist.pdf',
                         as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, threaded=True, debug=False, ssl_context = context)
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
