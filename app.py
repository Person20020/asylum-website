from flask import Flask, render_template, request


app = Flask(__name__)


# Navbar
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/getting-started')
def getting_started():
    return render_template('getting-started.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/submitting')
def submitting():
    return render_template('submitting.html')

@app.route('/featured-projects')
def featured_projects():
    return render_template('featured-projects.html')



# Archive
@app.route('/archive/weather-station')
def weather_station():
    return render_template('archive/weather-station.html')

@app.route('/archive/nfc-keychain')
def nfc_keychain():
    return render_template('archive/nfc-keychain.html')



# Guides
@app.route('/guides/nfc-keychain')
def nfc_keychain_guide():
    return render_template('guides/nfc-keychain.html')



# 404 page
@app.route('/<path:undefined_path>')
def catch_all(undefined_path):
    return render_template('404.html', path=undefined_path), 404