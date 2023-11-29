from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('hello', name=name))
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + name

if __name__ == '__main__':
    app.run()
