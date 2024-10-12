from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == "__name__":
    app.run(debug=False)
