from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from daikin_aircon_pylib import daikin_aircon


app = Flask(__name__)
CORS(app)

AIRCON_ADDR='10.33.1.244'

def _get_aircon():
    return daikin_aircon.Aircon(AIRCON_ADDR)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return jsonify('Hello')

@app.route('/power/start')
def power_start():
    aircon = _get_aircon()
    aircon.set_power(True)
    return jsonify('OK')

@app.route('/power/stop')
def power_stop():
    aircon = _get_aircon()
    aircon.set_power(False)
    return jsonify('OK')

@app.route('/power/status')
def get_power_status():
    aircon = _get_aircon()
    status={}
    status['power'] = aircon.get_power()
    return jsonify(status)
    
@app.route('/sensor/info')
def get_sensor_info():
    aircon = _get_aircon()
    info = aircon.get_sensor_info()
    return jsonify(info)
    
