from logging import debug
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import json


@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')

        js = request.form['javascript_data']
        print(js)  # parse as JSON
        return 'dddd'

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return render_template('test.html')

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

   



if __name__ == "__main__":
    app.run(debug='true')

