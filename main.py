import os
from flask import Flask, render_template, request

app = Flask("__main__")

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/mentor')
def mentor():
    return render_template('mentor.html')

@app.route('/mentee')
def mentee():
    return render_template('mentee.html')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))