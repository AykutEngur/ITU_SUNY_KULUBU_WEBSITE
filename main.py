from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hakkimizda')
def about():
    return render_template('hakkimizda.html')

@app.route('/etkinliklerimiz')
def etkinliklerimiz():
    return render_template('etkinliklerimiz.html')


if __name__ == '__main__':
    # Get the port from the environment variable (Railway automatically sets it)
    port = int(os.environ.get("PORT", 5000))
    
    # Run the app, make sure it's listening on all interfaces (0.0.0.0) for Railway
    app.run(host="0.0.0.0", port=port)

